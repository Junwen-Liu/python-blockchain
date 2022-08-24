from block import Block

class Blockchain:
    """
    blockchian is a public ledger of transactions, store a list of blocks, which are sets of transactions.
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def addBlock(self, data):
        self.chain.append(Block.mineBlock(self.chain[-1], data))

    #repr method is a python buildin method to get pritnable string representation of an object.
    def __repr__(self):
        return f'Blockchain:{self.chain}'

def main():    
    blockchain = Blockchain()
    blockchain.addBlock('one')
    blockchain.addBlock('two')
    print(blockchain)
    #__name__ is a buildin method, will tell which is main if we directly call a file
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()