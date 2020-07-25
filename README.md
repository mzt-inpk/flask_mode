# flask_mode
使用python的flask模块，在网页上输入要处理的文本，并选择处理方式，最终将处理结果显示到另一个文本框中
## 使用方法
1.在当前目录下打开cmd，执行命令： python test_flask.py;        (或双击文件bat.bat)  
2.在浏览器输入http://127.0.0.1:5000/
## 简单移植
1.在fun.py中更改要执行的程序功能  
2.在test_flak.py与templates/login.html两个文件中修改网页显示的选项，如：将两个文件中‘fun1’改为‘长度统计’
>test_flak.py : select1 = 'fun1'  
>templates/login.html : value="fun1"
