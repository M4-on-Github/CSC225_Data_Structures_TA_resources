# Sources and scope

The topic reviews draw on the course lecture decks. The diagnostic, mocks, coding tasks,
and solutions are TA practice materials, not exam questions or a prediction of coverage.
The heap exercises extend the limited heap material available in the decks; confirm heap
coverage with the instructor.

## Rebuilding the diagnostic

The diagnostic Markdown files are the source of truth. To rebuild from this folder:

```sh
python tools/build_diagnostic.py
python tools/build_print_copies.py
```

The builders need python-docx and reportlab. The first generates Word; the second makes a separate print layout from the Word paragraphs. It does not verify Word's own pagination. Native Word layout should be checked before distribution. Keep the files together so the Word and Markdown study links remain usable. The print PDFs include readable directions to the topic folders.
