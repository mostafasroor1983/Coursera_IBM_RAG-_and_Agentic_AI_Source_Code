from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate

openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper(max_tokens=512).createInstance()


# Increase accuracy of response by showing the intermediates steps and promote the transparency.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional problem solver.",
        ),
        (
            "user",
            """ 
            When I was 6, my sister was half of my age. Now I am 70, what age is my sister?
            Provide three independent calculations and explanations, then determine the most consistent result.
            """,
        ),
    ]
)

chain = prompt | llm
response = chain.invoke({})
print(response.content)
