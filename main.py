from fastapi import FastAPI
import socket

app = FastAPI()

CONTAINER_ID = socket.gethostname()

@app.get("/")
def root():
    return {
        "api": "default",
        "served_by": CONTAINER_ID
    }

@app.get("/api1")
def api1():
    return {
        "api": "api1",
        "served_by": CONTAINER_ID
    }

@app.get("/api2")
def api2():
    return {
        "api": "api2",
        "served_by": CONTAINER_ID
    }