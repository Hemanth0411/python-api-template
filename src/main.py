from fastapi import FastAPI

app = FastAPI(
    title="Python API Template",
    description="A professional, modern template for building robust Python REST APIs.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    """A simple health check endpoint."""
    return {"status": "ok", "message": "Welcome to the Python API Template!"}