import os
APIKEYSCHATBOT=os.getenv("APIKEYSCHATBOT")
os.environ["AZURE_AI_SEARCH_SERVICE_NAME"]="GENAI_PROJECTS"
os.environ["AZURE_AI_SEARCH_INDEX_NAME"]="azuretable-index"
# os.environ["AZURE_AI_SEARCH_API_KEY"]=os.getenv("AZURE_AI_SEARCH_API_KEY")
os.environ["AZURE_AI_SEARCH_API_KEY"]=os.getenv("AZURESEARCH")


import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.retrievers import AzureAISearchRetriever
from langchain_openai import AzureChatOpenAI

# ---- Azure Search ----
# retriever = AzureAISearchRetriever(
#     azure_search_endpoint=AZURE_SEARCH_ENDPOINT,
#     azure_search_key=AZURE_SEARCH_KEY,
#     index_name="azuretable-index",
#     content_key="Answer",
#     top_k=3,
# )
retriever = AzureAISearchRetriever(
    content_key="Answer",
    top_k=3,
    index_name = "azuretable-index"
)


# ---- Prompt ----
prompt = ChatPromptTemplate.from_template(
    """Answer the question based ONLY on the context below.

Context:
{context}

Question:
{question}
"""
)
st.title("Azure Data Analytics Search Chatbot")
# ---- LLM ----
llm = AzureChatOpenAI(
    model_name="DeepSeek-V3.2",  # DEPLOYMENT NAME
    api_key=APIKEYSCHATBOT,
    azure_endpoint="https://theai-mjx3u7kh-swedencentral.services.ai.azure.com",
    api_version="2024-05-01-preview",
)

# ---- Chain ----
chain = (
    {
        "context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)
# from langchain_core.runnables.base import RunnableDict

# chain = (
#     RunnableDict({
#         "context": retriever,
#         "question": RunnablePassthrough()
#     })
#     | prompt
#     | llm
#     | StrOutputParser()
# )


# ---- Streamlit Chat ----
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_question := st.chat_input("How can I help you?"):
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke(user_question)
            st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

