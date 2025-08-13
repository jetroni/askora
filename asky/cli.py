import typer
import asyncio
from .factory import get_provider


def main(
        type: str = typer.Option(..., help="Provider type (openai, ollama)"),
        prompt: str = typer.Option(..., help="Prompt to send to the AI"),
        key: str = typer.Option(None, help="API key (not needed for local providers)"),
        model: str = typer.Option(None, help="Model name"),
        base_url: str = typer.Option(None, help="Base URL"),
        async_mode: bool = typer.Option(False, "--async-mode", help="Run in async mode")
):
    """Send a prompt to an AI provider."""
    provider = get_provider(type, api_key=key, model=model, base_url=base_url)
    if async_mode:
        result = asyncio.run(provider.agenerate(prompt))
    else:
        result = provider.generate(prompt)
    typer.echo(result.model_dump_json(indent=2))


app = typer.Typer()
# Register the command
app.command(help="Send a prompt to an AI provider")(main)

if __name__ == "__main__":
    app()
