import google.generativeai as genai
import os
from prompts import BUSINESS_IDEA_PROMPT

class BusinessIdeaGenerator:
    def __init__(self, api_key=None):
        """
        Initialize the Business Idea Generator with Gemini API.
        
        Args:
            api_key (str): Your Gemini API key. If None, will look for GEMINI_API_KEY environment variable.
        """
        if api_key is None:
            api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("API key is required. Set GEMINI_API_KEY environment variable or pass api_key parameter.")
        
        genai.configure(api_key=api_key)
        
        # Try different model names in order of preference
        model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro', 'models/gemini-1.5-flash']
        
        for model_name in model_names:
            try:
                self.model = genai.GenerativeModel(model_name)
                print(f"✅ Using model: {model_name}")
                break
            except Exception as e:
                print(f"⚠️ Model {model_name} not available: {str(e)}")
                continue
        else:
            raise ValueError("No available Gemini models found. Please check your API key and model availability.")
    
    def list_available_models(self):
        """
        List all available Gemini models for debugging.
        """
        try:
            models = genai.list_models()
            print("Available models:")
            for model in models:
                print(f"  - {model.name}")
        except Exception as e:
            print(f"Error listing models: {str(e)}")
    
    def generate_business_ideas(self, domain):
        """
        Generate business ideas for a given domain.
        
        Args:
            domain (str): The business domain (e.g., "sustainable fashion", "personalized nutrition")
            
        Returns:
            str: Generated business ideas text
        """
        try:
            # Format the prompt with the domain
            formatted_prompt = BUSINESS_IDEA_PROMPT.format(domain=domain, number="{number}")
            
            # Generate content using Gemini
            response = self.model.generate_content(formatted_prompt)
            
            return response.text
            
        except Exception as e:
            return f"Error generating business ideas: {str(e)}"
    
    def display_ideas(self, ideas_text):
        """
        Display the generated business ideas in a formatted way.
        
        Args:
            ideas_text (str): The generated business ideas text
        """
        print("\n" + "="*80)
        print("🚀 GENERATED BUSINESS IDEAS 🚀")
        print("="*80)
        print(ideas_text)
        print("="*80)

def main():
    """
    Main function to run the Business Idea Generator.
    """
    print("Welcome to the Business Idea Generator!")
    print("This tool uses Google's Gemini AI to generate innovative business ideas.")
    print("-" * 60)
    
    # Get API key from user or environment
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("\n⚠️  API Key Setup Required:")
        print("1. Get your free API key from: https://ai.google.dev/")
        print("2. Set environment variable: set GEMINI_API_KEY=your_api_key_here")
        print("3. Or enter it below (not recommended for production)")
        
        api_key = input("\nEnter your Gemini API key (or press Enter if set as environment variable): ").strip()
        if not api_key:
            api_key = os.getenv('GEMINI_API_KEY')
    
    try:
        # Initialize the generator
        generator = BusinessIdeaGenerator(api_key)
        
        # Optionally list available models for debugging
        # Uncomment the next line if you want to see all available models
        # generator.list_available_models()
        
        while True:
            print("\n" + "-" * 60)
            domain = input("Enter a business domain (e.g., 'sustainable fashion', 'personalized nutrition'): ").strip()
            
            if not domain:
                print("Please enter a valid business domain.")
                continue
            
            print(f"\n🔄 Generating business ideas for: {domain}")
            print("Please wait...")
            
            # Generate business ideas
            ideas = generator.generate_business_ideas(domain)
            
            # Display the results
            generator.display_ideas(ideas)
            
            # Ask if user wants to generate more ideas
            continue_choice = input("\nWould you like to generate ideas for another domain? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                break
        
        print("\nThank you for using the Business Idea Generator! 🎉")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("Please make sure you have a valid Gemini API key.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()