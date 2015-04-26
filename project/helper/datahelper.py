__author__ = 'Raghav'

from project.data import data
from flask import jsonify

class Datahelper:
    def __init__(self):
        pass
    @staticmethod
    def get_data(id):
        data_id = str(id)
        return jsonify(data.record["data"][data_id])

    @staticmethod
    def update_data(id, json_data):
        for i in json_data.keys():
            if i not in data.record['data'][str(id)].keys():
                print i + "not defined in schema"
                return 0

            else:
                data.record['data'][str(id)][i] = json_data[i]
                return 1

    @staticmethod
    def delete_data(id):
        if str(id) not in data.record["data"].keys():
            print "data id is not valid"
            return 0
        else:
            del data.record["data"][str(id)]
            return 1

