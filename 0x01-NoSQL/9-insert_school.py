#!/usr/bin/env python3
"""definition of insert_school"""
import pymongo


if __name__ == '__main__':
    def insert_school(mongo_collection, **kwargs):
        """inserts new document in a collection"""
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
