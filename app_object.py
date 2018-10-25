from flask import Flask, render_template, request, redirect, url_for, session
from app_object_models import User, Question
from app_object_exts import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

# 主页
@app.route('/')
def index8():
    context = {
        # 时间排序由小到大加 " - "
        'questions' : Question.query.order_by('-create_time').all()
    }
    return render_template('index8.html', **context)

# 登陆
@app.route('/login5/', methods=['GET', 'POST'])
def login5():
    if request.method == 'GET':
        return render_template('login5.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password==password).first()
        if user:
            session['user_id'] = user.id
            if request.form.get('checkbox'):
                session.permanent = True
            return redirect(url_for('index8'))
        else:
            return '错误'

# 注册
@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')

        # 验证账号是否被注册
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '已被注册'
        else:
            if password != confirmpassword:
                print('两次输入不一致')
            else:
                user = User(telephone=telephone, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login5'))

# 注销
@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login5'))

# 发布问答
@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template("question.html")
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index8'))

# 查看问答详情
@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)

# 利用钩子函数判断登陆状态
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user' : user }
    else:
        return {}


if __name__ == '__main__':
    app.run()