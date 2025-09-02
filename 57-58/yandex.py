import requests

token = ''
catalog = ''
url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

def get_answer(text):
    data = {
        "modelUri": f"gpt://{catalog}/yandexgpt",
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
            },
            {
                "role": "user",
                "text": 'переведи на английский',
            }
        ]
    }

    headers = {'Authorization': f"Api-Key {token}"}

    res = requests.post(url, json=data, headers=headers)
    return res.json()['result']['alternatives'][0]['message']['text']


while True:
    user = input('Введи вопрос: ')
    print(get_answer(user))