## File: app/services/gpt_handler.py
```python
import openai

class GPTHandler:
    def __init__(self):
        openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with environment variable in production

    def generate_response(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
```