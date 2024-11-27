import streamlit as st

class InputForm:
    @staticmethod
    def render():
        with st.form("research_form"):
            research_input = st.text_area(
                "Enter research topic, URL, or text",
                help="You can enter a URL, paste text, or type your research topic"
            )
            uploaded_file = st.file_uploader(
                "Upload PDF document",
                type=['pdf'],
                help="Upload a PDF document for analysis"
            )
            submit_button = st.form_submit_button("Start Analysis")
        return research_input, uploaded_file, submit_button