from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dataframe import generate_dataframe

df = generate_dataframe(min_freq=10000)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {
        'data': df.to_dict(orient='records')
    }