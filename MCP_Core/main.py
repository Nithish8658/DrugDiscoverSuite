from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp_router import run_pipeline   # Import the correct function

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/run_mcp_pipeline")
def run_mcp_pipeline(disease: str):
    return run_pipeline(disease)
