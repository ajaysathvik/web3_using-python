import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/4a215fad0c874dfda9181e8ba8989656"
web3 = Web3(Web3.HTTPProvider(infura_url))

latest=web3.eth.block_number

print(web3.eth.get_block(latest))

hash='0xfb967fe6bda505c6141cfca88434133373591383d1136dc7bc0d4dd06b140750'
print(web3.eth.get_transaction_by_block(hash,2))