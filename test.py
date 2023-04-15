import openai
from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables from .env file

api_key = os.environ.get("OPENAI_API_KEY")
org_id = os.environ.get("ORG_ID")

openai.api_key = os.environ["OPENAI_API_KEY"]
prompt = (
    "Please generate a list of t-shirt slogans for me.\n"
    "## Input examples:\n"
    "- I need a t-shirt slogan for a software company\n"
    "- Can you give me some ideas for a t-shirt slogan related to science?\n"
    "## Output examples:\n"
    "- Code like a boss\n"
    "- Science is my jam\n"
    "- Caffeine is my superpower\n"
)

model_engine = "davinci"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=64,
    n=10,
    stop="\n",
    temperature=0.7,
    presence_penalty=0.5,
    frequency_penalty=0.5,
)
slogans = [choice.text.strip('-') for choice in completions.choices]
print(slogans)
