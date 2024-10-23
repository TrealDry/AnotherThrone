import json


class Config:
    def __init__(self):
        self.config: dict = {}

    def __getitem__(self, item):
        return self.config[item]

    def load_config_from_json(self):
        with open("config.json", "r") as file:
            self.config = json.load(file)
