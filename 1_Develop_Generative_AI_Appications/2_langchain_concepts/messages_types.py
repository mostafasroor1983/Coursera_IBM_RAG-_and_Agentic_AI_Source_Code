from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.messages import HumanMessage, SystemMessage

openaiclient_wrapper = OpenAIChatWrapper()
openai_llm = OpenAIChatWrapper().createInstance()

response = openai_llm.invoke(
    [
        SystemMessage(
            content="You are a helpful AI bot that assists a user in choosing the perfect book to read in one short sentence"
        ),
        HumanMessage(content="I enjoy mystery novels, what should I read?"),
    ]
)
print(response.content)
