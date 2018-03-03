# Toy Problems

Collection of toy problems written in Python.

Commit legend:

```
docs     | documentation related
ops      | operations related (dependency/lock-file updates, configuration changes, etc.)
solve    | solves a toy problem
prog     | begins a solution to a toy problem
fix      | adds a fix for an issue
test     | adds a test
refactor | refactoring-related (DRY-up some parts of the code)
style    | code-style related (adding line breaks, removing whitespace, etc.)
```
Cloning down for first time: `virtualenv venv`

Install packages: `pip3 install -r requirements.txt`

Activate virtualenv: `source env/bin/activate` or `source venv/bin/activate`

Deactivate virtualenv: `deactivate`

Freeze current state: `pip freeze > requirements.txt`

Run tests:

`cd <top-level-directory>` e.g. `cd toy-problem-collection/algorithms/arrays`

`python -m unittest tests/<module-name>`
