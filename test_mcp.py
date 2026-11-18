import os
import asyncio
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

load_dotenv()

async def main():
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        print("Lỗi: Chưa tìm thấy EXA_API_KEY trong file .env!")
        return

    # 1. Cấu hình thông số khởi chạy Exa MCP Server qua npx
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "exa-mcp-server"],
        env={
            **os.environ,
            "EXA_API_KEY": api_key
        }
    )

    print("⏳ Đang kết nối tới Exa MCP Server...")

    # 2. Mở kết nối giao tiếp qua stdio
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Khởi tạo bắt tay (handshake) với server
            await session.initialize()
            print("✅ Đã kết nối MCP Server thành công!")

            # 3. Lấy toàn bộ danh sách Tool mà Exa cung cấp
            tools = await load_mcp_tools(session)
            print(f"📦 Số lượng tools Exa cung cấp: {len(tools)}")
            for t in tools:
                print(f"  - Tool: {t.name}: {t.description[:80]}...")

            # 4. Tìm tool tìm kiếm web (thường là 'web_search_exa')
            search_tool = next((t for t in tools if "web_search" in t.name or "search" in t.name), tools[0])
            print(f"\n🚀 Đang thử gọi tool [{search_tool.name}]...")

            # 5. Gọi thử tìm kiếm
            result = await search_tool.ainvoke({
                "query": "Lý thuyết thông tin Shannon là gì?",
                "numResults": 3
            })

            print("\n--- KẾT QUẢ TÌM KIẾM TỪ MCP ---")
            print(result)

if __name__ == "__main__":
    asyncio.run(main())