import hashlib
import json

def crypto_hash(*args):
    """
    return the sha-256 hash of the given list of arguments    """
    #encode method only works with string, so we have to convert our data to string first, here we can use the json.dumps to turn this to string
    stringified_args = sorted(map(lambda data: json.dumps(data),args))
    #print(f'stringify args: {stringified_args}')

    jointed_data = ''.join(stringified_args)
    #print(jointed_data)
    #encoding is the process of converting data into an alternate representation
    return hashlib.sha256(jointed_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash(): {crypto_hash('one', 2, [4])}")
    print(f"crypto_hash(): {crypto_hash('one',  [4],2)}")

if __name__ == '__main__':
    main()