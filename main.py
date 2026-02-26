from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

nomi = []
Class Nome(BaseModel):
    nome: str

@app.post("/nome")
def post_nome(nomeReq: NomePostRequest):
            nomi.append(nomeReq.nome)

@app.get("/nome")
def get_nome():
       return nomi

@app.get("/")
def saluta():
    return {"text":"plug è tutto in apta"}
