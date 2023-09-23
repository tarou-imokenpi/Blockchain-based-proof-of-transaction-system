from block_chain import BlockChain

diff = 4
block_chain_list = BlockChain(diff)


data = {
    "apple": 100,
    "banana": 200,
}

block_chain_list.add_block(data)


# 購入の確認
for i in range(len(block_chain_list.block_chain)):
    print("-------------------------------------")
    print(block_chain_list.block_chain[i].previous_hash)
    print(block_chain_list.block_chain[i].hash)
    print(block_chain_list.block_chain[i].transaction_data)
    print("-------------------------------------")
