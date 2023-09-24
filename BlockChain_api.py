from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from block_chain import BlockChain

diff = 4
block_chain_list = BlockChain(diff)

app = FastAPI()


class Transaction(BaseModel):
    store_name: str
    items: dict


@app.get("/")
async def root():
    latest_blockchain_info = dict()
    block_chain_length: int = len(block_chain_list.block_chain)

    for i in range(0, block_chain_length):
        previous_hash = block_chain_list.block_chain[i].previous_hash
        hash = block_chain_list.block_chain[i].hash
        transaction_data = block_chain_list.block_chain[i].transaction_data
        timestamp = block_chain_list.block_chain[i].timestamp

        latest_blockchain_info[f"block {i}"] = {
            "previous_hash": previous_hash,
            "hash": hash,
            "timestamp": timestamp,
            "transaction_data": transaction_data,
        }
    result = {
        "message": "welcom block chain api",
        "latest_blockchain_length": block_chain_length,
        "The latest blockchain": latest_blockchain_info,
    }
    return result


@app.post("/add_block/")
async def add_block(transaction_data: Transaction):
    block_chain_list.add_block(transaction_data)
    return "OK"


if __name__ == "__main__":
    uvicorn.run("BlockChain_api:app", port=8000, log_level="info")
