from fastapi import APIRouter

rt = APIRouter()


@rt.get("/list")
def list_connectors():
    return [{"id": "idsa"}, {"id": "idsb"}]


@rt.get("/{connector_id}")
def get_connector(connector_id: int):
    return {"id": "idsa"}
