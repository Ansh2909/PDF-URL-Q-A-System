# Chat with PDF & Webpage Q&A using Google Gemini AI

This repository contains two projects leveraging **Google Gemini AI** and **FAISS Vector Database** to enable Q&A capabilities:
1. **Chat with PDF** - Allows users to upload PDFs and ask questions based on their content.
2. **Webpage Q&A** - Scrapes and processes webpage content for question-answering.

---

## 🚀 Features
✅ **Google Gemini AI** for accurate responses.  
✅ **FAISS Vector Store** for efficient document retrieval.  
✅ **Streamlit UI** for easy interaction.  
✅ **Web Scraping** using BeautifulSoup (for Webpage Q&A).  
✅ **PDF Parsing** using PyPDF2 (for PDF Chat).  

---

## 📌 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### **2️⃣ Set Up Google API Key**
Replace `'Enter your API key'` in the script with your **Google API Key** or set it as an environment variable:
```bash
set GOOGLE_API_KEY='your-api-key'  # On Windows
```

---

## 📖 Usage

### **1️⃣ Running Chat with PDF**
```bash
streamlit run chat_with_pdf.py
```
- Upload PDFs from the sidebar.
- Ask questions about the document.

### **2️⃣ Running Webpage Q&A**
```bash
streamlit run webpage_qa.py
```
- Enter a URL to scrape and process content.
- Ask questions related to the webpage.

---

## ⚡ Technologies Used
- **Python**
- **Streamlit** (Frontend UI)
- **PyPDF2** (PDF Parsing)
- **FAISS** (Vector Search)
- **Google Generative AI (Gemini)** (Text Embeddings & Chat Model)
- **BeautifulSoup** (Web Scraping)

---
