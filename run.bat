@echo off
echo ==============================================
echo   DANG KHOI CHAY BACKEND VA FRONTEND...
echo ==============================================

:: 1. Chay Backend FastAPI o 1 cua so rieng
start "FastAPI Backend" cmd /k "cd backend && ..\.venv\Scripts\uvicorn.exe src.api.chat_router:app --reload --port 8000"

:: 2. Chay Frontend Next.js bang pnpm o 1 cua so rieng
start "Next.js Frontend" cmd /k "cd frontend && pnpm dev"

echo Da khoi dong xong! Mo trinh duyet tai http://localhost:3000