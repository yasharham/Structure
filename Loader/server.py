from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from Utils.V1.config_reader import configure
from API.Router.V1 import example


def app():
    app = FastAPI()

    app.openapi_schema = configure.get("SWAGGER","DOCS")

    app.add_middleware(SessionMiddleware, secret_key=configure.get("AUTHENTICATION","MIDDLEWARE_KEY"))
    origins =["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(example.router)

    return app







