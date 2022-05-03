# useTime

### 📚 desciption

关于时间的一些utils

### 📜 property

static: 只读属性
dynamic: 意味着你可以改变它的值，且可能与其他动态属性共享状态

#### static

- year: 年 -> str
- month: 月 -> str
- day: 日 -> str
- hour: 时 -> str
- minute: 分 -> str
- second: 秒 -> str

#### dynamic

- time: 时间 -> str
- timestamp: 时间戳 -> int

```python
test.py
from pyuse import useTime

p = useTime()
```

```shell
p.year
>>> 2022

p.month
>>> 02

p.day
>>> 31

p.time
>>> Tue Apr 26 16:45:27 2022

p.timestamp
>>> 1650962851
```

### 🍽️ function

#### get_date()

```shell
t.get_date()
>>> 2022-4-26 下午4:54
```

#### to_time()

```shell
t.to_time(1650526296526, '%Y年%m月%d日')
>>> 2022年04月21日
```

#### to_timestamp()

```shell
t.to_timestamp('2020年12月21日', '%Y年%m月%d日')
>>> 1608480000
```

#### time_now()

```shell
t.time_now()
>>> 2022-04-26 16:57:22
```

### 🎐 demo

```python
from pyuse import useTime

t = useTime()
print(t.time)
print(t.timestamp)

t.timestamp = 1650528033
print(t.time)
print(t.timestamp)
```
