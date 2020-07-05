from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from TikTokApi import TikTokApi
import json

app = FastAPI()
api = TikTokApi()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    trending = api.discoverMusic()
    return trending
