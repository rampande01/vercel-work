from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inlined student data
students = [
  {
    "name": "sAyX6V4s",
    "marks": 76
  },
  {
    "name": "Q",
    "marks": 14
  },
  {
    "name": "lgVJvtXb",
    "marks": 11
  },
  {
    "name": "8QW",
    "marks": 34
  },
  {
    "name": "pE3MUB",
    "marks": 95
  },
  {
    "name": "G",
    "marks": 89
  },
  {
    "name": "qxnXc6ZMU",
    "marks": 62
  },
  {
    "name": "0Wl",
    "marks": 16
  },
  {
    "name": "k",
    "marks": 21
  },
  {
    "name": "fv317S",
    "marks": 47
  },
  {
    "name": "ZNGc",
    "marks": 61
  },
  {
    "name": "k95o3Mt",
    "marks": 44
  },
  {
    "name": "M1lKNFLzP",
    "marks": 75
  },
  {
    "name": "nLArKY6",
    "marks": 54
  },
  {
    "name": "DWXwhGudyn",
    "marks": 73
  },
  {
    "name": "uAoSmfmtuY",
    "marks": 16
  },
  {
    "name": "hc",
    "marks": 66
  },
  {
    "name": "3eF45Lda",
    "marks": 86
  },
  {
    "name": "Qz5HIYZ2",
    "marks": 96
  },
  {
    "name": "mQ",
    "marks": 83
  },
  {
    "name": "IDnq",
    "marks": 27
  },
  {
    "name": "7tcnJviBcK",
    "marks": 7
  },
  {
    "name": "M",
    "marks": 13
  },
  {
    "name": "YN7O7",
    "marks": 92
  },
  {
    "name": "x",
    "marks": 67
  },
  {
    "name": "rSmwLNv",
    "marks": 31
  },
  {
    "name": "wRj",
    "marks": 53
  },
  {
    "name": "iwC644ceh",
    "marks": 71
  },
  {
    "name": "bW4iYxTLz3",
    "marks": 92
  },
  {
    "name": "3Xvan",
    "marks": 49
  },
  {
    "name": "yWA",
    "marks": 37
  },
  {
    "name": "UDwXfd",
    "marks": 47
  },
  {
    "name": "vr",
    "marks": 48
  },
  {
    "name": "7tbd",
    "marks": 4
  },
  {
    "name": "1LuxN9S",
    "marks": 25
  },
  {
    "name": "zvbFB",
    "marks": 5
  },
  {
    "name": "AQyPf",
    "marks": 75
  },
  {
    "name": "vS1ORxTD",
    "marks": 50
  },
  {
    "name": "b4j",
    "marks": 26
  },
  {
    "name": "A1w5hN2E",
    "marks": 77
  },
  {
    "name": "TjEazhkk",
    "marks": 87
  },
  {
    "name": "Y5PIAt",
    "marks": 68
  },
  {
    "name": "RmuIT",
    "marks": 56
  },
  {
    "name": "po2kDG",
    "marks": 1
  },
  {
    "name": "Ib",
    "marks": 38
  },
  {
    "name": "KuSBi",
    "marks": 81
  },
  {
    "name": "EGi",
    "marks": 2
  },
  {
    "name": "PQcTY5A",
    "marks": 91
  },
  {
    "name": "JA8Z5Kp",
    "marks": 42
  },
  {
    "name": "W5xkyBIx",
    "marks": 3
  },
  {
    "name": "gkoc",
    "marks": 31
  },
  {
    "name": "MD",
    "marks": 30
  },
  {
    "name": "vC",
    "marks": 20
  },
  {
    "name": "13xouw",
    "marks": 52
  },
  {
    "name": "gV",
    "marks": 3
  },
  {
    "name": "8RAgwthbG",
    "marks": 42
  },
  {
    "name": "DhdJToE8r9",
    "marks": 76
  },
  {
    "name": "Z6paMmh",
    "marks": 33
  },
  {
    "name": "R5",
    "marks": 72
  },
  {
    "name": "5KOWsD0",
    "marks": 98
  },
  {
    "name": "roeBIOq",
    "marks": 45
  },
  {
    "name": "Rge",
    "marks": 46
  },
  {
    "name": "Eq",
    "marks": 11
  },
  {
    "name": "5qq2OHRROX",
    "marks": 27
  },
  {
    "name": "mj",
    "marks": 57
  },
  {
    "name": "VBpw0uW",
    "marks": 85
  },
  {
    "name": "aXr",
    "marks": 19
  },
  {
    "name": "yvJVooqxi",
    "marks": 45
  },
  {
    "name": "3qVQZCy",
    "marks": 72
  },
  {
    "name": "pKBgHiIc",
    "marks": 59
  },
  {
    "name": "l6Gd2T9VKp",
    "marks": 12
  },
  {
    "name": "U9spNsK",
    "marks": 91
  },
  {
    "name": "H3HrF",
    "marks": 72
  },
  {
    "name": "h",
    "marks": 26
  },
  {
    "name": "YZIU93kyz",
    "marks": 84
  },
  {
    "name": "6VE5BCj",
    "marks": 74
  },
  {
    "name": "A1zu",
    "marks": 94
  },
  {
    "name": "DlsAa",
    "marks": 23
  },
  {
    "name": "Ae7FTLvM",
    "marks": 88
  },
  {
    "name": "vxQr",
    "marks": 30
  },
  {
    "name": "la2uv",
    "marks": 70
  },
  {
    "name": "u5upRM",
    "marks": 32
  },
  {
    "name": "689",
    "marks": 92
  },
  {
    "name": "Kk",
    "marks": 50
  },
  {
    "name": "lC2LB6X",
    "marks": 56
  },
  {
    "name": "nLnONA8VwO",
    "marks": 72
  },
  {
    "name": "kgs",
    "marks": 14
  },
  {
    "name": "GJYG1M",
    "marks": 47
  },
  {
    "name": "E",
    "marks": 28
  },
  {
    "name": "ckXNBJWy",
    "marks": 67
  },
  {
    "name": "zyf",
    "marks": 92
  },
  {
    "name": "DPw83V5tt",
    "marks": 43
  },
  {
    "name": "tMzjlJL",
    "marks": 80
  },
  {
    "name": "QAk2v3lW",
    "marks": 25
  },
  {
    "name": "RF",
    "marks": 18
  },
  {
    "name": "B1",
    "marks": 53
  },
  {
    "name": "sj41OzP",
    "marks": 9
  },
  {
    "name": "I9Y",
    "marks": 98
  },
  {
    "name": "AjQyTyW8",
    "marks": 86
  },
  {
    "name": "ANpCZ",
    "marks": 32
  }
]
from fastapi import Query

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):

