# Retrieval, summarizer, calculator, search tools
from langchain.chains import LLMMathChain, RetrievalQA
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool

def get_tools(llm, vectorstore=None, processed_docs=None):
    tools = []

    # Calculator
    calc_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    tools.append(Tool(
        name="Calculator",
        func=calc_chain.run,
        description="Perform math calculations like percentages, growth rates, ratios."
    ))

    # Web search
    tools.append(Tool(
        name="Web Search",
        func=DuckDuckGoSearchRun().run,
        description="Search the web for up-to-date financial news or facts."
    ))

    # Financial news retrieval
    if vectorstore:
        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        def retrieve_with_sources(query: str):
            docs = retriever.invoke({"query": query})["output"]
            if not docs:
                return "No relevant documents found."
            sources = "\n".join([doc.metadata.get("source", "unknown") for doc in docs])
            qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
            result = qa_chain({"query": query})
            return f"{result.get('result', 'No answer found.')}\n\n**Sources:**\n{sources}"

        tools.append(Tool(
            name="Financial News Retriever",
            func=retrieve_with_sources,
            description="Answer questions from uploaded financial news articles with sources."
        ))

        # Summarizer
        def summarize_articles(_input=None):
            if not processed_docs:
                return "❌ No articles available to summarize."
            from langchain.chains.summarize import load_summarize_chain
            chain = load_summarize_chain(llm, chain_type="map_reduce")
            summary = chain.invoke({"input_documents": processed_docs})
            sources = "\n".join([doc.metadata.get("source", "unknown") for doc in processed_docs])
            return f"{summary['output_text']}\n\n**Sources:**\n{sources}"

        tools.append(Tool(
            name="Summarizer",
            func=summarize_articles,
            description="Summarize all uploaded articles with sources."
        ))

    return tools
