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