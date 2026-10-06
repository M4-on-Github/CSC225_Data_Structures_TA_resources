# Data Structures — TA resources

Study material I prepare as the course TA.

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
Start with [the foundation check](exam1/START_HERE.md),
then edit the matching `exam1/practice/p*.py` starter file. Replace its `pass  # TODO`
lines, save, and run its tests below. Keep the filenames and test files unchanged.

If `python` is not found, use `py` on Windows or `python3` on macOS/Linux in every command
below. If Git or Python is missing, follow your course's setup instructions or ask your TA.
You can also use **Code → Download ZIP** on GitHub; extract it and open the extracted
repository folder before running commands.

## Read the study pages in VS Code

**No Markdown extension is needed.** VS Code includes a Markdown preview.

1. Open `exam1/START_HERE.md` in the Explorer sidebar.
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

**[Start here: foundation check and study paths](exam1/START_HERE.md)**

Begin with 12 short questions, choose one area to review, and use hints when needed.
The diagnostic is available in Markdown, Word and printable PDF, with a separate answer guide.

Five topics, each with a review sheet, a mock test and a solutions file, plus six practice
coding problems with `unittest` checks:

| | Topic |
|---|---|
| 1 | Python review — classes and argument passing |
| 2 | Big-O and counting operations |
| 3 | Arrays, Python lists, and search |
| 4 | Sorting — all five algorithms |
| 5 | Heaps |

## Notes

- This is **practice material I wrote**, not the professor's exam and not a prediction of
  one. Nothing here is drawn from a real paper.
- Nothing is scored. There are no marks on any question — the mocks are there to show
  whether a topic is understood.
- The lecture slides themselves are **not** in this repo. They are the professor's
  material; the files cite them by deck and slide number instead.
