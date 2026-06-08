import streamlit as st
import pathlib

st.set_page_config(page_title="互動學習器", page_icon="📖", layout="wide")

html_dir = pathlib.Path(__file__).parent

PAGES = {
  "📖 互動閱讀器": "reading_companion.html",
  "🔤 50音學習卡": "kana50.html",
}

default_idx = 0
query = st.experimental_get_query_params()
if "page" in query and query["page"][0] in PAGES:
  default_idx = list(PAGES.keys()).index(query["page"][0]) if query["page"][0] in PAGES else 0

page = st.sidebar.selectbox("功能", list(PAGES.keys()), index=default_idx)

html_file = PAGES[page]
html_path = html_dir / html_file

if html_path.exists():
  with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()
  st.components.v1.html(html_content, height=800, scrolling=True)
else:
  st.error(f"找不到 {html_file}，請確認檔案存在。")