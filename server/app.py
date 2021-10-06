from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World!'

@app.route('/user', methods=['POST'])
def user_data():
    return request.form['query']

@app.route('/company', methods=['POST'])
def company_data():
    return request.form['query']

@app.route('/result')
def result():
    return request.args.get('id')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)