from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from langchain.prompts import load_prompt
from langchain.chains.summarize import load_summarize_chain

from langchain.prompts import load_prompt
from langchain.chains import LLMChain
from langchain.chat_models.gigachat import GigaChat

import conf

chat = GigaChat(credentials=f'{conf.auth_token}', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]


def simple_chat():
    while True:
        user_input = input("User: ")
        messages.append(HumanMessage(content=user_input))
        res = chat(messages)
        messages.append(res)
        print("Bot: ", res.content)


def chat_with_prompt():
    prompt = load_prompt('prompt.yaml')
    chain = prompt | chat
    text = chain.invoke({"text": "искуственый - интилектможет исправить все ощибки"})
    print(text, dir(text))
    print(text.content)


if __name__ == "__main__":
    simple_chat()
    # chat_with_prompt()
