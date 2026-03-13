from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return ("Hi")

@app.get("/health")

@app.get("/quote")

@app.get("/history")
