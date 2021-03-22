######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file
import sys

from werkzeug.serving import make_server

app = Flask(__name__)
@app.route('/bank')
def bank():
    #题库界面
    return send_file('templates/bank.html')
@app.route('/quiz_info')
def quiz_info():
    #考试信息页
    return send_file('templates/quiz_info.html')

@app.route('/<quiz_id>/<page_index>/quiz')
def quiz(quiz_id,page_index):
    #考试界面
    return send_file('templates/quiz.html')

@app.route('/<u_id>/<quiz_id>/score')
    #交卷页面
def score(u_id,quiz_id):
    return send_file('templates/score.html')





if __name__ == '__main__':
    app.run(debug=True)
