import uvicorn
from fastapi import FastAPI
from routes.wxo_routes import router as agents_router

app = FastAPI(title="Watsonx Orchestrate Agent API")
app.include_router(agents_router)


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)