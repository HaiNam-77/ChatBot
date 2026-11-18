import { createUIMessageStream, createUIMessageStreamResponse } from "ai";

export const maxDuration = 60;

export async function POST(request: Request) {
  try {
    const json = await request.json();
    const message = json.message;
    const messages = json.messages;

    let question = "";
    if (message?.parts && Array.isArray(message.parts)) {
      question = message.parts
        .filter((p: any) => p?.type === "text")
        .map((p: any) => p?.text ?? "")
        .join("");
    } else if (typeof message?.content === "string") {
      question = message.content;
    } else if (Array.isArray(messages) && messages.length > 0) {
      const last = messages[messages.length - 1];
      if (last?.parts && Array.isArray(last.parts)) {
        question = last.parts
          .filter((p: any) => p?.type === "text")
          .map((p: any) => p?.text ?? "")
          .join("");
      } else if (typeof last?.content === "string") {
        question = last.content;
      }
    }

    const chatId = json.id || "default-session";
    const textPartId = `text-${Date.now()}`;

    const stream = createUIMessageStream({
      execute: async ({ writer: dataStream }) => {
        let hasStartedText = false;

        const ensureTextStart = () => {
          if (!hasStartedText) {
            hasStartedText = true;
            dataStream.write({
              type: "text-start",
              id: textPartId,
            });
          }
        };

        const finishText = () => {
          if (hasStartedText) {
            dataStream.write({
              type: "text-end",
              id: textPartId,
            });
            hasStartedText = false;
          }
        };

        // Gửi status ban đầu cho hiệu ứng Shimmer
        dataStream.write({
          type: "data-waiting-status",
          data: {
            phase: "waiting",
            message: "Đang phân tích câu hỏi...",
            modelId: "default-model",
            modelName: "RAG Assistant",
          },
          transient: true,
        });

        // Gọi sang FastAPI Backend (chạy ở cổng 8000)
        let backendRes: Response;
        try {
          backendRes = await fetch("http://127.0.0.1:8000/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              session_id: chatId,
              message: question,
            }),
          });
        } catch (err: any) {
          ensureTextStart();
          dataStream.write({
            type: "text-delta",
            id: textPartId,
            delta: `Không thể kết nối tới FastAPI Backend tại http://127.0.0.1:8000. Hãy kiểm tra xem server FastAPI đã chạy chưa. (${err?.message})`,
          });
          finishText();
          return;
        }

        if (!backendRes.ok || !backendRes.body) {
          ensureTextStart();
          dataStream.write({
            type: "text-delta",
            id: textPartId,
            delta: `Lỗi kết nối tới Backend (mã lỗi ${backendRes.status}).`,
          });
          finishText();
          return;
        }

        const reader = backendRes.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";

        try {
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split("\n");
            buffer = lines.pop() ?? "";

            for (const line of lines) {
              if (!line.trim()) continue;
              try {
                const ev = JSON.parse(line);
                if (ev.type === "rewrite") {
                  // Cập nhật trạng thái đang tra cứu giáo trình
                  dataStream.write({
                    type: "data-waiting-status",
                    data: {
                      phase: "thinking",
                      message: `Đang tra cứu: "${ev.text}"...`,
                      modelId: "default-model",
                      modelName: "RAG Assistant",
                    },
                    transient: true,
                  });
                } else if (ev.type === "token") {
                  ensureTextStart();
                  dataStream.write({
                    type: "text-delta",
                    id: textPartId,
                    delta: ev.text,
                  });
                } else if (ev.type === "done") {
                  finishText();
                } else if (ev.type === "error") {
                  ensureTextStart();
                  dataStream.write({
                    type: "text-delta",
                    id: textPartId,
                    delta: `\n\nCó lỗi xảy ra: ${ev.message}`,
                  });
                  finishText();
                }
              } catch {
                // Bỏ qua lỗi parse của chunk dở dang
              }
            }
          }
        } finally {
          finishText();
        }
      },
    });

    return createUIMessageStreamResponse({ stream });
  } catch (error: any) {
    console.error("API Chat Error:", error);
    return new Response(
      JSON.stringify({ error: error?.message || "Internal server error" }),
      {
        status: 500,
        headers: { "Content-Type": "application/json" },
      }
    );
  }
}

export async function DELETE(request: Request) {
  const { searchParams } = new URL(request.url);
  const id = searchParams.get("id");
  if (id) {
    try {
      await fetch(`http://127.0.0.1:8000/api/sessions/${id}`, {
        method: "DELETE",
      });
    } catch {}
  }
  return Response.json({ status: "ok" });
}
