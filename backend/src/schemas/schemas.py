from pydantic import BaseModel, Field
from typing import Literal, Optional

class ChatRequest(BaseModel):
    session_id: str = Field(..., min_length=1, max_length=64)
    message: str = Field(..., min_length=1, max_length=2000)
    search_mode: Literal["auto", "local_only", "web_only", "both"] = "auto"

class QueryPlan(BaseModel):
    standalone_query: str = Field(description="Câu hỏi đã làm rõ ngữ cảnh từ lịch sử chat.")
    route_mode: Literal["local_only", "web_only", "both"] = Field(
        description="Chọn 'both' nếu câu hỏi cần đối chiếu giáo trình với thực tế hiện nay."
    )
    local_sub_query: Optional[str] = Field(default=None, description="Truy vấn tìm trong giáo trình.")
    web_sub_query: Optional[str] = Field(default=None, description="Truy vấn tìm trên Exa Web Search.")