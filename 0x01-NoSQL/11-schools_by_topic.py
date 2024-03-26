#!/usr/bin/env python3
"""definition of schools_by_topic"""
import pymongo


if __name__ == '__main__':
    def schools_by_topic(mongo_collection, topic):
        """returns a list of schools having a specific topic"""
        filter = {"topics": topic}
        results = mongo_collection.find(filter)
        return results
