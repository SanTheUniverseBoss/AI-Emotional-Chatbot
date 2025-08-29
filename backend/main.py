from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# Initialize app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load emotion classifier (HuggingFace)
emotion_model = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

# Chat request body
class ChatRequest(BaseModel):
    user_id: str
    text: str
    history: list

@app.post("/chat")
def chat(req: ChatRequest):
    emotion = emotion_model(req.text)[0]
    emo_label = emotion['label']

    # Simple emotional response
    responses = {
        "joy": "That's wonderful! I'm so happy to hear that. 😊",
        "anger": "I can sense some frustration. Want to share more? 😡",
        "sadness": "I'm really sorry you're feeling down. I'm here to listen. 😢",
        "fear": "I hear your worries. You're not alone in this. 😟",
        "neutral": "I see. Tell me more so I can understand better. 🙂"
    }
    reply = responses.get(emo_label.lower(), "I understand. Please go on.")

    return {
        "reply": reply,
        "emotion": {"label": emo_label, "score": emotion['score']}
    }
