from difflib import diff_bytes
import time
from tkinter import EXCEPTION
from backend.util.crypto_hash import crypto_hash
from backend.util.arguments import GENESIS_DATA,MINE_RATE
from backend.util.hex_to_binary import hex_to_binary


class Block:
    """
    block: a unit of storage
    stores transactions in a blockchain
    """
    def __init__(self, timestamp, last_hash, hash,data, difficulty, nounce):
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.difficulty = difficulty
        self.nounce = nounce

    def __repr__(self):
        return (
            'Block'
            f'timestamp:{self.timestamp}, '
            f'last_hash:{self.last_hash}, '
            f'hash:{self.hash}, '
            f'data:{self.data}, '
            f'difficulty:{self.difficulty}, '
            f'nounce:{self.nounce}'
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def mineBlock(last_block, data):
        #mine a block based on the given last_block and data, until a block hash has been found
        #time_ns count the nano seconds since Jan.1, 1970
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjustDifficulty(last_block, timestamp)
        nounce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nounce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nounce = nounce + 1
            timestamp = time.time_ns()
            difficulty = Block.adjustDifficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nounce) 

        return Block(timestamp, last_hash, hash, data, difficulty, nounce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjustDifficulty(last_block, new_timestamp):
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        
        return (last_block.difficulty - 1) if (last_block.difficulty - 1) >= 1 else 1

    @staticmethod
    def is_valid_block(last_block, block):
        """
        validate block by enforcing the following rules:
          -the block must have the proper last_hash reference
          -the block must meet the proof of work requirement
          -the difficulty must only adjust by 1
          -the block hash must be a valid combiantion of the block fields
        """
        if block.last_hash != last_block.hash:
            raise Exception('The block last_hash must be correct')

        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of requirement was not met')
        
        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception('The block difficulty must only adjust by 1')

        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nounce,
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception('The block hash must be correct')

def main():
    genesis_block = Block.genesis()
    bad_block = Block.mineBlock(genesis_block, 'ffo')
    bad_block.last_hash = 'evil-data'
    try:
        Block.is_valid_block(genesis_block, bad_block)
    except Exception as e:
        print(f'is_valid_block: {e}')

    

if __name__ == '__main__':
    main()