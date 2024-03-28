import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []
        jsonfied_response = json.loads(self.get_response_body())
        for response in jsonfied_response:
            data_list.append(response)
        return data_list