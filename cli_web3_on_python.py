import json
from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/4a215fad0c874dfda9181e8ba8989656"
web3 = Web3(Web3.HTTPProvider(infura_url))

option= input ("what do you waant to do :\n 1) cretate account \n")

if option=='yes' or 'Yes':
    account=web3.eth.account.create()
    print('account created')

option=input('1 -> do you to get the account adress ??\n 2 -> do you want to get the private key ??\n')

if option== '1':
    print(account.address)

if option=='2':
    print(account.privateKey)