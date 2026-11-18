# backend/src/core/exa_search.py
import httpx
import logging
from typing import List, Dict, Any
from src.config import EXA_API_KEY

logger = logging.getLogger(__name__)

class ExaSearchClient:
    def __init__(self, api_key: str = EXA_API_KEY, timeout: float = 6.0):
        self.api_key = api_key
        self.timeout = timeout
        self.base_url = "https://api.exa.ai/search"

    async def search(self, query: str, num_results: int = 4) -> List[Dict[str, Any]]:
        if not self.api_key:
            logger.warning("Chưa cấu hình EXA_API_KEY.")
            return []

        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "query": query,
            "type": "auto",          # Exa tự chọn giữa neural search và keyword search
            "numResults": num_results,
            "contents": {
                "highlights": {      # Chỉ lấy các đoạn trích đắt giá nhất để đưa vào RAG
                    "numSentences": 4,
                    "highlightsPerUrl": 2
                }
            }
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.post(self.base_url, headers=headers, json=payload)
                resp.raise_for_status()
                data = resp.json()

                docs = []
                for item in data.get("results", []):
                    highlights = item.get("highlights", [])
                    content = "\n".join(highlights) if highlights else item.get("text", "")
                    if content.strip():
                        docs.append({
                            "content": content.strip(),
                            "metadata": {
                                "title": item.get("title", "Tài liệu Web"),
                                "source": item.get("url", ""),
                                "source_type": "web"
                            }
                        })
                return docs
        except Exception as e:
            logger.error(f"Lỗi gọi Exa Search: {e}")
            return []