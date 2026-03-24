from fastapi import FastAPI
import routes as rt

app = FastAPI()
app.include_router(rt.router)
