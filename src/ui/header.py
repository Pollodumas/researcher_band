import streamlit as st

class Header:
    @staticmethod
    def render():
        st.title("Blockchain Research System")
        st.markdown("""
        This system analyzes blockchain technologies using a team of AI agents:
        - 🔍 Blockchain Researcher
        - 🏗️ Architecture Analyst
        - ✅ Technical Validator
        """)