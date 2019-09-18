from web3 import Web3

ganeche_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganeche_url))
from_account = '0x3FdcD7477cf415c7bd6F90C88C412c58769cB0A0'
to_account = '0x86D144b2dd24a29350a0a268A25D6F8d0026C753'
from_private_key = 'd8356f617569db1280a51de79caabcf3b3936dcfd7e05d24fd23933cb1897b19'

# get the nonce
nonce = web3.eth.getTransactionCount(from_account)
# build taransaction
tx = {
    'nonce': nonce,
    'to': to_account,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000, # 0.2m
    'gasPrice': web3.toWei(50, 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, from_private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))