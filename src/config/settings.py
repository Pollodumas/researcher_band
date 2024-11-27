import os
from typing import Dict, Any
from dotenv import load_dotenv

class Settings:
    @staticmethod
    def get_agent_settings() -> Dict[str, float]:
        load_dotenv()
        return {
            "researcher_temperature": float(os.getenv("RESEARCHER_TEMPERATURE", 0.7)),
            "analyst_temperature": float(os.getenv("ANALYST_TEMPERATURE", 0.5)),
            "validator_temperature": float(os.getenv("VALIDATOR_TEMPERATURE", 0.3))
        }

    @staticmethod
    def get_openai_settings() -> Dict[str, Any]:
        load_dotenv()
        return {
            "api_key": os.getenv("OPENAI_API_KEY")
        }