from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Automatic Sending'

@app.route('/contact/url', methods=['POST'])
def contact_url():
    return request.get_data()

@app.route('/contact/html', methods=['POST'])
def contact_html():
    return request.get_data()

@app.route('/contact/tag', methods=['POST'])
def contact_tag():
    return request.get_data()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
