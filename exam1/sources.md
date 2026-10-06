# Sources and scope

The existing topic reviews cite the course lecture decks by name, deck number and slide. The professor's slides are not distributed here. Use your course copies to check those citations.

The diagnostic, guided exercises and mixed readiness check are TA practice material. Their questions assess the concepts in this package; they do not establish the exam's scope or predict its questions.

No dedicated heap deck was available for this package. The heap implementation and extended exercises supplement the cited heap property and costs. Confirm heap coverage with your instructor before including that study path.

The diagnostic Markdown files are the source of truth. To rebuild from this folder:

```sh
python tools/build_diagnostic.py
python tools/build_print_copies.py
```

The builders need python-docx and reportlab. The first generates Word; the second makes a separate print layout from the Word paragraphs. It does not verify Word's own pagination. Native Word layout should be checked before distribution. Keep the files together so the Word and Markdown study links remain usable. The print PDFs include readable directions to the topic folders.
