from web3 import Web3
infura_url="https://mainnet.infura.io/v3/4a215fad0c874dfda9181e8ba8989656"
web3=Web3(Web3.HTTPProvider(infura_url))
accountnumber=input("enter the account number: ")
print(web3.eth.get_balance(accountnumber))