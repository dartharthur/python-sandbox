# Python Sandbox

Collection of notes, toy problems, and spikes written in Python.

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

- Install packages: `pip install -r requirements.txt`
- Freeze current state: `pip freeze > requirements.txt`
- Deactivate virtualenv: `deactivate`

Run tests:
- `cd <problem-directory>` e.g. `cd algorithms/two-sum`
- `python -m unittest <test-module-name>` e.g. `python -m unittest test_two_sum.py`