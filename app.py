from flask import Flask, render_template, send_from_directory

import os
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


# 定义首页路由
@app.route('/')
def home():
    return render_template('home.html')

# 定义体适能标准相关的路由
@app.route('/situp_rule')
def situp_rule():
    return render_template('situp_rule.html')

@app.route('/reversecrunch_rule')
def reversecrunch_rule():
    return render_template('reversecrunch_rule.html')

@app.route('/jump_rule')
def jump_rule():
    return render_template('jump_rule.html')

@app.route('/sit_rule')
def sit_rule():
    return render_template('sit_rule.html')

@app.route('/knees_rule')
def knees_rule():
    return render_template('knees_rule.html')

@app.route('/run_rule')
def run_rule():
    return render_template('run_rule.html')

# 定义其他路由
@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/situp')
def situp():
    return render_template('situp.html')

@app.route('/reversecrunch')
def reversecrunch():
    return render_template('reversecrunch.html')

@app.route('/jump')
def jump():
    return render_template('jump.html')

@app.route('/sit')
def sit():
    return render_template('sit.html')

@app.route('/knees')
def knees():
    return render_template('knees.html')

@app.route('/run')
def run():
    return render_template('run.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/save_record')
def save_record():
    return render_template('save_record.html')


if __name__ == '__main__':
    app.run(debug=True)
