from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

# for 遍历字典
# @app.route("/")
# def index():
#     # zi'dian'bian'li
#     user = {
#                 'username' : 'ljk',
#                 'age' : 11
#     }
#     websites = ['baidu.com','google.com']
#     return render_template('index2.html', user=user, websites=websites)

# for 遍历列表
# @app.route("/")
# def index():
#     books = [
#         {
#             'name' : '西游记',
#             'author' : '吴承恩',
#             'price': 109
#          },
#         {
#             'name': '红楼梦',
#             'author': '曹雪芹',
#             'price': 200
#         },
#         {
#             'name': '三国演义',
#             'author': '罗贯中',
#             'price': 120
#         },
#         {
#             'name': '水浒传',
#             'author': '施耐庵',
#             'price': 1230
#         },
#     ]
#     return render_template('index2.html', books=books)


if __name__ == '__main__':
    app.run()