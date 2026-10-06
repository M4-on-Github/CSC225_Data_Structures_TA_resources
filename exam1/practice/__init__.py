"""Discover practice tests while preserving their standalone student imports."""

from pathlib import Path
import unittest


def load_tests(loader, tests, pattern):
    # The exercises import neighbouring files by name (for example, p3_sorts).
    # Use practice as their import root, regardless of where discovery began.
    # A separate loader keeps the outer discovery's root intact.
    practice = str(Path(__file__).resolve().parent)
    local_loader = unittest.TestLoader()
    local_loader.testNamePatterns = loader.testNamePatterns
    return local_loader.discover(
        start_dir=practice,
        pattern=pattern or "test*.py",
        top_level_dir=practice,
    )
