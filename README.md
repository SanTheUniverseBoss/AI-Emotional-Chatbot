# AI-Emotional-Chatbot
# Quick next steps after downloading the zip file :
Unzip, open the backend folder and install deps:
Run backend:
cd backend
pip install -r requirements.txt
uvicorn main:app --reload (from the backend directory)
Serve frontend (recommended) and open in browser:
cd frontend
python -m http.server 5500
Then
Open http://127.0.0.1:5500/index.html
## AI Model Integration
This project supports real AI models via Hugging Face 🤗.
### Requirements
```bash
pip install transformers torch
## 🚀 Next Steps for You
1. Download + unzip the repo I gave.  
2. Run through **Step 1** → Push to GitHub.  
3. Upgrade to **Step 2** → Real AI backend.  
4. Commit changes:  
   ```bash
   git add .
   git commit -m "🤖 Added Hugging Face AI models for chatbot + emotion detection"
   git push
