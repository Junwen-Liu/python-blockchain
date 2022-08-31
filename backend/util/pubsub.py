import redis
from backend.util.arguments import CHANNELS

class PubSub:
    def __init__(self):
        self.client = redis.Redis(host="123.60.55.61", port=6379,decode_responses=True)
        
    def publish(self, env, data):
        self.client.publish(env, data)

    def subscribe(self, env):
        p = self.client.pubsub()
        p.subscribe(env)


def main():
    #r = redis.Redis(host="123.60.55.61", port=6379,decode_responses=True)
    #r.set("name","slkdfjafds")
    #r.flushall()
    #r.delete('name')
    #print(r.get("name"))

    p = PubSub()
    p.subscribe(CHANNELS['TEST'])
    p.publish(CHANNELS['TEST'], 'this is something great')


if __name__ == '__main__':
    main()