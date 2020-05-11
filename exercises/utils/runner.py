#!/usr/bin/env python3
"""
Runs the test suite and prints the results to standard output.
It uses the given separator in the following way:

<Meta-separator>
#Test Run
<Meta-separator>
Error 1
<Separator>
...
<Separator>
Error N
<Meta-separator>
Failure 1
<Separator>
...
<Separator>
Failure M
<Meta-separator>
"""
import unittest
import traceback
import sys


def main():
    metasep = sys.argv[1]
    sep = sys.argv[2]

    try:
        import tests
    except SyntaxError as e:
        runs = 1
        errors = [f"{e}\n{traceback.format_exc()}"]
        failures = []
    else:
        suite = unittest.TestLoader().loadTestsFromModule(tests)
        result = unittest.TextTestRunner(verbosity=0).run(suite)

        runs = result.testsRun
        errors = list(map(lambda x: f"{x[0]}\n{x[1]}", result.errors))
        failures = list(map(lambda x: f"{x[0]}\n{x[1]}", result.failures))

    print(metasep, end="")
    print(runs, end="")
    print(metasep, end="")
    print(sep.join(errors), end="")
    print(metasep, end="")
    print(sep.join(failures), end="")
    print(metasep, end="")


if __name__ == "__main__":
    main()
