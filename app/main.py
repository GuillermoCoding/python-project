from fastapi import FastAPI
from TikTokApi import TikTokApi
import json

app = FastAPI()
api = TikTokApi()

@app.get("/")
def read_root():
    trending = api.discoverMusic()
    return trending
