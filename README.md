# Data Structures — study resources

Study material for CSC225 Exam 1.

## Download and open

You need **Git** to clone the repository and **Python 3.7 or newer** to run the practice
tests. No Python packages need installing for the exercises.

Open a terminal in the folder where you want to keep your work, then run:

```sh
git clone https://github.com/M4-on-Github/CSC225_Data_Structures_TA_resources.git
cd CSC225_Data_Structures_TA_resources
python --version
```

In VS Code, choose **File → Open Folder** and select the cloned repository folder.
Start with [the foundation check](exam1/diagnostic/questions.md),
then edit the matching `exam1/practice/p*.py` starter file. Replace its `pass  # TODO`
lines, save, and run its tests below. Keep the filenames and test files unchanged.

If `python` is not found, use `py` on Windows or `python3` on macOS/Linux in every command
below. If Git or Python is missing, follow your course's setup instructions or ask your TA.
You can also use **Code → Download ZIP** on GitHub; extract it and open the extracted
repository folder before running commands.

## Read the study pages in VS Code

**No Markdown extension is needed.** VS Code includes a Markdown preview.

1. Open `exam1/diagnostic/questions.md` in the Explorer sidebar.
2. Right-click the file's **editor tab** and choose **Open Preview**.
   Alternatively, press **Ctrl+Shift+V** on Windows/Linux or **Cmd+Shift+V** on Mac.
3. Read the formatted page and follow its links to the exercises.

For a side-by-side view, open the Command Palette with **Ctrl+Shift+P**
(**Cmd+Shift+P** on Mac), then choose **Markdown: Open Preview to the Side**.
Seeing `#` headings and other formatting symbols in the text editor is normal;
the preview displays the formatted version.

See [VS Code's Markdown guide](https://code.visualstudio.com/docs/languages/markdown)
for more help. Use **Terminal → New Terminal** to run the test commands below.

## Run your tests

These commands search the current folder **and its subfolders**. They work from the
repository folder, `exam1`, `exam1/practice`, or the folder directly containing the clone.

```sh
# All six practice problems
python -m unittest discover -s . -p "test_p*.py" -v

# Just problem 3; change the filename for another problem
python -m unittest discover -s . -p "test_p3_sorts.py" -v

# Just the heap index helpers
python -m unittest discover -s . -p "test_p5_min_heap.py" -k TestIndexArithmetic -v
```

Keep the quotes around the filename pattern. If the parent folder contains other
projects, restrict the search to this clone:

```sh
python -m unittest discover -s CSC225_Data_Structures_TA_resources -p "test_p*.py" -v
```

- **Failures and errors are expected** while starter functions still contain TODOs.
- **`OK`** means the discovered tests passed. Explain your solution and try a fresh example too.
- **`Ran 0 tests`** means no tests were found, not that your work passed. Check the filename
  pattern and your current folder. Discovery searches downward, not into parent folders;
  if you are inside a topic folder, open a terminal at the repository root.

For the optional one-line-per-problem summary, run `python exam1/practice/check.py`
from the repository root. That helper resolves its test files relative to itself.

## Exam 1

**Foundation check:** [Print PDF](exam1/diagnostic/questions.pdf) · [Read in VS Code](exam1/diagnostic/questions.md) · [Editable Word draft](exam1/diagnostic/questions.docx)

**Answer guide:** [PDF](exam1/diagnostic/answers.pdf) · [Markdown](exam1/diagnostic/answers.md) · [Word draft](exam1/diagnostic/answers.docx)

Try the four-page check first, then use the answer guide to choose a [study path](exam1/study_paths.md).
It covers worst-case efficiency, sorting pseudocode, and an optional paper heap exercise.

### Study and review

- [Study paths and coding checkpoints](exam1/study_paths.md)
- [Guided practice](exam1/guided_practice.md) · [Hints and worked examples](exam1/hints.md)
- [Quick reference](exam1/quick_reference.md)
- [Mixed readiness check](exam1/mock_exam/questions.md) · [Solutions](exam1/mock_exam/solutions.md)

Start with the foundation check, then study the topic you need. The longer mocks and coding tasks are optional practice. Heaps depend on course coverage.

| Topic | Review | Mock questions | Solutions |
|---|---|---|---|
| Python classes and argument passing | [Review](exam1/topics/1-python-review/review.md) | [Questions](exam1/topics/1-python-review/mock.md) | [Solutions](exam1/topics/1-python-review/solutions.md) |
| Big-O and counting operations | [Review](exam1/topics/2-big-o/review.md) | [Questions](exam1/topics/2-big-o/mock.md) | [Solutions](exam1/topics/2-big-o/solutions.md) |
| Arrays, lists, and search | [Review](exam1/topics/3-arrays/review.md) | [Questions](exam1/topics/3-arrays/mock.md) | [Solutions](exam1/topics/3-arrays/solutions.md) |
| Sorting | [Review](exam1/topics/4-sorting/review.md) | [Questions](exam1/topics/4-sorting/mock.md) | [Solutions](exam1/topics/4-sorting/solutions.md) |
| Heaps | [Review](exam1/topics/5-heaps/review.md) | [Questions](exam1/topics/5-heaps/mock.md) | [Solutions](exam1/topics/5-heaps/solutions.md) |

### Coding practice

[Practice instructions](exam1/practice/README.md) · [Test commands](#run-your-tests) · [Summary checker](exam1/practice/check.py)

Open a starter to read its task. Use the tests to check your attempt; consult a reference answer only after trying.
Do problem 3 before 4, and finish problem 5's MinHeap before 6.

| Problem | Starter and task | Tests | Reference answer |
|---|---|---|---|
| 1 | [Bank account](exam1/practice/p1_bank_account.py) | [Tests](exam1/practice/test_p1_bank_account.py) | [Answer](exam1/practice/solutions/p1_bank_account.py) |
| 2 | [Search](exam1/practice/p2_search.py) | [Tests](exam1/practice/test_p2_search.py) | [Answer](exam1/practice/solutions/p2_search.py) |
| 3 | [Sorting functions](exam1/practice/p3_sorts.py) | [Tests](exam1/practice/test_p3_sorts.py) | [Answer](exam1/practice/solutions/p3_sorts.py) |
| 4 | [Sortable list](exam1/practice/p4_sortable_list.py) | [Tests](exam1/practice/test_p4_sortable_list.py) | [Answer](exam1/practice/solutions/p4_sortable_list.py) |
| 5 | [Min-heap](exam1/practice/p5_min_heap.py) | [Tests](exam1/practice/test_p5_min_heap.py) | [Answer](exam1/practice/solutions/p5_min_heap.py) |
| 6 | [Triage queue](exam1/practice/p6_triage_queue.py) | [Tests](exam1/practice/test_p6_triage_queue.py) | [Answer](exam1/practice/solutions/p6_triage_queue.py) |

## About these materials

These are ungraded practice materials, not exam questions. Confirm exam coverage with your instructor, especially for heaps. The lecture slides are not included here.
