from fastapi import Depends
from redis import Redis

redis_client = Redis(host='localhost', port=6379)

async def get_redis() -> Redis:
    return redis_client