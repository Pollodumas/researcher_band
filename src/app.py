import sys
from pathlib import Path
import os
import streamlit as st
from dotenv import load_dotenv
import pysqlite3
sys.modules['sqlite3'] = pysqlite3

from src.ui.settings_panel import SettingsPanel
from src.ui.input_form import InputForm
from src.ui.results_view import ResultsView
from src.services.research_service import ResearchService
from src.utils.file_processor import FileProcessor

# Configure page
st.set_page_config(
    page_title="Blockchain Research System",
    page_icon="🔍",
    layout="wide"
)

# Load environment variables
load_dotenv()

def main():
    try:
        st.title("Blockchain Research System")
        st.markdown("""
        This system analyzes blockchain technologies using a team of AI agents:
        - 🔍 Blockchain Researcher
        - 🏗️ Architecture Analyst
        - ✅ Technical Validator
        """)
        
        # Get temperature settings from sidebar
        settings = SettingsPanel.render()
        
        # Initialize services with current settings
        research_service = ResearchService(settings)
        file_processor = FileProcessor()
        
        # Render main input form
        research_input, uploaded_file, submit_button = InputForm.render()
        
        if submit_button:
            if not research_input and not uploaded_file:
                st.error("Please provide input text, URL, or upload a PDF file")
                return
                
            with st.spinner("Processing input and performing analysis..."):
                # Process input
                content = ""
                if research_input:
                    if research_input.startswith('http'):
                        content = file_processor.process_url(research_input)['content']
                    else:
                        content = file_processor.process_text(research_input)
                        
                if uploaded_file:
                    pdf_content = file_processor.process_pdf(uploaded_file)
                    content += "\n" + pdf_content
                
                # Perform analysis
                result = research_service.analyze_content(content)
                
                # Display results
                ResultsView.render(result)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()