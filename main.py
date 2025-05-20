from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = [
    {"name": "Q", "marks": 14},
    {"name": "AjQyTyW8", "marks": 86},
    {"name": "ANpCZ", "marks": 32},
    # Add all 100 here...
]

@app.get("/")
def root():
    return {"message": "Use /api?name=NAME to get marks."}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    name_to_marks = {s["name"]: s["marks"] for s in students}
    return {"marks": [name_to_marks.get(n, None) for n in name]}
