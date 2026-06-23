from redis import Redis
from time import time

class RateLimiter:
    def __init__(self, redis: Redis, rate: int, per: int):
        self.redis = redis
        self.rate = rate  # Max requests
        self.per = per    # Time window (seconds)

    async def is_allowed(self, key: str) -> bool:
        now = time()
        bucket_key = f'rate_limit:{key}'
        tokens = await self.redis.get(bucket_key)
        if tokens is None:
            await self.redis.set(bucket_key, self.rate - 1, ex=self.per)
            return True
        elif int(tokens) > 0:
            await self.redis.decr(bucket_key)
            return True
        return False