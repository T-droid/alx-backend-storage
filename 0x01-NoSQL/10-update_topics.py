#!/usr/bin/env python3
"""definition of update_topocs"""

import pymongo


if __name__ == '__main__':
    def update_topics(mongo_collection, name, topics):
        """changes all topics of a school document based on name"""
        filter = {"name": name}
        update = {"$set": {"topics": topics}}
        mongo_collection.update_many(filter, update)
