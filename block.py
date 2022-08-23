class Block:
    """
    block: a unit of storage
    stores transactions in a blockchain
    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block:{self.data}'

def main():
    block = Block('foo')
    print(block)
    print(f'block.py __name__: {__name__}')

if __name__ == '__main__':
    main()