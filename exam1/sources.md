# Rebuilding the diagnostic (maintenance note)

The diagnostic Markdown files are the source of truth. To rebuild from this folder:

```sh
python tools/build_diagnostic.py
python tools/build_print_copies.py
```

The builders need python-docx and reportlab. The first generates Word; the second makes a separate print layout from the Word paragraphs. It does not verify Word's own pagination. Native Word layout should be checked before distribution. Keep the files together so the Word and Markdown study links remain usable. The print PDFs include readable directions to the topic folders.
