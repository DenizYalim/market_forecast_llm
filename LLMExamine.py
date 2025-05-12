import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
(os.getenv("OPENAI_API_KEY"))
client = openai.OpenAI()

headline = "Elon musk dies. Stockholders expect X to be more usable now"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a financial analyst."},
        {"role": "user", "content": "Will this headline cause a stock to rise or fall? Headline: Apple reports record profits."}
    ]
)

print(response.choices[0].message.content)
