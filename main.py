from fastapi import FastAPI
from objects.data import (surround_in_array)
from modules import decisions
from fastapi.middleware.cors import CORSMiddleware
from objects.body import Body

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/decisions")
def get_decision(body: Body):
    results = decisions.get_teory(
            alternatives=surround_in_array(body.dict()["matrix"]),
            probabilities=surround_in_array(body.dict()["probabilities"]),
            dependsProbabilities=surround_in_array(body.dict()["depends_probabilities"])
    )

    return results
