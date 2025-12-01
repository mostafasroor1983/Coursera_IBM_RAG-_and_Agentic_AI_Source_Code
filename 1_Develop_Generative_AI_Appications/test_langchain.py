from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Define the LLM (Chat Model)
# We use ChatOpenAI for the best and latest models (gpt-3.5-turbo or gpt-4)
# The API key is automatically picked up from the OPENAI_API_KEY environment variable.
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,  # A value between 0.0 (deterministic) and 1.0 (creative)
)

# 2. Define the Prompt Template
# A ChatPromptTemplate is designed for chat models, using system/user roles.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional software architect. Your answers must be concise, elegant, and focused on design principles.",
        ),
        (
            "user",
            "Explain the difference between monolith and microservices in two sentences.",
        ),
    ]
)

# 3. Create the Chain (Prompt + LLM)
# Using LangChain Expression Language (LCEL) with the pipe operator (|)
chain = prompt | llm

# 4. Invoke the Chain and Print the Result
# The invoke method sends the fully constructed prompt to the LLM.
response = chain.invoke({})

# The response object has a 'content' attribute with the raw text output.
print(response.content)

# Example Output (varies based on temperature):
# "A Monolith is a single, tightly coupled code base, simplifying deployment but making scaling difficult. Microservices are small, independent services communicating via APIs, which enhances agility and specialized scaling."

# nano ~/.zshrc;
# /opt/homebrew/Cellar/python@3.12/3.12.12/libexec
# /Users/mostafasrour/Desktop/Courses/AI-Agents/IBM RAG and Agentic AI - Coursera/Coursera_IBM_RAG-_and_Agentic_AI_Source_Code
# source langchain-env/bin/activate
