# python 3.9.0
# web3py 5.19.0 - https://github.com/ethereum/web3.py
# This script is sample of how to get deterministic address of a contract based on nonce 
# adapted/modified from https://ethereum.stackexchange.com/a/63235

import rlp
from web3 import Web3

base_address = "0x6490fCb4C402dAEa0C80Feee0f6E0DCD58F2b584"
nonce = 0

def get_contract_address(sender: str, nonce: int) -> str:
    sender_bytes = Web3.toBytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    hash = Web3.keccak(raw)
    address_bytes = hash[12:]
    return Web3.toChecksumAddress(address_bytes)

print(f'Address: {base_address} with nonce: {nonce} will deploy contract at:\n {get_contract_address(base_address, nonce)}')

# known good values you can check against 
# assert get_contract_address(Web3.toChecksumAddress("0x6ac7ea33f8831ea9dcc53393aaa88b25a785dbf0"), 1) == Web3.toChecksumAddress("0x343c43a37d37dff08ae8c4a11544c718abb4fcf8")