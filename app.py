from flask import Flask

# Создаем приложение Flask
app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return "Сайт работает! 🚀"

# Проверка, что запускается только локально, а не на Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
