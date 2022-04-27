# useDingTalk

### 📚 desciption

关于钉钉机器人的一些utils

### 🍽️ function

#### set_config()

```python
ding.set_config(
    access_token="4faxxxxxxxxxxxxxxxxxxxxxxxxx6b28ed",
    key="xxxx",
    app_secret="SECxxxxxxxxxxxxxxx305983",
    at_mobiles=[13500000000, 13800000000],
    is_at_all=False,
)
```

#### send()

```python
ding.send("some text")
```

### 🎐 demo

```python
from pyuse import useDingTalk

d = useDingTalk(
    access_token="4faxxxxxxxxxxxxxxxxxxxxxxxxx6b28ed",
    key="xxxx",
    app_secret="SECxxxxxxxxxxxxxxx305983",
    at_mobiles=[13500000000, 13800000000],
    is_at_all=False,
)
d.send("some text")
```
