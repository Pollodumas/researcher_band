"""
Blockchain Research System - A multi-agent system for blockchain analysis
"""

from src.config.settings import Settings
from src.services.research_service import ResearchService
from src.ui.components import UIComponents
from src.utils.file_processor import FileProcessor

__version__ = "0.1.0"
__all__ = [
    'Settings',
    'ResearchService',
    'UIComponents',
    'FileProcessor'
]