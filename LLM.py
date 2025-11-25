from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)  # Load your OpenAI API key from the local api setup file


# Abstract Parent Class
class _base_LLM:
    def __init__(self, model, name="unnamed_LLM"):
        print(f"Initializing a {model} named {name} ")
        self.model = model
        self.name = name 

    def work(self, prompt):
        response, tokens_input, tokens_output = self.__getResponse(
            prompt=prompt, context=self.context
        )

        return response

    def __getResponse(self, prompt, context):  #  -> tuple[str, int, int]
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt},
            ],
        )
        response_text = response.choices[0].message.content

        return (
            response_text,
            response.usage.prompt_tokens,
            response.usage.completion_tokens,
        )


class example_llm(_base_LLM):
    def __init__(
        self,
        model="gpt-4o-mini",
        name="consulter",
        flow_id=None,
        loc_override="",
        ticker="",
    ):
        super().__init__(
            name=name, model=model, loc_override=loc_override, ticker=ticker
        )

        self.context = f"""
            """
