#!/usr/bin/env python3
"""
Test script to check Gemini model availability and API connection.
"""

import google.generativeai as genai
import os

def test_api_connection():
    """Test the Gemini API connection and list available models."""
    
    # Get API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        api_key = input("Enter your Gemini API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided")
        return
    
    try:
        # Configure the API
        genai.configure(api_key=api_key)
        print("✅ API configured successfully")
        
        # List available models
        print("\n📋 Available models:")
        models = genai.list_models()
        for model in models:
            print(f"  - {model.name}")
            if hasattr(model, 'supported_generation_methods'):
                print(f"    Supported methods: {model.supported_generation_methods}")
        
        # Test a simple generation
        print("\n🧪 Testing model generation...")
        
        # Try different model names
        test_models = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
        
        for model_name in test_models:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content("Hello, world!")
                print(f"✅ {model_name}: {response.text[:50]}...")
                break
            except Exception as e:
                print(f"❌ {model_name}: {str(e)}")
        
    except Exception as e:
        print(f"❌ API Error: {str(e)}")

if __name__ == "__main__":
    test_api_connection()
