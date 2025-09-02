import requests


class YandexGPT:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog
        self.url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    def get_answer(self, text):
        data = {
            "modelUri": f"gpt://{self.catalog}/yandexgpt",
            "completionOptions": {
                "stream": False,
                "temperature": 0.4,
                "maxTokens": 100,
                "reasoningOptions": {
                    "mode": "DISABLED"
                }
            },
            "messages": [
                {
                    "role": "user",
                    "text": text,
                }
            ]
        }

        headers = {'Authorization': f"Api-Key {self.token}"}

        res = requests.post(self.url, json=data, headers=headers)
        return res.json()['result']['alternatives'][0]['message']['text']
