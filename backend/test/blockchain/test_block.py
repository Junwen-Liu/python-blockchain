import time

from backend.blockchain.block import Block
from backend.util.arguments import GENESIS_DATA, MINE_RATE, SECOND
from backend.util.hex_to_binary import hex_to_binary

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mineBlock(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        assert getattr(genesis, key) == value 
    
def test_quickly_mined_block():
    last_block = Block.mineBlock(Block.genesis(), 'foo')
    mined_block = Block.mineBlock(last_block, 'bar')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mineBlock(Block.genesis(), 'foo')
    time.sleep(MINE_RATE/SECOND)
    mine_block = Block.mineBlock(last_block, 'bar')

    assert mine_block.difficulty == last_block.difficulty -1