# Define a detailed prompt template.
# This template should guide the model to generate a business name, 
# a short description, the target audience, and potential revenue streams.

BUSINESS_IDEA_PROMPT = """
You are an innovative business strategist and entrepreneur. Your task is to generate creative and viable business ideas for the {domain} domain.

Please generate exactly 5 unique business ideas following this format for each idea:

**Business Idea {number}:**
- **Business Name:** [Creative and memorable name]
- **Description:** [2-3 sentences describing the core concept and value proposition]
- **Target Audience:** [Specific demographic or market segment]
- **Revenue Streams:** [List 2-3 potential ways to generate income]

Requirements:
- Each idea should be innovative and address real market needs
- Focus on scalability and modern market trends
- Include both B2B and B2C opportunities where relevant
- Consider technology integration and sustainability aspects
- Make sure each idea is distinct and not repetitive

Domain: {domain}

Please provide creative, well-thought-out business ideas that could realistically be implemented in today's market.
"""