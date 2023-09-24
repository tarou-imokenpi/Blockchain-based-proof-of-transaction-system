from block import Block
from loguru import logger


class BlockChain:
    def __init__(self, diff: int) -> None:
        """init

        Parameters
        ----------
        diff : int
            ブロックチェーンの難易度
        """
        self.block_chain: list = []
        self.diff: int = diff
        self.__create_genesis_block()
        self.update_info()

    def __create_genesis_block(self) -> None:
        """genesis blockを作成します"""
        block = Block(
            diff=self.diff,
            previous_hash=0,
            transaction_data={"message": "Genesis Block"},
        )
        self.block_chain.append(block)
        logger.debug("create genesis block")

    def update_info(self) -> dict:
        """ブロックチェーン情報を更新

        Returns
        -------
        dict
            ブロックチェーン情報
        """
        BlockChain_info = dict()
        block_chain_length: int = len(self.block_chain)

        for i in range(0, block_chain_length):
            previous_hash = self.block_chain[i].previous_hash
            hash = self.block_chain[i].hash
            transaction_data = self.block_chain[i].transaction_data
            timestamp = self.block_chain[i].timestamp

            BlockChain_info[f"block {i}"] = {
                "previous_hash": previous_hash,
                "hash": hash,
                "timestamp": timestamp,
                "transaction_data": transaction_data,
            }
        result = {
            "message": "welcom BlockChain api",
            "latest BlockChain length": block_chain_length,
            "The latest BlockChain": BlockChain_info,
        }
        logger.debug("Update info")
        self.info = result
        return result

    def add_block(self, transaction_data: dict) -> dict:
        """ブロックチェーンにブロックを追加

        Parameters
        ----------
        transaction_data : dict
            取引データ

        Returns
        -------
        dict
            結果のmessage dict
        """
        try:
            block = Block(
                diff=self.diff,
                previous_hash=self.block_chain[-1].hash,
                transaction_data=transaction_data,
            )
            self.block_chain.append(block)
            self.update_info()
            return {"message": "Successfully added blockchain"}
        except IndexError:
            logger.error("previous_hashのindexの値が見つかりません")
            return {"message": "request error"}
