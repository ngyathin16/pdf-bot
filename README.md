# 📄 PDF Bot with NVIDIA NIM, LangChain & FAISS

🚀 **A powerful AI-driven chatbot that extracts information from PDFs using NVIDIA NIM, FAISS, and LangChain.**  
Users can upload PDFs and ask questions about the content, with real-time responses powered by advanced AI.

![Demo](https://user-images.githubusercontent.com/your-image-link.png)  <!-- Add a demo image/gif here -->

---

## **✨ Features**
✅ **Upload PDFs** – Extracts and processes documents automatically  
✅ **AI-Powered Search** – Uses **NVIDIA NIM + FAISS** for efficient document retrieval  
✅ **Interactive Chat** – Ask questions and get instant, accurate answers  
✅ **Streamlit UI** – Simple and user-friendly web app  

---

## **📦 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/pdf-bot.git
cd pdf-bot
```

### **2️⃣ Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
- Create a `.env` file in the project root:
  ```
  NVIDIA_API_KEY=your_actual_api_key_here
  ```

---

## **🚀 Running the App Locally**
```bash
streamlit run app.py
```
The app will launch in your browser at `http://localhost:8501/` 🎉  

---

## **🌍 Deployment**
### **Option 1: Deploy on Streamlit Cloud**
1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your repository.
3. Set up **Secrets** in Streamlit:
   ```
   NVIDIA_API_KEY = your_actual_api_key_here
   ```
4. Click **Deploy** and share your app link!

### **Option 2: Deploy on Hugging Face Spaces**
1. Create a Hugging Face Space and select **Streamlit**.
2. Upload all project files.
3. Add the API key to **Secrets**.
4. Start your app and share the URL.

---

## **🛠️ Tech Stack**
- **[NVIDIA NIM](https://developer.nvidia.com/nim)** – AI inference models
- **[LangChain](https://python.langchain.com/)** – LLM-powered document processing
- **[FAISS](https://faiss.ai/)** – Efficient vector search
- **[Streamlit](https://streamlit.io/)** – Web UI
- **Python** – Backend scripting

---

## **📌 Example Queries**
- "What is the salary mentioned in the document?"
- "List the benefits described in this contract."
- "Summarize the key points from this report."

---

## **📝 To-Do & Future Improvements**
- [ ] ✅ Support multiple PDFs 📚
- [ ] ✅ Improve response accuracy with **RAG optimizations**
- [ ] ✅ Add file download support
- [ ] ✅ Deploy on more platforms

---

## **📢 Contributing**
Want to improve this project? **Feel free to fork and submit a pull request!** 💡  

---

## **📜 License**
This project is **MIT Licensed**. See the [LICENSE](LICENSE) file for details.

---

## **🙌 Acknowledgments**
Thanks to **NVIDIA, LangChain, and FAISS** for their incredible AI tools!  
Built with ❤️ by [Your Name](https://github.com/YOUR_USERNAME).

