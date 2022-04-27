# useGenerator

### 📚 desciption

a utils library for generating some test datas

### 🍽️ function

#### get_phone()

```python
g.get_phone()
>>> 15866924846
```

#### get_username()

```python
g.get_username("some text")
>>> UZRhZM
```

#### get_passwd()

```python
g.get_username("some text")
>>> Rx19371684
```

#### get_email()

```python
g.get_username("some text")
>>> Rz092686@163.com
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
