"use server";

import { cookies } from "next/headers";

export async function saveChatModelAsCookie(model: string) {
  const cookieStore = await cookies();
  cookieStore.set("chat-model", model);
}

export async function deleteTrailingMessages(_params: { id: string }) {
  // Đã lược bỏ database
}

export async function updateChatVisibility(_params: {
  chatId: string;
  visibility: string;
}) {
  // Đã lược bỏ database
}