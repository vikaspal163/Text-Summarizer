
🚀 AI Text Summarizer

A modern, production-ready AI-powered text summarization web app built using FastAPI and T5 Transformer models. This tool converts long text or dialogues into concise, readable summaries with a sleek chat-style interface.

✨ Features
🧠 Transformer-based Summarization using T5
⚡ Fast API backend with FastAPI
💬 Interactive chat-style UI
📜 Input cleaning & post-processing
📥 Download summaries as .txt
📋 Copy to clipboard functionality
🕘 Local history storage (browser-based)
🎨 Clean, modern UI with responsive design
🛠️ Tech Stack

Backend

FastAPI
PyTorch
Hugging Face Transformers (T5)

Frontend

HTML, CSS, JavaScript
Lucide Icons
Jinja2 Templates
📂 Project Structure
.
├── app.py                  # FastAPI backend
├── templates/
│   └── index.html          # Frontend UI
├── saved_summary_model/    # Pretrained T5 model (local)
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
🧠 Model Setup

Make sure your trained T5 model is placed in:

./saved_summary_model/

This should include:

model weights
tokenizer files
▶️ Running the App
uvicorn app:app --reload

Open in browser:

http://127.0.0.1:8000
📡 API Endpoint
POST /summarize/

Request

{
  "dialogue": "Your long text here..."
}

Response

{
  "summary": "Concise summarized text."
}
🧩 Key Functionalities
🔹 Text Cleaning
Removes extra spaces, line breaks, HTML tags
🔹 Summarization Pipeline
Prefix-based T5 input (summarize:)
Tokenization & truncation
Beam search generation
🔹 Post-processing
Capitalization correction
Sentence completion
📸 UI Highlights
Chat-style conversation interface
Typing animation for responses
Sidebar with history tracking
Responsive layout (mobile-friendly)
🚧 Future Improvements
🌐 Deploy to cloud (AWS / Vercel / Render)
📊 Add summary length control
🧾 Export to PDF
🔐 User authentication
📚 Multi-language support
🤝 Contributing

Contributions are welcome!

# Fork the repo
# Create your feature branch
git checkout -b feature/AmazingFeature

# Commit changes
git commit -m "Add AmazingFeature"

# Push
git push origin feature/AmazingFeature
📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Your Name

GitHub: https://github.com/vikaspal163

⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!
