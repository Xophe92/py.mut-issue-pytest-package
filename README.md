# Mutpy : behaviour differences  pytest vs. unittest

TLDR 


* **Issue** : With the pytest runner and test suite, actual mutations are considered (as showed by the -m flag in the command line) but not really applied (?) as all mutations survive. [Details here](#behaviour-with-pytest)

* **Benchmark** : the same kind of tests in unittest kill all mutations. [Details here](#behaviour-with-unittest)




## Set up the environment

git clone this repository then install the package in editable mode:


```bash
git clone git@github.com:Xophe92/py.mut-issue-pytest-package.git
cd py.mut-issue-pytest-package
pip install -e .
```
pytest to make sure everything works as expected:

```bash
(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>pytest
==================================================================================================== test session starts ====================================================================================================
platform win32 -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package
collected 13 items

src\tests\test_pytest.py .......                                                                                                                                                                                       [ 53%] 
src\tests\test_unittest.py ......                                                                                                                                                                                      [100%]

==================================================================================================== 13 passed in 0.13s ===================================================================================================== 
```

## Behaviour with pytest

(I do not know why the script is not identified as such: when I directly use the command py.mut, it just opens the file in notepad... so I added python... before)


The mutations are actually performed but are not killed:

```bash
(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>python env\Scripts\mut.py --runner pytest --target demo.main --unit-test src\tests\test_pytest.py -m      
[*] Start mutation process:
   - targets: demo.main
   - tests: src\tests\test_pytest.py
[*] 7 tests passed:
   - test_pytest [0.11261 s]
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
[0.07141 s] survived
   - [#   2] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) - fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.06882 s] survived
   - [#   3] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) + fibonacci(n + 2)
--------------------------------------------------------------------------------
[0.08190 s] survived
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
[0.06852 s] survived
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
[0.07094 s] survived
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
[0.07158 s] survived
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
[0.07323 s] survived
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
[0.07290 s] survived
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
[0.07296 s] survived
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
[0.06948 s] survived
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
[0.07296 s] survived
[*] Mutation score [1.05929 s]: 0.0%
   - all: 11
   - killed: 0 (0.0%)
   - survived: 11 (100.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)

```

**All mutants survived.**

## Behaviour with unittest
To benchmark this behaviour against the more mature unittest runner, I also created tests in unittest

```bash
(env) C:\Users\Christophe\Documents\Programmation\test_git\pymut\py.mut-issue-pytest-package>python env\Scripts\mut.py --target demo.main --unit-test src\tests\test_unittest.py -m                 
[*] Start mutation process:
   - targets: demo.main
   - tests: src\tests\test_unittest.py
[*] 6 tests passed:
   - test_unittest [0.00000 s]
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
[0.38178 s] killed by test_fib4 (test_unittest.TestFibonacci)
   - [#   2] AOR demo.main: 
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) - fibonacci(n - 2)
--------------------------------------------------------------------------------
[0.00100 s] killed by test_fib4 (test_unittest.TestFibonacci)
   - [#   3] AOR demo.main:
--------------------------------------------------------------------------------
  14:             f'Fibonacci is only defined on positive integers, {n} given.')
  15:     if n <= 2:
  16:         return n
  17:     else:
- 18:         return fibonacci(n - 1) + fibonacci(n - 2)
+ 18:         return fibonacci(n - 1) + fibonacci(n + 2)
--------------------------------------------------------------------------------
[0.37880 s] killed by test_fib4 (test_unittest.TestFibonacci)
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
[0.00100 s] incompetent
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
[0.00100 s] incompetent
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
[0.00100 s] killed by test_fib1 (test_unittest.TestFibonacci)
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
[0.00300 s] killed by test_fib1 (test_unittest.TestFibonacci)
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
[0.00302 s] killed by test_fib1 (test_unittest.TestFibonacci)
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
[0.00100 s] killed by test_fibonacci_zero (test_unittest.TestFibonacci)
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
[0.00202 s] killed by test_fib1 (test_unittest.TestFibonacci)
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
[0.00202 s] killed by test_fib2 (test_unittest.TestFibonacci)
[*] Mutation score [0.92760 s]: 100.0%
   - all: 11
   - killed: 9 (81.8%)
   - survived: 0 (0.0%)
   - incompetent: 2 (18.2%)
   - timeout: 0 (0.0%)
```

**No mutant survived.**
