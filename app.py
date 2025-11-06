import chainlit as cl
from langfuse import Langfuse
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize clients
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hi! Type any question to test the LLM prompt.").send()


@cl.on_message
async def main(message: cl.Message):
    # Log trace
    trace = langfuse.trace(name="prompt_test", input=message.content)

    prompt = f"You are a helpful assistant.\n\nUser: {message.content}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    # Update LangFuse trace
    trace.update(output=answer)
    trace.end()

    # Send back to user
    await cl.Message(content=answer).send()

