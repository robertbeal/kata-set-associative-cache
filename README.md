
# Getting Started

`make build test`

(or view the `Makefile` for the docker commands to run)

# Usage

```
setCount = 10
setSize = 50
cache = Cache(str, str, setCount, MRUPolicy(50))
cache.add('foo', 'bar')
cache.get('foo')
>>> 'bar'
```
```
class FooPolicy:
  def __init__(self, setSize):
    # some code

  def update(self, tag):
    # some code

  def remove(self):
    # some code

cache = Cache(10, FooPolicy(50))
```
