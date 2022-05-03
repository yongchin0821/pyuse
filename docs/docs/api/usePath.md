# usePath

### 📚 desciption

utils about of path

### 📜 property

static: read only
dynamic: can be changed，will share state with other dynamic properties


#### static

- floder_path: floder path -> str
- exec_path: execution path -> str
- file_path: file path -> str
- filename: file name -> str

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
