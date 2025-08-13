from .providers import OpenAIProvider, OllamaProvider, AIProvider


def get_provider(name: str, api_key: str = None, model: str = None, base_url: str = None) -> AIProvider:
    providers = {
        "openai": OpenAIProvider,
        "ollama": OllamaProvider
    }
    name = name.lower()
    if name not in providers:
        raise ValueError(f"Unknown provider: {name}")
    return providers[name](api_key=api_key, model=model, base_url=base_url)
