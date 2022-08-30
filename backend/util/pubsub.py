import redis

def main():
    r = redis.Redis(host="123.60.55.61", port=6379,decode_responses=True)
    #r.set("name","slkdfjafds")
    #r.flushall()
    r.delete('name')
    print(r.get("name"))

if __name__ == '__main__':
    main()