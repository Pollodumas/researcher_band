import unittest
from src.agents.blockchain_researcher import BlockchainResearcher
from src.agents.architecture_analyst import ArchitectureAnalyst
from src.agents.technical_validator import TechnicalValidator

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.researcher = BlockchainResearcher()
        self.analyst = ArchitectureAnalyst()
        self.validator = TechnicalValidator()

    def test_researcher_initialization(self):
        self.assertIsNotNone(self.researcher)
        self.assertIsNotNone(self.researcher.agent)
        self.assertEqual(self.researcher.agent.name, "Blockchain Researcher")

    def test_analyst_initialization(self):
        self.assertIsNotNone(self.analyst)
        self.assertIsNotNone(self.analyst.agent)
        self.assertEqual(self.analyst.agent.name, "Architecture Analyst")

    def test_validator_initialization(self):
        self.assertIsNotNone(self.validator)
        self.assertIsNotNone(self.validator.agent)
        self.assertEqual(self.validator.agent.name, "Technical Validator")