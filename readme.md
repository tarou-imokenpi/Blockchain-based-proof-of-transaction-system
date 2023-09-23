

# Blockchain-based-proof-of-transaction-system

## ブロックチェーンの雰囲気実装です。

# クラス図

```mermaid
classDiagram
    class Block {
        diff: int
        previous_hash: str
        transaction_data: dict
        timestamp: float
        hash: str
        __calculate_hash()
    }

    class BlockChain {
        block_chain: list
        diff: int
        __create_genesis_block()
        add_block(transaction_data: dict)
    }

    Block --> BlockChain : 1..*
    Block --> sha256 : uses
    BlockChain --> Block : contains
    BlockChain --> loguru : uses
    Block --> time : uses
}

```
