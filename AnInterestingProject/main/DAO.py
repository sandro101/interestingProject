import json
import os


def get_data_location():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/mockData.json")
    return path


def read_data(identifier):
    with open(get_data_location()) as mockData:
        data = json.load(mockData)
        return list(filter(lambda item: item['id'] == identifier, data))


def append_id(data, item):
    item['id'] = len(data) + 1
    return item


def write_data(item):
    with open(get_data_location()) as mockDataRead:
        data = json.load(mockDataRead)
        item = append_id(data, item)
        data.insert(item['id'], item)
    with open(get_data_location(), 'w') as mockDataWrite:
        mockDataWrite.write(json.dumps(data))
