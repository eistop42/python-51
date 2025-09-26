import os
import json
class TelegramDB:
    def __init__(self, filename):
        self.filename = filename

    def set_value(self, telegram_id, name, value):
        # получить текущую базу, дополнить или создать запись
        # для текущего пользователя
        data = self._get_data()
        # присваиваем значение, если пользователь
        # первый раз
        if str(telegram_id) not in data:
            data[telegram_id] = {name:value}
            self._save_data(data)
            return True
        # если пользватель есть - добавляем новый параметр
        data[str(telegram_id)][name] = value
        # перезаписываем файл
        self._save_data(data)
    def get_value(self, telegram_id, name):
        """Возвращаем значение по ключу"""
        data = self._get_data()
        telegram_id = str(telegram_id)
        if telegram_id not in data:
            return None
        if name not in data[telegram_id]:
            return None
        return data[telegram_id][name]
    def _get_data(self):
        """Получить данные из файла"""
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    def _save_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f :
            json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    db = TelegramDB('tg.json')
    db.set_value('123', 'lang', 'ru')
    print(db.get_value('123', 'lang'))
