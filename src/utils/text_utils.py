import re
import unicodedata

def bo_dau(text: str) -> str:
    """Loại bỏ dấu tiếng Việt để tối ưu cho BM25."""
    t = unicodedata.normalize("NFD", text.lower().replace("đ", "d"))
    return "".join(c for c in t if unicodedata.category(c) != "Mn")

def protect_math_blocks(text: str):
    """Thay thế tạm thời các khối công thức $$...$$ bằng token cố định độ dài."""
    math_blocks = []

    def replacer(match):
        math_blocks.append(match.group(0))
        return f"__MATH_BLOCK_{len(math_blocks) - 1:06d}__"

    protected_text = re.sub(r'\$\$.*?\$\$', replacer, text, flags=re.DOTALL)
    return protected_text, math_blocks

def restore_math_blocks(text: str, math_blocks: list) -> str:
    """Khôi phục lại các khối công thức toán học ban đầu."""
    def replacer(match):
        idx = int(match.group(1))
        if 0 <= idx < len(math_blocks):
            return math_blocks[idx]
        return match.group(0)

    return re.sub(r'__MATH_BLOCK_(\d{6})__', replacer, text)