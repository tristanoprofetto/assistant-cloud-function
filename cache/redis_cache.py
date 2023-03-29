import os
import logging
import redis


class RedisCache:
    """
    A class representing a Redis instance. Provides methods for adding,
    updating, deleting, listing, and flushing keys in the cache.
    """
    def __init__(self, redis_endpoint: str, db=0):
        """
        Initializes a new Redis instance with the specified host, port, and database.
        """
        host, port = redis_endpoint.split(':')
        self.cache_db = redis.StrictRedis(host=host, port=int(port))
        try:
            self.cache_db.ping()
        except Exception as e:
            logging.info(e)

    
    def check_key(self, key):
        """
        Verifies if a key exist in the Redis cache.
        
        Returns:
            1 (int): if key exists
            0 (int): if key does NOT exist
        """
        try:
            value = self.cache_db.exists(key)
            return value
        except Exception as e:
            logging.info(e)


    def get_key(self, key):
        """
        Retrieves a Value given a Key, and returns the value if it exists
        """
        try:
            if self.cache_db.exists(key):
                value = self.cache_db.mget(key)
                return value
            
            else:
                logging.info(f'Error: Key {key} does not exist.')

        except Exception as e:
            logging.info(e)
        

    def add_key(self, key, value):
        """
        Adds a new key-value pair to the Redis cache.
        """
        try:
            self.cache_db.mset(key, value)

        except Exception as e:
            logging.info(f'Error: Key {key} could not be added to the Cache')


    def update_key(self, key, value):
        """
        Updates an existing key's value in the Redis cache.
        """
        try:
            if self.cache_db.exists(key):
                self.cache_db.mset(key, value)
            else:
                logging.info(f'Error: Key {key}, does not exist in the Cache')
        
        except Exception as e:
            logging.info(e)

    
    def delete_key(self, key):
        """
        Deletes a key-value pair from the Redis cache.
        """
        try:
            if self.cache_db.exists(key):
                self.cache_db.delete(key)
            else:
                logging.info(f'Error: Key {key} does not exist in the Cache, therefore cannot be deleted.')

        except Exception as e:
            logging.info(e)

    
    def flush_cache(self):
        """
        Flushes all keys from the Redis cache.
        """
        try:
            self.cache_db.flushall()
            logging.info('Successfully flushed all keys from the Cache.')

        except Exception as e:
            logging.info(e)

