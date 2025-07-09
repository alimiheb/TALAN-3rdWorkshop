# Business Idea Generator

A Python application that generates innovative business ideas using Google's Gemini AI for any given domain.

## Features

- 🚀 Generate 5 unique business ideas for any domain
- 💡 Each idea includes: Business Name, Description, Target Audience, and Revenue Streams
- 🎯 Focuses on scalable, modern, and realistic business concepts
- 🔄 Interactive CLI interface for multiple domain queries
- 🛡️ Proper error handling and user-friendly experience

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your Gemini API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Create an account or sign in
3. Generate a free API key
4. Copy the API key

### 3. Set Your API Key

**Option A: Environment Variable (Recommended)**
```bash
# Windows PowerShell
$env:GEMINI_API_KEY = "your_api_key_here"

# Windows Command Prompt
set GEMINI_API_KEY=your_api_key_here

# Linux/Mac
export GEMINI_API_KEY="your_api_key_here"
```

**Option B: Enter when prompted**
The application will ask for your API key if it's not set as an environment variable.

## Usage

Run the application:

```bash
python main.py
```

### Example Domains to Try

- "sustainable fashion"
- "personalized nutrition"
- "remote work tools"
- "mental health technology"
- "urban agriculture"
- "elderly care services"
- "educational technology"
- "renewable energy"

## Project Structure

```
business_idea_generator/
├── main.py           # Main application logic
├── prompts.py        # Prompt templates for Gemini AI
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Sample Output

```
🚀 GENERATED BUSINESS IDEAS 🚀
================================================================================

**Business Idea 1:**
- **Business Name:** EcoThread Collective
- **Description:** A subscription service that creates custom sustainable clothing...
- **Target Audience:** Environmentally conscious millennials and Gen Z consumers...
- **Revenue Streams:** Monthly subscriptions, premium customization fees, partnerships...

[... 4 more business ideas ...]
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid or missing API keys
- Network connectivity issues
- API rate limits
- Invalid user input

## Contributing

Feel free to enhance the application by:
- Adding more detailed prompt templates
- Implementing business idea saving functionality
- Adding market research integration
- Creating a web interface

## License

This project is for educational purposes as part of the TALAN 3rd Workshop challenge.
