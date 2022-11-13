from os import error
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from modules import decisions, games, queues
from objects.data import (surround_in_array)
from objects.body import Body, BodyEconomicAnalysis, BodyQueuesProbabilities, BodyGames, BodyQueues


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

@app.post("/games")

def get_games(body: BodyGames):

    results = games.get_teory(
        data  = surround_in_array(body.dict()["matrix"])
    )

    return results


@app.post("/queues")

def get_queues(body: BodyQueues):

    results = queues.get_teory(body);


    if( "error" in results):

        raise HTTPException(status_code=400, detail=results["error"])

    return results

@app.post("/queues/pn")
def get_queues(body: BodyQueuesProbabilities):

    results = queues.calculateProbabilities(body);
    if ("error" in results):
        raise HTTPException(status_code=400, detail=results["error"])
    
    return results

@app.post("/queues/economicAnalysis")

def get_economic_analysis(body: BodyEconomicAnalysis):

    results = queues.get_teory_analysis_economic(body)

    if ("error" in results):
        raise HTTPException(status_code=400, detail=results["error"])
    
    return results
