from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
from typing import Optional
import uvicorn

app = FastAPI(title="Random Joke Generator API")

JOKE_APIS = {
    "official": "https://official-joke-api.appspot.com/random_joke",
    "jokeapi": "https://v2.jokeapi.dev/joke/Any",
    "dadjoke": "https://icanhazdadjoke.com/"
}

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Joke Generator API",
        "endpoints": {
            "get_joke": "/joke",
            "get_joke_by_source": "/joke?source={source}",
            "get_multiple": "/jokes/{count}?source={source}"
        },
        "available_sources": list(JOKE_APIS.keys())
    }

@app.get("/joke")
async def get_joke(source: str = "official"):
    """Get a random joke from the specified source"""
    
    if source not in JOKE_APIS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid source. Available: {list(JOKE_APIS.keys())}"
        )
    
    try:
        if source == "official":
            response = requests.get(JOKE_APIS[source], timeout=5)
            response.raise_for_status()
            data = response.json()
            return {
                "source": "Official Joke API",
                "setup": data.get("setup"),
                "punchline": data.get("punchline"),
                "type": data.get("type")
            }
        
        elif source == "jokeapi":
            response = requests.get(JOKE_APIS[source], timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if data.get("type") == "single":
                return {
                    "source": "JokeAPI",
                    "joke": data.get("joke"),
                    "category": data.get("category")
                }
            else:
                return {
                    "source": "JokeAPI",
                    "setup": data.get("setup"),
                    "punchline": data.get("delivery"),
                    "category": data.get("category")
                }
        
        elif source == "dadjoke":
            response = requests.get(
                JOKE_APIS[source],
                headers={"Accept": "application/json"},
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            return {
                "source": "icanhazdadjoke",
                "joke": data.get("joke")
            }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"API error: {str(e)}")

@app.get("/jokes/{count}")
async def get_multiple_jokes(count: int = 5, source: str = "official"):
    """Get multiple random jokes"""
    
    if count < 1 or count > 50:
        raise HTTPException(status_code=400, detail="Count must be between 1 and 50")
    
    jokes = []
    for _ in range(count):
        try:
            response = requests.get(
                f"{JOKE_APIS[source]}?count={count}",
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            jokes.append(data)
        except:
            continue
    
    return {"count": len(jokes), "jokes": jokes}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
