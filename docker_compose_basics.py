from redis import Redis

cache = Redis("redis", 6379)
cache.set("example", 5)
print(int(cache.get("example")) ** 2)