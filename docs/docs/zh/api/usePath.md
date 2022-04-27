# usePath

### 📚 desciption

关于路径的一些utils

### 🪧 property

static: 只读属性
dynamic: 意味着你可以改变它的值，且可能与其他动态属性共享状态

#### static

- floder_path: 目录路径 -> str
- exec_path: 执行路径 -> str
- file_path: 文件路径 -> str
- filename: 文件名 -> str

#### dynamic

- alias: 别名路径字典 -> dict
  默认为 {"~": <exec_path> }

```python
test.py
from pyuse import usePath

p = usePath()
```

```shell
p.exec_path
>>> /home/pyuse

p.file_path
>>> /home/pyuse

p.filename
>>> test

p.alias
>>> {"~": "/home/pyuse"}
```

### 🍽️ function

#### path()

```shell
p.path("~/reports/log.txt")
>>> /home/pyuse/reports/log.txt
```

### 🎐 demo

```python
from pyuse import usePath

p = usePath()
report_path = p.path("~/reports/report.txt")
```
