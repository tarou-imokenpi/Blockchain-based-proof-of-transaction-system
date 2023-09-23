from block import Block
from loguru import logger


class BlockChain:
    def __init__(self, diff: int) -> None:
        self.block_chain: list = []
        self.diff: int = diff
        self.__create_genesis_block()

    def __create_genesis_block(self) -> None:
        block = Block(
            diff=self.diff,
            previous_hash=0,
            transaction_data={"message": "Genesis Block"},
        )
        self.block_chain.append(block)
        logger.debug("create genesis block")

    def add_block(self, transaction_data: dict) -> list:
        try:
            block = Block(
                diff=self.diff,
                previous_hash=self.block_chain[-1].hash,
                transaction_data=transaction_data,
            )
            self.block_chain.append(block)
            
            return self.block_chain
        except IndexError:
            logger.error("previous_hashのindexの値が見つかりません")
