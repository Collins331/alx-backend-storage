#!/usr/bin/env python3
"""
Main file that imports
redis and uuid modules
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Constructor that initializes
        the redis instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method that takes
        data and returns a key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """
        Get method that takes a key
        and an optional Callable function
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get method that takes a key
        and returns a string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Get method that takes a key
        and returns an integer
        """
        return self.get(key, int)
