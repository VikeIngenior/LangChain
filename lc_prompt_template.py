
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-4o', temperature=0.1)

system_prompt = "You are an expert linguistic."
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

print(chain.invoke({"text" : "Translate this sentence to Turkish: Hello, are you an engineer?"}))
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
model = ChatOpenAI(model="gpt-4")

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

parser = StrOutputParser()

chain = prompt_template | model | parser


if __name__ == "__main__":
    print(chain.invoke({"language": "italian", "text": "hi"}))
"""