# mut.py-issue-pytest-package

I have problems to kill mutants when using a package installed in editable mode.

To reproduce the issue:

git clone this repository


```bash
pip install -e .
```
pytest to make sure everything works

```bash
(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>pytest
==================================================================================================== test session starts ====================================================================================================
platform win32 -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package
collected 6 items

src\tests\test_main_module.py ......                                                                                                                                                                                   [100%] 

===================================================================================================== 6 passed in 0.06s ===================================================================================================== 
```


python env\Scripts\mut.py --runner pytest --target demo.main --unit-test src\tests\test_main_module.py -m

(I do not know why the scipt is not identified as such whet I directly py.mut, it just open the file in notepad... so I added python... before)


The mutations are actually performed but are not killed:

```bash
(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>python env\Scripts\mut.py --runner pytest --target demo.main --unit-test src\tests\test_main_module.py -m
[*] Start mutation process:
   - targets: demo.main
   - tests: src\tests\test_main_module.py
[*] 6 tests passed:
   - test_main_module [0.10408 s]
[*] Start mutants generation and execution:
   - [#   1] AOR demo.main:
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n + 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07096 s] survived
   - [#   2] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) - fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.06696 s] survived
   - [#   3] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) + fibonacci(n + 2)
--------------------------------------------------------------------------------
[0.08074 s] survived
   - [#   4] COD demo.main: 
--------------------------------------------------------------------------------
   5:         n (int): The fibonacci number to compute.
   6:     Returns:
   7:         Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
   8:     '''
-  9:     if not (isinstance(n, int)):
+  9:     if isinstance(n, int):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
--------------------------------------------------------------------------------
[0.06962 s] survived
   - [#   5] COI demo.main: 
--------------------------------------------------------------------------------
   5:         n (int): The fibonacci number to compute.
   6:     Returns:
   7:         Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
   8:     '''
-  9:     if not (isinstance(n, int)):
+  9:     if not ((not (isinstance(n, int)))):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
--------------------------------------------------------------------------------
[0.06903 s] survived
   - [#   6] COI demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if not (n <= 0):
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.07246 s] survived
   - [#   7] COI demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if not (n <= 2):
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.06997 s] survived
   - [#   8] ROR demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if n >= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06903 s] survived
   - [#   9] ROR demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if n < 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06896 s] survived
   - [#  10] ROR demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if n >= 2:
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.06686 s] survived
   - [#  11] ROR demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if n < 2:
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07094 s] survived
[*] Mutation score [1.02833 s]: 0.0%
   - all: 11
   - killed: 0 (0.0%)
   - survived: 11 (100.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)

(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>python env\Scripts\mut.py --runner pytest --target demo.main --unit-test src\tests\test_main_module.py -m
[*] Start mutation process:
   - targets: demo.main
   - tests: src\tests\test_main_module.py
[*] 6 tests passed:
   - test_main_module [0.10109 s]
[*] Start mutants generation and execution:
   - [#   1] AOR demo.main:
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n + 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07136 s] survived
   - [#   2] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) - fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07181 s] survived
   - [#   3] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) + fibonacci(n + 2)
--------------------------------------------------------------------------------
[0.08471 s] survived
   - [#   4] COD demo.main: 
--------------------------------------------------------------------------------
   5:         n (int): The fibonacci number to compute.
   6:     Returns:
   7:         Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
   8:     '''
-  9:     if not (isinstance(n, int)):
+  9:     if isinstance(n, int):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
--------------------------------------------------------------------------------
[0.06796 s] survived
   - [#   5] COI demo.main: 
--------------------------------------------------------------------------------
   5:         n (int): The fibonacci number to compute.
   6:     Returns:
   7:         Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
   8:     '''
-  9:     if not (isinstance(n, int)):
+  9:     if not ((not (isinstance(n, int)))):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
--------------------------------------------------------------------------------
[0.06998 s] survived
   - [#   6] COI demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if not (n <= 0):
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06860 s] survived
   - [#   7] COI demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if not (n <= 2):
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07321 s] survived
   - [#   8] ROR demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if n >= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06996 s] survived
   - [#   9] ROR demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if n < 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06960 s] survived
   - [#  10] ROR demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if n >= 2:
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07080 s] survived
   - [#  11] ROR demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if n < 2:
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07196 s] survived
[*] Mutation score [1.04413 s]: 0.0%
   - all: 11
   - killed: 0 (0.0%)
   - survived: 11 (100.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)

(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>python env\Scripts\mut.py --runner pytest --target demo.main --unit-test . -m                              
[*] Start mutation process:
   - targets: demo.main
   - tests: .
usage: mut.py [-h] [-c]
mut.py: error: unrecognized arguments: --runner pytest --target demo.main --unit-test . -m

(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>python env\Scripts\mut.py --runner pytest --target demo.main --unit-test src\tests\test_main_module.py -m
[*] Start mutation process:
   - targets: demo.main
   - tests: src\tests\test_main_module.py
[*] 6 tests passed:
   - test_main_module [0.10480 s]
[*] Start mutants generation and execution:
   - [#   1] AOR demo.main:
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n + 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07113 s] survived
   - [#   2] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) - fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07096 s] survived
   - [#   3] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) + fibonacci(n + 2)
--------------------------------------------------------------------------------
[0.08095 s] survived
   - [#   4] COD demo.main: 
--------------------------------------------------------------------------------
   5:         n (int): The fibonacci number to compute.
   6:     Returns:
   7:         Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
   8:     '''
-  9:     if not (isinstance(n, int)):
+  9:     if isinstance(n, int):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
--------------------------------------------------------------------------------
[0.07174 s] survived
   - [#   5] COI demo.main: 
--------------------------------------------------------------------------------
   5:         n (int): The fibonacci number to compute.
   6:     Returns:
   7:         Optional[int]: The n-th fibonacci number is n is positive int, None otherwise.
   8:     '''
-  9:     if not (isinstance(n, int)):
+  9:     if not ((not (isinstance(n, int)))):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
--------------------------------------------------------------------------------
[0.06796 s] survived
   - [#   6] COI demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if not (n <= 0):
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06977 s] survived
   - [#   7] COI demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if not (n <= 2):
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.06691 s] survived
   - [#   8] ROR demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if n >= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.09195 s] survived
   - [#   9] ROR demo.main: 
--------------------------------------------------------------------------------
   8:     '''
   9:     if not (isinstance(n, int)):
  10:         raise TypeError(
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
- 12:     if n <= 0:
+ 12:     if n < 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
--------------------------------------------------------------------------------
[0.06896 s] survived
   - [#  10] ROR demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if n >= 2:
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.06997 s] survived
   - [#  11] ROR demo.main: 
--------------------------------------------------------------------------------
  11:             f'Fibonacci is only defined on integers, {type(n)} given.')
  12:     if n <= 0:
  13:         raise ValueError(
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
- 15:     if n <= 2:
+ 15:     if n < 2:
  16:         return n
  17:     else:
  18:         return fibonacci(n - 1) + fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.07213 s] survived
[*] Mutation score [1.04778 s]: 0.0%
   - all: 11
   - killed: 0 (0.0%)
   - survived: 11 (100.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
```