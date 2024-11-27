# Blockchain Research System

A multi-agent system for blockchain research and analysis using Crew AI and Streamlit.

## Features

- Three specialized AI agents:
  - Blockchain Researcher
  - Architecture Analyst
  - Technical Validator
- Process multiple input types:
  - Text input
  - URLs
  - PDF documents
- Interactive web interface
- Comprehensive analysis reports

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blockchain-research-system.git
cd blockchain-research-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
RESEARCHER_TEMPERATURE=0.7
ANALYST_TEMPERATURE=0.5
VALIDATOR_TEMPERATURE=0.3
```

## Running the Application

### Web Interface
```bash
streamlit run src/app.py
```

### Command Line Interface
```bash
python main.py
```

## Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your secrets in the Streamlit Cloud dashboard:
   - OPENAI_API_KEY
   - RESEARCHER_TEMPERATURE
   - ANALYST_TEMPERATURE
   - VALIDATOR_TEMPERATURE

## Project Structure

```
├── src/
│   ├── agents/          # AI agents implementation
│   ├── config/          # Configuration settings
│   ├── services/        # Business logic
│   ├── templates/       # Prompt templates
│   ├── ui/             # UI components
│   └── utils/          # Utility functions
├── tests/              # Test files
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License