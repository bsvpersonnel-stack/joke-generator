import requests
from typing import Dict, Optional
from enum import Enum

class JokeAPI(Enum):
    OFFICIAL = "https://official-joke-api.appspot.com/random_joke"
    JOKEAPI = "https://v2.jokeapi.dev/joke/Any"
    DADJOKE = "https://icanhazdadjoke.com/"

class JokeGenerator:
    """Multi-API joke generator with fallback support"""
    
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
    
    def get_joke_from_official(self) -> Optional[Dict]:
        """Fetch from Official Joke API"""
        try:
            response = requests.get(
                JokeAPI.OFFICIAL.value,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            return {
                "source": "Official Joke API",
                "setup": data.get("setup", ""),
                "punchline": data.get("punchline", ""),
                "type": data.get("type", "general")
            }
        except requests.exceptions.RequestException as e:
            print(f"Official API failed: {e}")
            return None
    
    def get_joke_from_jokeapi(self) -> Optional[Dict]:
        """Fetch from JokeAPI"""
        try:
            response = requests.get(
                JokeAPI.JOKEAPI.value,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get("type") == "single":
                return {
                    "source": "JokeAPI",
                    "joke": data.get("joke", ""),
                    "category": data.get("category", ""),
                    "type": "single"
                }
            else:
                return {
                    "source": "JokeAPI",
                    "setup": data.get("setup", ""),
                    "punchline": data.get("delivery", ""),
                    "category": data.get("category", ""),
                    "type": "twopart"
                }
        except requests.exceptions.RequestException as e:
            print(f"JokeAPI failed: {e}")
            return None
    
    def get_joke_from_dadjoke(self) -> Optional[Dict]:
        """Fetch from icanhazdadjoke API"""
        try:
            response = requests.get(
                JokeAPI.DADJOKE.value,
                headers={"Accept": "application/json"},
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            return {
                "source": "icanhazdadjoke",
                "joke": data.get("joke", ""),
                "id": data.get("id", ""),
                "type": "single"
            }
        except requests.exceptions.RequestException as e:
            print(f"Dad Joke API failed: {e}")
            return None
    
    def get_random_joke(self, preferred_api: str = "official") -> Optional[Dict]:
        """Get a random joke with fallback to other APIs"""
        
        # Try preferred API first
        if preferred_api == "official":
            joke = self.get_joke_from_official()
            if joke:
                return joke
            joke = self.get_joke_from_jokeapi()
            if joke:
                return joke
            return self.get_joke_from_dadjoke()
        
        elif preferred_api == "jokeapi":
            joke = self.get_joke_from_jokeapi()
            if joke:
                return joke
            joke = self.get_joke_from_official()
            if joke:
                return joke
            return self.get_joke_from_dadjoke()
        
        elif preferred_api == "dadjoke":
            joke = self.get_joke_from_dadjoke()
            if joke:
                return joke
            joke = self.get_joke_from_official()
            if joke:
                return joke
            return self.get_joke_from_jokeapi()
    
    def print_joke(self, joke: Dict) -> None:
        """Pretty print a joke"""
        if not joke:
            print("❌ Could not fetch joke from any API")
            return
        
        source = joke.get("source", "Unknown")
        print("\n" + "="*60)
        print(f"📝 {source}")
        print("="*60)
        
        if "setup" in joke:
            print(f"Setup: {joke['setup']}")
            print(f"Punchline: {joke['punchline']}")
        else:
            print(f"Joke: {joke.get('joke', '')}")
        
        if "category" in joke:
            print(f"Category: {joke['category']}")
        
        print("="*60 + "\n")

# Usage
if __name__ == "__main__":
    generator = JokeGenerator()
    
    # Get a random joke (with fallback)
    joke = generator.get_random_joke(preferred_api="official")
    generator.print_joke(joke)
