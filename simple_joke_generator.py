import requests
import json

def get_random_joke():
    """Fetch a random joke from Official Joke API"""
    try:
        response = requests.get(
            "https://official-joke-api.appspot.com/random_joke",
            timeout=5
        )
        response.raise_for_status()
        
        joke_data = response.json()
        
        # Format the joke
        print("\n" + "="*50)
        print(f"📝 {joke_data['type'].upper()}")
        print("="*50)
        print(f"Setup: {joke_data['setup']}")
        print(f"Punchline: {joke_data['punchline']}")
        print("="*50 + "\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

if __name__ == "__main__":
    get_random_joke()
