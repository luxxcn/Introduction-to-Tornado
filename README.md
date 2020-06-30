# Introduction to Tornado
![Introduction to Tornado](https://learning.oreilly.com/library/cover/9781449312787/)<br>
电子书地址: [O'Reilly book](http://shop.oreilly.com/product/0636920021292.do)<br>
原书示例代码：[GitHub](https://github.com/Introduction-to-Tornado/Introduction-to-Tornado)

## 本项目是照《Introduction to Tornado》做的练习

Tornado官网站：[链接](https://www.tornadoweb.org/en/stable/)<br>
Tornado源码：[GitHub](https://github.com/tornadoweb/tornado)

### 目录
#### 第一章 Introduction
Example 1-1. The basics: [hello.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/1.%20Introduction/hello.py)<br>
Example 1-2. Handing input: [string_service.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/1.%20Introduction/string_service.py)<br>
Example 1-3. Custom error response: [hello-errors.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/1.%20Introduction/hello-errors.py)
#### 第二章 Forms and Templates
Example 2-1. Simple forms and templates: [poemmaker.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/poemmaker.py)
> 模板文件（同时这些文件对应Example 2-3, 2-4）：[`index.html`](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/templates/index.html) 和 [`poem.html`](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/templates/poem.html)

Example 2-4. Complete forms and templates: [main.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/main.py)
> 其他文件（同时这些文件对应Example 2-5, 2-6, 2-7）: [`index24.html`](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/templates/index24.html), [`munged.html`](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/templates/munged.html)和[`style.css`](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/2.Forms%20and%20Templates/static/style.css)
#### 第三章 Extending Templates
Example 3-1.Module basics: [hello_module.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/3.Extending%20Templates/hello_module.py)
> 其他文件[`hello.html`](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/3.Extending%20Templates/templates/hello.html)
#### 第四章 Databases
Example 4-1. A dictionary web service: [definitions_readonly.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/4.Databases/definitions_readonly.py)
> 其他文件，用例需数据：[db_example_words.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/4.Databases/db_example_words.py)

Example 4-2.A read/write dictionary service: [definitions_readwrite.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/4.Databases/definitions_readwrite.py)

Example 4-3.Reading from the database: [burts_books_db.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/4.Databases/burts_books_db.py)
> 其他文件，初始化用例数据，只执行一次：[init_burts_books_db.py](https://github.com/luxxcn/Introduction-to-Tornado/blob/master/4.Databases/init_burts_books_db.py)，以及相关模板页面和静态文件(css和js)

## 备注
----
#### 安装mongodb如果卡在了Installing MongoDB Compass...
>1. 安装时不勾选Compass<br>
>2. 单独安装 [Compass](https://www.mongodb.com/try/download/compass)