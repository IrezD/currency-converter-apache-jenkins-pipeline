import requests

url = requests.get('https://v6.exchangerate-api.com/v6/c6eafa5bf6a022784e6fdf57/pair/USD/PLN')

response = url.status_code
data = url.json()['conversion_rate'] * 100

print(data)

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello world"

# if __name__ == "__main__":
#     app.run(debug=True)
