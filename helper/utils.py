import json
import os
import configparser


class DataForTest:

    def __init__(self):
        self.file = os.path.abspath(".\\helper\\test_data.json")

    def get(self, *keys):
        f = open(self.file, "r")
        content_json = json.load(f)
        f.close()
        result = []
        for key in keys:
            result.append(content_json[key])

        return result

    def update(self, key_value_pairs):
        f = open(self.file, "r")
        content_json = json.load(f)
        for key, value in key_value_pairs.items():
            content_json[key] = value

        f = open(self.file, "w")
        json.dump(content_json, f, indent=4)


class ConfigProperties:

    def __init__(self):
        self.file = os.path.abspath(".\\config\\config.properties")

    def get(self, section, option):

        config = configparser.RawConfigParser()
        config.read(self.file)
        return config.get(section, option)
