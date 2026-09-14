# 🎭 Random Joke Generator

A Python project that generates random jokes using external APIs with multiple implementations and fallback support.

## Features

✨ **Multiple implementations:**
- Simple script using Official Joke API
- Advanced class with multi-API support and fallback
- FastAPI web service with REST endpoints
- React frontend (optional)

🔄 **Fallback support** - If one API fails, automatically tries the next

🎯 **Three joke sources:**
1. [Official Joke API](https://official-joke-api.appspot.com/)
2. [JokeAPI](https://v2.jokeapi.dev/)
3. [icanhazdadjoke](https://icanhazdadjoke.com/api)

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/bsvpersonnel-stack/joke-generator.git
cd joke-generator

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Option 1: Simple Script

```bash
python simple_joke_generator.py
```

Output:
```
==================================================
📝 GENERAL
==================================================
Setup: What did the buffalo say to his son when he left for college?
Punchline: Bison
==================================================
```

### Option 2: Advanced Generator with Fallback

```bash
python joke_generator.py
```

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

# Get a joke from preferred API (with fallback)
joke = generator.get_random_joke(preferred_api="official")
generator.print_joke(joke)

# Or try a specific source
joke = generator.get_joke_from_dadjoke()
```

### Option 3: FastAPI Web Service

```bash
python joke_api.py
```

Then visit:
- **Interactive Docs:** http://localhost:8000/docs
- **API Root:** http://localhost:8000/
- **Get a joke:** http://localhost:8000/joke?source=official
- **Get multiple:** http://localhost:8000/jokes/5?source=dadjoke

**With curl:**

```bash
# Get a single joke
curl http://localhost:8000/joke?source=official

# Get from different source
curl http://localhost:8000/joke?source=dadjoke

# Get multiple jokes
curl http://localhost:8000/jokes/10?source=jokeapi
```

**API Response Examples:**

```json
{
  "source": "Official Joke API",
  "setup": "Why do programmers prefer dark mode?",
  "punchline": "Because light attracts bugs!",
  "type": "general"
}
```

## Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information and available endpoints |
| GET | `/joke?source={source}` | Get a random joke from specified source |
| GET | `/jokes/{count}?source={source}` | Get multiple jokes (1-50) |

**Source options:** `official`, `jokeapi`, `dadjoke`

## Error Handling

All implementations include robust error handling:

- Connection timeouts (5 seconds)
- Invalid API responses
- Automatic fallback to alternative sources
- User-friendly error messages

## Architecture

```
┌─────────────────────────────────┐
│    Joke Generator Project       │
├─────────────────────────────────┤
│                                 │
│  simple_joke_generator.py       │
│  └─ Basic usage example         │
│                                 │
│  joke_generator.py              │
│  └─ Multi-API with fallback     │
│                                 │
│  joke_api.py                    │
│  └─ FastAPI web service         │
│                                 │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│     External Joke APIs          │
├─────────────────────────────────┤
│                                 │
│  Official Joke API              │
│  JokeAPI                        │
│  icanhazdadjoke                 │
│                                 │
└─────────────────────────────────┘
```

## Project Structure

```
joke-generator/
├── simple_joke_generator.py    # Basic implementation
├── joke_generator.py           # Advanced multi-API class
├── joke_api.py                 # FastAPI service
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Technology Stack

- **Language:** Python 3.7+
- **HTTP Client:** requests
- **Web Framework:** FastAPI
- **Server:** Uvicorn
- **External APIs:** Official Joke API, JokeAPI, icanhazdadjoke

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Joke Sources

- **Official Joke API** - General, Programming, Knock-knock jokes
- **JokeAPI** - Multiple categories with content filtering
- **icanhazdadjoke** - Dad jokes collection

## Example Jokes

```
Setup: Why do programmers prefer dark mode?
Punchline: Because light attracts bugs.
```

```
Setup: What do you call a factory that makes good products?
Punchline: A satisfactory.
```

```
Setup: Why don't scientists trust atoms?
Punchline: Because they make up everything!
```

---

**Built with ❤️ using Python and external APIs**
