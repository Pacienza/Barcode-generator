from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
