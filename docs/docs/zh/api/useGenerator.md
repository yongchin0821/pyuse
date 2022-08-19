# useGenerator

### 📚 desciption

这是一个用于测试生成测试数据的utils库

### 🍽️ function

#### get_phone()

```python
g.get_phone()
>>> 15866924846
```

#### get_username()

```python
g.get_username()
>>> UZRhZM
```

#### get_passwd()

```python
g.get_passwd()
>>> Rx19371684
```

#### get_email()

```python
g.get_email()
>>> Rz092686@163.com
```

#### get_code()

```python
g.get_code("weak", 6)
>>> gsxmbk
g.get_code("strong", 8)
>>> 6[8Jj!<:
g.get_code()
>>> FiFdBbGE
```

### 🎐 demo

```python
from pyuse import useGenerator

g = useGenerator()

print(g.get_phone())
print(g.get_username())
print(g.get_passwd())
print(g.get_email())
```
