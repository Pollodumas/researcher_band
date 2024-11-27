class ResearchPrompts:
    INITIAL_RESEARCH = """
    Analyze the following blockchain-related content and provide a comprehensive research summary:
    {content}
    Focus on:
    1. Key technological innovations
    2. Architectural implications
    3. Potential use cases
    """

    ARCHITECTURE_ANALYSIS = """
    Based on the research findings, evaluate the architectural aspects:
    {research_findings}
    Consider:
    1. Scalability considerations
    2. Security implications
    3. Integration challenges
    """

    TECHNICAL_VALIDATION = """
    Validate the technical feasibility of the proposed architecture:
    {architecture_analysis}
    Evaluate:
    1. Implementation complexity
    2. Performance impact
    3. Security considerations
    """