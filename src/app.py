import logging
from fastapi import FastAPI

from src.core.utils.xmlutils import XmlUtils
from src.services.mongoclient import DbClient


log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI()
    # application.include_router(
        
    # )
    
    return application


app = create_application()

@app.get("/db")
async def db():
    db = DbClient()
    return f"{db.connect().server_info()}"

@app.get("/")
async def root():
    values = XmlUtils.load_file("./resources/xml/PrixCarburants_annuel_2021.xml")
    return values[0]


#
# Action on event, here start and stop predefined
# For now, this event just log start and stop app
#
# Action on start API
@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


# Action on stop API
@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
