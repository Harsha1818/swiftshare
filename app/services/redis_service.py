import aioredis

class RedisService:
    def __init__(self, redis_url):
        self.redis = aioredis.from_url(redis_url, decode_responses=True)

    async def set_cache(self, key, value, expire=3600):
        await self.redis.set(key, value, ex=expire)

    async def get_cache(self, key):
        return await self.redis.get(key)

# Usage:
# redis_service = RedisService(redis_url="redis://localhost:6379")
# await redis_service.set_cache("key", "value")
