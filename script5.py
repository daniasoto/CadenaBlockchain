from blockchain import Blockchain

block_one_transactions = {"origen":"Ana", "destino": "Pepe", "cantidad":"50"}
block_two_transactions = {"origen": "juan", "destino":"Carlos", "cantidad":"25"}
block_three_transactions = {"origen":"Alicia", "destino":"Jorge", "cantidad":"35"}

fake_transactions = {"origen": "Dania", "destino":"Pepe, Alicia", "cantidad":"25"}

local_blockchain = Blockchain()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.chain[2].transactions = fake_transactions  ## a descomentar para probar si la cadena se invalida al modificarla
local_blockchain.print_blocks()
local_blockchain.validate_chain()

