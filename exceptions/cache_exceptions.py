class RedisError(Exception):
    """Base class for Redis-related errors"""
    pass


class RedisConnectionError(RedisError):
    """Raised when we fail to connect to a Redis instance"""
    pass


class KeyNotFoundError(RedisError):
    """Raised when a requested key is not found"""
    pass


class KeyExistsError(RedisError):
    """Raised when a key already exists"""
    pass


class ValueError(RedisError):
    """Raised when a value is not valid"""
    pass


class RedisConnectionError(RedisError):
    """Raised when a Redis connection cannot be established"""
    pass


class RedisAuthenticationError(RedisError):
    """Raised when authentication to Redis fails"""
    pass