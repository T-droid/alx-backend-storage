#!/usr/bin/env python3
"""definition of of function list_all"""
import pymongo


if __name__ == '__main__':
    def list_all(mongo_collection):
        """"lists all documents in a collection"""
        documents = mongo_collection.find()
        return documents
