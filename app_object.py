from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
    return render_template('index8.html')

@app.route('/login5/', methods=['GET', 'POST'])
def login5():
    if request.method == 'GET':
        return render_template('login5.html')
    else:
        pass

if __name__ == '__main__':
    app.run()