from backend.util.crypto_hash import crypto_hash

HEX_TO_BINARY_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex_string):
    binary_string = ''
    for c in hex_string:
        binary_string += HEX_TO_BINARY_TABLE[c]

    return binary_string

def main():
    number = 351
    hex_number = hex(number)[2:]
    print(f'the original number is {number} and hex number is {hex_number}')

    binary_str = hex_to_binary(hex_number)
    int_number = int(binary_str, 2)
    print(f'new number is {int_number}')

    hex_to_binary_cryptoHash = hex_to_binary(crypto_hash('test-data'))
    print(f'hex_to_binary_cryptoHash:{hex_to_binary_cryptoHash}')

if __name__ == '__main__':
    main()

