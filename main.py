from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0.9)

messages = [
    SystemMessage(content="You are a Generative AI engineer!"),
    HumanMessage(content="What is a transformer?"),
]


if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)