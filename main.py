from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Allow frontend to connect (CORS for localhost:5500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load a lightweight English chatbot
chatbot = pipeline("text-generation", model="gpt2")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.message
    response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
    return {"reply": response[len(user_input):].strip()}
