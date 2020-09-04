from collections import namedtuple  # namedtuple
from collections import defaultdict  # defaultdict
from collections import Counter  # Counter
from collections import deque  # deque


def run():
    # namedtuple
    Color = namedtuple('Color', ['red', 'green', 'blue'])
    color = Color(red=55, green=155, blue=255)
    print(color.red)

    # defaultdict
    '''
    defaultdict replaces method below:
    for c in 'IndianPythonista':
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    '''
    d = defaultdict(int)
    for c in 'IndianPythonista': d[c] += 1
    print(d)

    # Counter
    a = [1, 2, 3, 4, 2, 3, 4, 1, 2, 3]
    c = Counter(a)
    print(c)
    print(c[1])

    # deque
    '''
    Faster when adding elements to the end/beginning of a list
    '''
    d = deque("hello")  # Accepts any iterable element
    d.append('4')
    d.appendleft('5')
    x = d.pop()
    y = d.popleft()
    print(f'{d}: popped {x} and {y}')
    d.extend('456')
    d.extendleft('hello')
    print(d)
    d.rotate(-2)
    print(d)

    d = deque('hello', maxlen=5)
    print(d)
    d.extend([1, 2, 3])
    print(d)
