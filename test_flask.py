from flask import Flask,request,render_template
from wsgiref.simple_server import make_server
import fun
select1 = 'fun1'  # 此处应与login.html中的option value="fun1"的fun1对应
select2 = 'fun2'  # 同上
# 可添加select3、4 等多个选项


# 根据web选项执行对应操作
def fun_select( select = select1):
    if select == select1:
        return fun.fun1()
    if select == select2:
        return fun.fun2()
    else:
        return "err:前后端标签不匹配"


# flask框架
app  =  Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def login(show='', src='请输入文本...'):

    if request.method == 'POST':
        src = request.form['src']  # 待处理文本；获取在login.html中输入的文本
        select = request.form['sentSelect']  # 处理方式；获取在login.html中选择的处理方式
        if len(src) != 0:
            show = fun_select(select)  # 根据选项执行对应操作
        else:
            return '请输入内容!'
    # 输入内容保留到输入的文本框中，返回的结果显示到另一个文本框中
    # src对应.html中的{{src}} ,result对应.html中的{{result}}
    return render_template('login.html', src=src, result=show)


if __name__ == "__main__":
    print('\n\n请在浏览器输入地址:http://127.0.0.1:5000/，以进行相关操作\n\n')
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run('127.0.0.1', 5000)


