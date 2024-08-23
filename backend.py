import google.generativeai as genai
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API keys
gemini_api_key = os.getenv('API_KEY')
search_api_key = os.getenv('SEARCH_API_KEY')  # Example: for Google Custom Search API


if not gemini_api_key or not search_api_key:
    raise ValueError("No API key(s) found. Please set the API_KEY, SEARCH_API_KEY, and SEARCH_ENGINE_ID environment variables.")

# Configure the Gemini API key
genai.configure(api_key=gemini_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def search_web(query):
    # Use a search API to get search results
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': search_api_key,
        'q': query
    }
    response = requests.get(search_url, params=params)
    results = response.json()
    
    # Extract URLs from the search results
    urls = [item['link'] for item in results.get('items', [])]
    return urls

def extract_content(url):
    # Implement content extraction from URL
    return f"Content extracted from {url}"

def process_content(contents):
    # Combine and process the extracted contents
    return ' '.join(contents)

def generate_response(query, processed_content):
    try:
        # Use Gemini to generate a response
        response = model.generate_content(f"Query: {query}\nContent: {processed_content}")
        return response.text.replace('. ', '.\n')
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chatbot_response(query):
    urls = search_web(query)
    contents = [extract_content(url) for url in urls]
    processed_content = process_content(contents)
    response = generate_response(query, processed_content)
    return response

