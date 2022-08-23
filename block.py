import time

def mineBlock(last_block, data):
    """
    mine a block based on the given last_block and data
    """
    #time_ns count the nano seconds since Jan.1, 1970
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'

    return Block(timestamp, last_hash, hash, data)

def genesis():
    """
    Generate the genesis block
    """
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])

class Block:
    """
    block: a unit of storage
    stores transactions in a blockchain
    """
    def __init__(self, timestamp, last_hash, hash,data):
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash

    def __repr__(self):
        return (
            'Block'
            f'timestamp:{self.timestamp}, '
            f'last_hash:{self.last_hash}, '
            f'hash:{self.hash}, '
            f'data:{self.data}, '
        )

def main():
    genesis_block = genesis()
    block = mineBlock()

if __name__ == '__main__':
    main()