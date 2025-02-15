from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Файл для хранения баланса
DATA_FILE = 'balances.json'

# Загрузка данных из файла
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Сохранение данных в файл
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Получение баланса пользователя
@app.route('/get-balance', methods=['GET'])
def get_balance():
    user_id = request.args.get('user_id')
    data = load_data()
    balance = data.get(user_id, 0)
    return jsonify({'balance': balance})

# Увеличение баланса пользователя
@app.route('/increase-balance', methods=['POST'])
def increase_balance():
    user_id = request.json.get('user_id')
    data = load_data()
    data[user_id] = data.get(user_id, 0) + 1
    save_data(data)
    return jsonify({'balance': data[user_id]})

if __name__ == '__main__':
    app.run(debug=True)