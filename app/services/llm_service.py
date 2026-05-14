import os
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Respond clearly and concisely.
"""


class LLMService:

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def generate_response(user_message: str) -> str:
        """
        Sends user input to the LLM provider
        and returns generated text.
        """

        response = await client.chat.completions.create(
            model=MODEL_NAME,
            timeout=30,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.choices[0].message.content