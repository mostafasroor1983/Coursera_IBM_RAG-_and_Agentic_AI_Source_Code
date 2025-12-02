from client_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate

client_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper(max_tokens=5).createInstance()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional sentiments analysis",
        ),
        (
            "user",
            """ 
            Here are few examples of classifying emotions in statements:

            Statement: 'I just won my first marathon!'
            Emotion: Joy
            
            Statement: 'I can't believe I lost my keys again.'
            Emotion: Frustration
            
            Statement: 'My best friend is moving to another country.'
            Emotion: Sadness
            
            Now, classify the emotion in the following statement:
            Statement: 'That movie was so scary I had to cover my eyes.’
            """,
        ),
    ]
)

chain = prompt | llm
response = chain.invoke({})
print(response.content)
