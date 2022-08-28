from backend.blockchain.block import Block
from backend.test.blockchain.test_block import last_block

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

    def replace_chain(self, chain):
        """
        replace the local chain with incoming one is folloiwng applies:
            -the incoming chain is longer than the local
            -the incoming chain is format properly
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace, the incoming chain should be longer')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace, the incoming chain is invalid: {e}')

        self.chain = chain

    @staticmethod
    def is_valid_chain(chain):
        """
        validate the incoming chain.
        enforce the following rules of the blockchain:
            -the chain must start with genesis block
            -blocks must be formated correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('the genesis block must be valid')

        for  i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)

def main():    
    blockchain = Blockchain()
    blockchain.addBlock('one')
    blockchain.addBlock('two')
    print(blockchain)
    #__name__ is a buildin method, will tell which is main if we directly call a file
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()