from fastapi_simple_security import api_key_router, api_key_security
from typing import Optional

from fastapi import Depends, FastAPI, Query
from app.routers import overlap_indicators
from app.models import items
from app.i18n import overlap_docs

app = FastAPI(openapi_tags=overlap_docs.tags_metadata)

app.include_router(api_key_router, prefix="/auth", tags=["_auth"])
app.include_router(overlap_indicators.router, prefix="/indicators")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", tags=["items"], response_description=overlap_docs.tag_items[1]["get_response_description"], summary=overlap_docs.tag_items[0]["summary"], response_model=items.Item)
def read_item(item_id: int, q: Optional[str] = Query(None, description=overlap_docs.tag_items[1]["q"])):
    return {"item_id": item_id, "q": q}


@app.post("/items/", tags=["items"])
async def create_item(item: items.Item):
    return item


@app.get("/secure", dependencies=[Depends(api_key_security)])
def read_secure():
    return {"Status": "Success"}
