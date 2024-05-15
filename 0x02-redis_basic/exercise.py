#!/usr/bin/env python3
"""
Main file that imports
redis and uuid modules
"""
import redis
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """
        Store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
