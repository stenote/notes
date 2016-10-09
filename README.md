# mysite

开始进行 `django` 学习. 每日学习进度如下:

| 日期 | 内容 |
| ---- | ---- |
| 10/09 | 进行 django 的简单初始化学习 |


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

其中, `manage.py` 