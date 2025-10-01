# LLM, agent, memory initialization
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from backend.tools import get_tools

def init_agent(processed_docs=None, vectorstore=None):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    tools = get_tools(llm, vectorstore, processed_docs)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent
