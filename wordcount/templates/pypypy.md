문자열을 숫자형과 곱하면 숫자형만큼 문자형이 반복된다.

```python
>>> a = "python"
>>> 2 * a
'pythonpython'
```

문자열의 길이는 len 함수를 이용하여 구할 수 있다. len 함수는 python의 기본 내장함수이다.

```python
>>> a = 'python!'
>>> len(a)
7
```

문자열 인덱싱이란 문자마다 번호를 매기는 것을 말한다. 

```
You need Python
0         1
012345678901234
```

다음의 문자열에서 Python의 h는 12번째 문자임을 알 수 있다. 인덱싱은 다음과 같이 한다.

```python
>>> a = 'You need Python'
>>> a[12]
'h'
```

가만보면 'h' 가 12번째가 아니라 13번째 문자라고 생각할 수 있을 것이다. 파이썬 인덱싱의 가장 중요한 점은 **0부터 숫자를 센다**는 것이다.


따라서 위의 변수 a에는 15개의 문자가 있지만 0부터 숫자를 세기 때문에 인덱싱의 번호는 14번까지 존재하고, 15번 문자는 찾을 수 없다.

```python
>>> a[0]
'Y'
>>> a[14]
'n'
>>> a[15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

인덱싱에 음수값을 넣으면 문자열의 뒤에서부터 문자를 찾는다. 역시 문자열의 길이를 벗어나면 에러값을 나타낸다.

```python
>>> a[-1]
'n'
>>> a [-15]
'Y'
>>> a [-16]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

슬라이싱이란 문자열의 단어를 뽑아내기 위한 방법이다. 방법은 아래와 같다.

```python
>>> a = "You need Python"
>>> b = a[0] + a[1] + a[2]
>>> b
'You'
```

