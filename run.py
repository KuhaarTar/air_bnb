from app import app


@app.route('/')
def hello():
    return 'Hello, flask!'


if __name__ == '__main__':
    app.run(port=5050, debug=True)
