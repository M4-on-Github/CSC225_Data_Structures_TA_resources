# Runs every practice test file and prints one line per problem.
#
#     python check.py              check YOUR code (the p1..p6 files in this folder)
#     python check.py 3            check only problem 3
#     python check.py --solutions  check the reference answers in solutions/
#     python check.py -v 3         show the full unittest output for problem 3
#
# You do not need this script. Running "python test_p3_sorts.py" directly does the same
# thing for one problem and prints more detail. This is just the whole-folder view, for
# when you want to know what is left.
#
# --solutions runs the tests against solutions/ in a scratch copy, so a broken file of
# your own cannot affect the result. If that mode ever reports a failure, the reference
# answer is wrong and your TA wants to hear about it.

import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

PROBLEMS = [
    (1, "p1_bank_account", "Topic 1  classes and argument passing"),
    (2, "p2_search", "Topic 3  linear and binary search"),
    (3, "p3_sorts", "Topic 4  the five sorts"),
    (4, "p4_sortable_list", "Topic 4  the sorts as a class"),
    (5, "p5_min_heap", "Topic 5  MinHeap, build_heap, heap sort"),
    (6, "p6_triage_queue", "Topic 5  applying a heap"),
]


def parse_args(argv):
    only = []
    verbose = False
    solutions = False
    for arg in argv:
        if arg == "--solutions":
            solutions = True
        elif arg in ("-v", "--verbose"):
            verbose = True
        elif arg.isdigit():
            only.append(int(arg))
        else:
            print("Unrecognised argument: " + arg)
            print("Usage: python check.py [--solutions] [-v] [problem number ...]")
            sys.exit(2)
    return only, verbose, solutions


def run_one(directory, module, verbose):
    # Returns (passed, tests_run, first_problem_line).
    result = subprocess.run(
        [sys.executable, "test_" + module + ".py"],
        cwd=directory,
        capture_output=True,
        text=True,
        errors="replace",
    )
    output = (result.stdout or "") + (result.stderr or "")
    if verbose:
        print(output.rstrip())
        print()

    tests_run = 0
    for line in output.splitlines():
        if line.startswith("Ran ") and " test" in line:
            tests_run = int(line.split()[1])

    detail = ""
    if result.returncode != 0:
        for line in output.splitlines():
            if line.startswith(("FAIL:", "ERROR:")):
                detail = line.strip()
                break
        if not detail:
            for line in output.splitlines():
                if line.startswith(("Traceback", "ImportError", "ModuleNotFoundError")):
                    detail = line.strip()
                    break
    return result.returncode == 0, tests_run, detail


def solutions_copy():
    # The tests import "p3_sorts", which resolves to whichever copy sits next to them.
    # So put the tests next to the reference files instead of next to the starters.
    temp = tempfile.mkdtemp(prefix="ds_solutions_")
    for name in os.listdir(os.path.join(HERE, "solutions")):
        if name.endswith(".py"):
            shutil.copy(os.path.join(HERE, "solutions", name), temp)
    for name in os.listdir(HERE):
        if name.startswith("test_") and name.endswith(".py"):
            shutil.copy(os.path.join(HERE, name), temp)
    return temp


def main():
    only, verbose, solutions = parse_args(sys.argv[1:])
    chosen = [p for p in PROBLEMS if not only or p[0] in only]
    if not chosen:
        print("No such problem. There are 6.")
        return 2

    directory = HERE
    temp = None
    if solutions:
        temp = solutions_copy()
        directory = temp
        print("Checking the REFERENCE answers in solutions/.\n")
    else:
        print("Checking YOUR answers. Try first; consult one solution section if stuck.\n")

    total = 0
    failed = []
    try:
        for number, module, title in chosen:
            passed, tests_run, detail = run_one(directory, module, verbose)
            total += tests_run
            mark = "pass" if passed else "FAIL"
            print("  %s  problem %d  %-18s %3d tests  %s"
                  % (mark, number, module.split("_", 1)[1], tests_run, title))
            if not passed:
                failed.append(number)
                if detail:
                    print("           %s" % detail)
    finally:
        if temp:
            shutil.rmtree(temp, ignore_errors=True)

    print("\n  %d tests run." % total)
    if failed:
        print("  Still to do: " + ", ".join("problem %d" % n for n in failed))
        print("  Run one on its own for the details, e.g. "
              "python test_%s.py" % PROBLEMS[failed[0] - 1][1])
        return 1
    print("  All selected problems pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
