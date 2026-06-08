import streamlit as st
import pathlib

st.set_page_config(page_title="互動閱讀器", page_icon="📖")

html_path = pathlib.Path(__file__).parent / "reading_companion.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)