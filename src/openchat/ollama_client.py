import ollama
from typing import List, Dict, Generator

def get_local_models() -> List[str]:
    """
    Fetch the list of available models from the local Ollama server.
    """
    try:
        response = ollama.list()
        print(f"Ollama list response: {response}") # Debugging output

        # Handle different response formats across Ollama versions 
        if isinstance(response, dict) and 'models' in response:
            models = [model['name'] if isinstance(model, dict) else getattr(model, 'model', getattr(model, 'name', 'unknown')) for model in response['models']]
        elif hasattr(response, 'models'): # Handle object-based response (like the one we see in logs)
            models = [getattr(model, 'model', getattr(model, 'name', 'unknown')) for model in response.models]
        elif isinstance(response, list):
            models = [m['name'] if isinstance(m, dict) else getattr(m, 'model', getattr(m, 'name', 'unknown')) for m in response]
        else:
            models = []

        return models
    except Exception as e:
        print(f"Error fetching local models: {e}")
        return []

def generate_chat_response(model: str, messages: List[Dict[str, str]]) -> Generator[str, None, None]:
    """
    A generator that calls ollama.chat with streaming enabled and yields content chunks.
    """
    try:
        stream = ollama.chat(
            model=model,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            yield chunk['message']['content']
    except Exception as e:
        yield f"Error generating response: {str(e)}"
