import json
from web3 import Web3

ganache_url="HTTP://127.0.0.1:7545"

web3=Web3(Web3.HTTPProvider(ganache_url))

accont1=input("enter the account number: ")
accont2="0x9f93232Ce9B8c68547B92F15d166b1bfaBbc4241"
mon =int(input("enter the money to send; "))
private_key=input("enter the private key of the account number: ")

# nonce(prevent two same transaction)
nonce=web3.eth.get_transaction_count(accont1)

# build a transaction
ts={
    'nonce':nonce,
    'to': accont2,
    'value': web3.to_wei(mon,'ether'),
    'gas': 2000000,
    'gasPrice':web3.to_wei('50','gwei'),
}

# sign transaction
signed_tx=web3.eth.account.sign_transaction(ts,private_key)

#send transaction
tx_hash=web3.eth.send_raw_transaction(signed_tx.rawTransaction)

#get transaction hash
print(tx_hash)