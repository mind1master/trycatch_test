## Solution for Trycatch Chess Challenge

- Run program:

    `usage: chess_challenge.py [-h] [--compact]
                          M N kings queens bishops rooks knights`

- Installing coverage/pylint/flake8:
 
    `pip install -r requirements.txt`

- Run tests:

    `make test`

- Run pep8/pylint:

    `make checkers`

- Run coverage:

    `make cov`
    
    `open htmlcov/index.html`

- Tested on python 2.7/3.5.

Computing 7×7 board with 2 Kings, 2 Queens, 2 Bishops and 1 Knight got the following result:

    Got 3063828 variants in 83.5179150105 secs

using desktop PC with Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz.

### Notes
As it can be seen, original solution was more pythonic and easy to read, however the task stated that execution time is important, so multiple optimizations were performed. For example, `.append()` methods were removed in favour of preallocation and index access. Such optimization reduced code readability (however it wins few seconds), so I would probably not do that in real project. Moreover, I have tried to move from recursive implementation to sequential, but it hasn't improved execution time, so I haven't put it into final solution (see branch `inlined`).
