import streamlit as st
import pathlib

st.set_page_config(page_title="互動學習器", page_icon="📖", layout="wide")

html_dir = pathlib.Path(__file__).parent

PAGES = {
  "📖 日文閱讀": "reading_companion.html",
  "🔤 50音學習": "kana50.html"
}

with st.sidebar:
  st.title("導航")
  choice = st.radio("選擇功能", list(PAGES.keys()), label_visibility="collapsed")

html_file = PAGES[choice]
html_path = html_dir / html_file

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=900, scrolling=True)