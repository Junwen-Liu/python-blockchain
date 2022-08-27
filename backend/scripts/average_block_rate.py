import time
from backend.blockchain.blockchain import Blockchain
from backend.util.arguments import SECOND

blockchain = Blockchain()

times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.addBlock(i)
    end_time = time.time_ns()
    mined_time = (end_time - start_time)/SECOND
    times.append(mined_time)

    average_time = sum(times)/len(times)
    print(f"new block difficulty: {blockchain.chain[-1].difficulty}")
    print(f"time to mine new block: {mined_time}")
    print(f"the average time of mining block is {average_time}s\n")
