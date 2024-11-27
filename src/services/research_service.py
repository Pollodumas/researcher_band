from typing import List, Dict
from crewai import Crew, Agent, Task
from src.agents.blockchain_researcher import BlockchainResearcher
from src.agents.architecture_analyst import ArchitectureAnalyst
from src.agents.technical_validator import TechnicalValidator
from src.templates.prompts import ResearchPrompts

class ResearchService:
    def __init__(self, settings: Dict[str, float] = None):
        if settings is None:
            settings = {
                "researcher_temperature": 0.7,
                "analyst_temperature": 0.5,
                "validator_temperature": 0.3
            }
        
        self.researcher = BlockchainResearcher(settings["researcher_temperature"])
        self.analyst = ArchitectureAnalyst(settings["analyst_temperature"])
        self.validator = TechnicalValidator(settings["validator_temperature"])
        self.prompts = ResearchPrompts()

    def get_agents(self) -> List[Agent]:
        return [
            self.researcher.agent,
            self.analyst.agent,
            self.validator.agent
        ]

    def analyze_content(self, content: str) -> str:
        # Create specific tasks for each agent
        research_task = Task(
            description=self.prompts.INITIAL_RESEARCH.format(content=content),
            expected_output="Detailed research analysis of the blockchain technology, including key innovations, architectural implications, and potential use cases.",
            agent=self.researcher.agent
        )

        analysis_task = Task(
            description=self.prompts.ARCHITECTURE_ANALYSIS,
            expected_output="Comprehensive architectural evaluation focusing on scalability, security, and integration aspects.",
            agent=self.analyst.agent
        )

        validation_task = Task(
            description=self.prompts.TECHNICAL_VALIDATION,
            expected_output="Technical validation report covering implementation complexity, performance impact, and security considerations.",
            agent=self.validator.agent
        )

        # Create and kickoff the crew
        crew = Crew(
            agents=self.get_agents(),
            tasks=[research_task, analysis_task, validation_task]
        )
        
        return crew.kickoff()