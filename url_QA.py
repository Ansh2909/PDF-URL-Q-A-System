import streamlit as st # type: ignore
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai # type: ignore
from langchain.vectorstores import FAISS # type: ignore
from langchain_google_genai import GoogleGenerativeAIEmbeddings # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter # type: ignore
from langchain.docstore.document import Document # type: ignore
import os

# Set up Google Generative AI API Key
os.environ["GOOGLE_API_KEY"] = "Enter Your API Key"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.environ["GOOGLE_API_KEY"])


def scrape_webpage(url):
    """Scrapes text from a webpage."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.get_text() for p in soup.find_all("p")])
        return text
    except Exception as e:
        return f"Error: {e}"

def create_vector_db(text):
    """Creates a FAISS vector store using Google's Embeddings."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = [Document(page_content=chunk) for chunk in text_splitter.split_text(text)]

    vector_db = FAISS.from_documents(documents, embeddings)
    return vector_db

def get_answer(query, vector_db):
    """Retrieves answer using Google Gemini API."""
    retriever = vector_db.as_retriever()
    relevant_docs = retriever.get_relevant_documents(query)
    
    # Combine relevant text
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # Generate response using Google Gemini AI
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Answer the question based on this context:\n\n{context}\n\nQuestion: {query}")
    
    return response.text if response else "No answer found."

# Streamlit UI
st.title("🔍 Webpage Q&A (RAG with Google AI)")

url = st.text_input("Enter a webpage URL:")
if st.button("Scrape & Process"):
    if url:
        with st.spinner("Scraping and processing..."):
            scraped_text = scrape_webpage(url)
            if "Error" not in scraped_text:
                st.session_state.vector_db = create_vector_db(scraped_text)
                st.success("Webpage processed! Ask questions below.")
            else:
                st.error(scraped_text)

# Question Input
if "vector_db" in st.session_state:
    question = st.text_input("Ask a question about the webpage:")
    if st.button("Get Answer"):
        with st.spinner("Searching..."):
            answer = get_answer(question, st.session_state.vector_db)
            st.write("### Answer:")
            st.write(answer)
