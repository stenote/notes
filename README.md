# mysite

开始进行 `django` 学习. 每日学习进度如下:

| 日期 | 内容 |
| ---- | ---- |
| 10/09 | 进行 django 的简单初始化学习 |
| 10/10 | django project 的基本结构, app 的创建, app 结构 |


---

## 10/09

### django 的安装

```shell
sudo pip install -U django
```

安装完成后, 可进行 `django` 的安装检查:

```shell
sudo pip list | grep django
```

或者进入 `python shell`, 执行如下命令进行检查

```python
import django
print(django.VERSION)
```

如果无法正常 `import`, 表示有问题。最终, 会正常输出当前 `django` 的版本.

### django 的项目初始化

`django` 自己提供了一个 `django-admin` 的工具, 用于进行 `django` 项目的创建:

```shell
django-admin startproject mysite
```

如上, 创建了目前我们开始开发的项目: mysite

目录结构如下:

```
.
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

2 directories, 5 files
```

其中, `manage.py` 是用来进行 `project` 管理使用的脚本, `mysite` 即为开发的 `projec`.

`mysite` 目录下包含如下几个文件, 一一说明:

* `__init__.py` , 说明 `mysite` 为一个 **package**
* `settings.py`, 项目的配置文件
* `urls.py`, 项目的 url 配置文件
* `wsgi.py`, **wsgi** 的入口文件, 用于项目部署使用

### django app 和 project 的区别

django 在 project 中, 还需要有多个 app, app 和 project 有什么区别呢?

---

app 可以理解为一个独立的模块, 需要独立提供特定服务, 比如: 博客系统, 投票系统 等等. 而 project 是包含了一些列 app 的一个完整的网站, 例如门户网站.

project 可以包含多个 app, 多个 app 构成了一个 project.

同时, 一个 app 可以供多个 project 使用

### django app 相关

#### 创建 app

我们可以使用 `project/manage.py` 来创建 app, 如下:

```
python manage.py startapp polls
```
生成后的结构如下:

```
polls/
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-35.pyc
│   ├── urls.cpython-35.pyc
│   └── views.cpython-35.pyc
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
├── urls.py
└── views.py

2 directories, 11 files
```

简单说明:

* `__init__.py`, polls 为一个独立的包
* `admin.py`, 后续说明
* `apps.py`, 后续说明
* `migrations` 为数据库结构变动的升级脚本
* `models.py` ORM 对象
* `tests.py` app 专用的单元测试
* `urls.py` 用于进行 app 的 url 设定
* `views.py` app 的 controller 


----

### app 的一些简单笔记, 后续补充

#### urls

首先, 我们可以进行 url 的规划, 直接在 app 中创建 urls.py, 通过 `from django.conf.urls import url`, 来创建不同的 url 匹配规则, 同时指定到对应的 views 中的 method

我们还可通过 app 中, include(app.urls) 

严格意义上来说, 所有的 urls.py 都需要时 include 进来


---

#### models 

django 提供了丰富的 models 配置.

我们只需要继承 django.db.models.Model 即可

```

import datetime


from django.db import models

from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

如下为一些简单的操作:

```
Question.objects.all() # 获取所有的 Question, 返回 Question_Set
Question.objects.filter() # 进行部分条件过滤
Question.objects.get() # 只获取一个(要求条件检索结果唯一)

Question.objects.all().delete() # 清空所有, all() 返回的 Question_Set 还可进行其他操作

# 下面 q 代表 Question 的一个实例化对象

q.choice_set.create(choice_text='xxx', votes=0).save()

相当于

Choice(question=q, choice_text='xxx', votes=0).save()

q.choice_set 调用, 不需要在 Question 中申明

进行 filter 或者 get 调用检索, 需要注意 __ 进行区分.

比如, 我只需要查询 choice 的 votes 为 0 的所有的 choice:

Choice.objects.filter(votes=0) 即可

我需要查询 Question 的 id 为 1 的所有的 Choice:

Choice.objects.filter(question__id=1)

查询 Question 的 question_text 以 'hello' 为开头的所有的 Choice

Choice.objects.filter(question__question_text__startswith='hello')
```

设定完 model 后, 我们就可进行 migration 的创建


```
python3 manage.py makemigrations # 创建 migration

python3 manage.py showmigrations polls # 查看 polls 的所有的 migrations, 如果不增加 polls, 则返回所有的 migrations

python3 manage.py sqlmigrat polls 0001 # 查看 migration 转为 SQL 的语句

python3 manage.py migrate # 进行 migrate

如果我们有几个 migrations 还没执行, 我们可以考虑进行合并

python3 manage.py squashmigrations polls 0002 0003

提示后, 会合并为一个 migrations
```
