import streamlit as st
import pathlib

st.set_page_config(page_title="互動學習器", page_icon="📖", layout="wide")

html_dir = pathlib.Path(__file__).parent

PAGES = {
  "📖 互動閱讀器": "reading_companion.html",
  "🔤 50音學習卡": "kana50.html",
}

# 嘗試取得目前頁面
try:
    query = st.query_params
    page_key = query.get("page", "📖 互動閱讀器")
    if page_key not in PAGES:
        page_key = "📖 互動閱讀器"
except Exception:
    page_key = "📖 互動閱讀器"

page = st.sidebar.selectbox("功能", list(PAGES.keys()), index=list(PAGES.keys()).index(page_key))

# 記住用戶選擇
try:
    st.query_params["page"] = page
except Exception:
    pass

html_file = PAGES[page]
html_path = html_dir / html_file

if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.error(f"找不到 {html_file}")