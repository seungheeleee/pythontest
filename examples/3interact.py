import json
from web3 import Web3
ganeche_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganeche_url))
greeter_abi = json.loads('[{"constant":false,"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
greeter_address = '0xb9BCA0a37C19Dc78C6aEd330B8023787fa53AB36'
web3.eth.defaultAccount = web3.eth.accounts[0]
address_2 = web3.eth.accounts[1]

# connect to contract
contract = web3.eth.contract(address=greeter_address, abi=greeter_abi)

print(contract.functions.greet().call())#네트워크상태변화를일으키지않음
# call contaract function
before_balance = web3.eth.getBalance(address_2)
# connect to contract
# call contaract function
# send transaction
tx_hash = contract.functions.setGreeting('hi!!1234').transact({'from': address_2, 'gasPrice': web3.toWei(22, 'gwei')})
# get receipt
receipt = web3.eth.waitForTransactionReceipt(tx_hash)
after_balance = web3.eth.getBalance(address_2)
wei_usage = before_balance - after_balance

# call contaract function
print(f'updated greeting: {contract.functions.greet().call()}')
print(f'wei usage:{wei_usage}')
print(f'gas usage:{receipt.gasUsed}')
print(f'gas price:{wei_usage / receipt.gasUsed}')