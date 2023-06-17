import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

adress = Web3.to_checksum_address('0x633D6bE2a27Ec2db024A88eb985fA5Bfe599FAEe')
abi = json.loads(
    '[{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"}]')

contract = web3.eth.contract(address=adress, abi=abi)
print(contract.functions.get().call())
