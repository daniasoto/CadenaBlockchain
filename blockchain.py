from block import Block

class Blockchain:

  dificultad = 2
  def __init__(self):
    self.chain = []
    self.genesis_block()

  def genesis_block(self):
    transactions = []
    genesis_block = Block(transactions, "0")
    genesis_block.generate_hash()
    self.chain.append(genesis_block)
  

  def add_block(self, transactions):
    previous_hash = (self.chain[len(self.chain)-1]).generate_hash()
    new_block = Block(transactions, previous_hash)
    
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.previous_hash != previous.generate_hash()):
        print("Se ha modificado el bloque ",i-1," porque el hash generado de ese bloque no concuerda con el almacenado en la cabecera del bloque ",i,".")
        return False
    return True
  
  def proof_of_work(self,block):
    
    proof = block.generate_hash()
    while not proof.startswith('0' * Blockchain.dificultad):
      block.nonce += 1
      proof = block.generate_hash()
    return proof
