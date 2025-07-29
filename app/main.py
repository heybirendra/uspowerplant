from fastapi import FastAPI
from app.api import router as api_router
from app.pretty.PrettyJson import PrettyJson
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(default_response_class=PrettyJson)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
