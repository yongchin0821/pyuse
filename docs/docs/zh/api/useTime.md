# useTime

### ð desciption

å³äºæ¶é´çä¸äºutils

### ð property

static: åªè¯»å±æ§  
dynamic: æå³çä½ å¯ä»¥æ¹åå®çå¼ï¼ä¸å¯è½ä¸å¶ä»å¨æå±æ§å±äº«ç¶æ

#### static

- year: å¹´ -> str
- month: æ -> str
- day: æ¥ -> str
- hour: æ¶ -> str
- minute: å -> str
- second: ç§ -> str

#### dynamic

- time: æ¶é´ -> str
- timestamp: æ¶é´æ³ -> int

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

### ð½ï¸ function

#### get_date()

```shell
t.get_date()
>>> 2022-4-26 ä¸å4:54
```

#### to_time()

```shell
t.to_time(1650526296526, '%Yå¹´%mæ%dæ¥')
>>> 2022å¹´04æ21æ¥
```

#### to_timestamp()

```shell
t.to_timestamp('2020å¹´12æ21æ¥', '%Yå¹´%mæ%dæ¥')
>>> 1608480000
```

#### time_now()

```shell
t.time_now()
>>> 2022-04-26 16:57:22
```

### ð demo

```python
from pyuse import useTime

t = useTime()
print(t.time)
print(t.timestamp)

t.timestamp = 1650528033
print(t.time)
print(t.timestamp)
```
