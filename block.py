from hashlib import sha256
from loguru import logger
import time


class Block:
    """初期化

    diff: 難易度の調整\n
    previous_hash: 前のブロックのハッシュ値\n
    transaction_data: 登録したい取引データの辞書\n
    """

    def __init__(self, diff: int, previous_hash: str, transaction_data: dict) -> None:
        self.diff: int = int(diff)
        self.previous_hash: str = str(previous_hash)
        self.transaction_data: dict = transaction_data
        self.timestamp: float = time.time()
        self.hash: str = self.calculate_hash()

    def calculate_hash(self) -> str:
        nonce: int = 0
        block_hash: str = ""
        logger.debug("マイニング開始")
        while True:
            block_data = {
                "transaction_data": self.transaction_data,
                "previous_hash": self.previous_hash,
                "timestamp": self.timestamp,
                "nonce": nonce,
            }
            block_hash: str = sha256(str(block_data).encode()).hexdigest()
            nonce += 1
            if nonce % 10000 == 0:
                logger.debug(f"seaching: {nonce}...")

            if block_hash[0 : self.diff] == "0" * self.diff:
                logger.debug(
                    f"マイニング完了！！\nprevious_hash: {self.previous_hash}\nnonce: {nonce}\nhash: {block_hash}\ntimestamp: {self.timestamp}"
                )
                return block_hash
