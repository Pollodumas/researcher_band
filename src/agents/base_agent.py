from crewai import Agent
from typing import List

class BaseAgent:
    def __init__(self, name: str, role: str, goals: List[str], backstory: str, temperature: float):
        self.agent = Agent(
            name=name,
            role=role,
            goal=goals[0],  # Set the primary goal
            backstory=backstory,
            temperature=temperature,
            verbose=True
        )