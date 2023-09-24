from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from BlockChain import BlockChain

diff = 4
block_chain = BlockChain(diff)

app = FastAPI()


class Transaction(BaseModel):
    store_name: str
    items: dict


@app.get("/info")
async def root():
    return block_chain.info


@app.post("/add_block/")
async def add_block(transaction_data: Transaction):
    block_chain.add_block(transaction_data)
    return "OK"


if __name__ == "__main__":
    uvicorn.run("BlockChain_api:app", port=8000, log_level="info")
