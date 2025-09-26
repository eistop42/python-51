from argparse import ArgumentParser

from speechkit import model_repository, configure_credentials, creds
from creds import YANDEX_TOKEN

# Authentication with an API key.
configure_credentials(
   yandex_credentials=creds.YandexCredentials(
      api_key=YANDEX_TOKEN
   )
)

def synthesize(text):
   model = model_repository.synthesis_model()

   # Specify the synthesis settings.
   model.voice = 'jane'
   model.role = 'good'

   # Performing speech synthesis and creating the output audio file.
   result = model.synthesize(text, raw_format=True)

   return result
   # result.export(export_path, 'wav')

if __name__ == '__main__':
   text = 'привет как дела'
   file = 'test.wav'

   synthesize(text)