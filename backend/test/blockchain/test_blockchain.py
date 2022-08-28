import pytest
from getopt import GetoptError
from backend.blockchain.blockchain import Blockchain
from backend.util.arguments import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()
    genesisBlock = blockchain.chain[0]

    for key, value in GENESIS_DATA.items():
        assert getattr(genesisBlock, key) == value

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.addBlock(data)

    assert blockchain.chain[-1].data == data

@pytest.fixture
def blockchain_four_blocks():
    blockchain = Blockchain()
    for i in range(4):
        blockchain.addBlock(i)
    return blockchain

def test_is_valid_chain(blockchain_four_blocks):
    Blockchain.is_valid_chain(blockchain_four_blocks.chain)

def test_is_valid_chain_bad_gensis(blockchain_four_blocks):
    blockchain_four_blocks.chain[0].hash = 'evil=hash'

    with pytest.raises(Exception, match='genesis block must be valid'):
        Blockchain.is_valid_chain(blockchain_four_blocks.chain)

def test_replace_chain(blockchain_four_blocks):
    blockchain = Blockchain()
    for i in range(5):
        blockchain.addBlock(i)

    blockchain_four_blocks.replace_chain(blockchain.chain)
    assert blockchain_four_blocks.chain == blockchain.chain

def test_replace_not_longer_chain(blockchain_four_blocks):
    blockchain = Blockchain()
    for i in range(2):
        blockchain.addBlock(i)

    with pytest.raises(Exception, match='the incoming chain should be longer'):
        blockchain_four_blocks.replace_chain(blockchain.chain)
    
def test_replace_bad_chain(blockchain_four_blocks):
    blockchain = Blockchain()
    for i in range(5):
        blockchain.addBlock(i)
    blockchain.chain[3].hash = 'bad-hash'

    with pytest.raises(Exception, match='incoming chain is invalid'):
        blockchain_four_blocks.replace_chain(blockchain.chain)