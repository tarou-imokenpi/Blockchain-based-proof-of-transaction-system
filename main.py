from BlockChain import BlockChain

diff = 5
block_chain_list = BlockChain(diff)


for i in range(1, 10):
    transaction_data = {
        "apple": 100,
        "banana": 200,
        "num": i,
    }

    block_chain_list.add_block(transaction_data)


# チェーンの確認
for i in range(1, len(block_chain_list.block_chain)):
    print(f"---------------block{i}---------------------")
    print(f"previous_hash: {block_chain_list.block_chain[i].previous_hash}")
    print(f"hash: {block_chain_list.block_chain[i].hash}")
    print(f"transaction_data: {block_chain_list.block_chain[i].transaction_data}")
    print("---------------------------------------------")
