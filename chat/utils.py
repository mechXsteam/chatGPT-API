from dotenv import load_dotenv

load_dotenv()

from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()


def get_response(prompt, context):
    get_response = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=(
                    "You are Chat GPT clone by Aditya Kumar that helps user to find solutions to their problems. "
                )
            ),
            HumanMessagePromptTemplate.from_template(f"Generate response based on {prompt} and {context}"),
        ]
    )

    return llm(get_response.format_messages(prompt=prompt, context=context))
