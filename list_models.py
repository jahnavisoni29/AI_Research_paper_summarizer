import os
import google.generativeai as genai

# Configure with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List models
for model in genai.list_models():
    print(model.name)
    print("  Supported methods:", model.supported_generation_methods)
    print()
