import PyPDF2
import requests
from typing import Dict, Any

class FileProcessor:
    @staticmethod
    def process_pdf(file) -> str:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    @staticmethod
    def process_url(url: str) -> Dict[str, Any]:
        response = requests.get(url)
        response.raise_for_status()
        return {
            'content': response.text,
            'status': response.status_code,
            'headers': dict(response.headers)
        }

    @staticmethod
    def process_text(text: str) -> str:
        # Add any text preprocessing logic here
        return text.strip()