from client_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate

client_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper(max_tokens=50).createInstance()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional translator between English and French.",
        ),
        (
            "user",
            """ 
            Here is an example of translating a sentence from English to French:

            English: “How is the weather today?”
            French: “Comment est le temps aujourd'hui?”
            
            Now, translate the following sentence from English to French:
            
            English: “Where is the nearest supermarket?
            """,
        ),
    ]
)

chain = prompt | llm
response = chain.invoke({})
print(response.content)
