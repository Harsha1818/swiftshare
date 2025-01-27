from fastapi import FastAPI
from app.api import file_routes, auth_routes

app = FastAPI()

# Include API routers
app.include_router(file_routes.router, prefix="/files", tags=["Files"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SwiftShare!"}
