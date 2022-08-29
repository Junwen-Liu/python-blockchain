from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def default():
    return 'Main page'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(list(map(lambda block: block.__dict__, blockchain.chain)))

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction = 'sample_transaction_data'
    blockchain.addBlock(transaction)
    return jsonify(blockchain.chain[-1].__dict__)

app.run(port=5001)