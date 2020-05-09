from flask import Flask,escape,url_for
app=Flask(__name__)

@app.route('/')      #所谓注册，就是给视图函数戴上一个装饰器帽子
@app.route('/home')  #装饰器的参数-URL规则
@app.route('/index')

def hello():
    return '<h1>hello teemo!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % escape(name)    #用户的输入可能包含恶意代码，所以使用escape()函数对name变量进行转义处理

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='teemo'))  # 输出：/user/greyli
    print(url_for('user_page', name='python'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'