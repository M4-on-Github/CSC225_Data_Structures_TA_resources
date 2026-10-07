"""Integration checks for the student-facing unittest discovery commands.

Run: python -m unittest discover -s tools/tests -v
"""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[2]


class TestStudentDiscovery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="csc225 discovery ")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.parent = Path(cls.temp.name)
        cls.repo = cls.parent / "CSC225_Data_Structures_TA_resources"
        cls.practice = cls.repo / "exam1" / "practice"
        cls.practice.mkdir(parents=True)
        for relative in ("__init__.py", "exam1/__init__.py", "exam1/practice/__init__.py"):
            shutil.copy2(SOURCE / relative, cls.repo / relative)
        # Test reference answers in an isolated clone, never overwrite student work.
        for path in (SOURCE / "exam1/practice/solutions").glob("p*.py"):
            shutil.copy2(path, cls.practice / path.name)
        for path in (SOURCE / "exam1/practice").glob("test_p*.py"):
            shutil.copy2(path, cls.practice / path.name)
        cls.locations = (cls.parent, cls.repo, cls.repo / "exam1", cls.practice)

    def run_discovery(self, cwd, pattern="test_p*.py", extra=(), start="."):
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", start,
             "-p", pattern, *extra],
            cwd=cwd, capture_output=True, text=True, timeout=30,
        )
        return result.returncode, result.stdout + result.stderr

    def test_all_problems_from_each_supported_folder(self):
        for folder in self.locations:
            with self.subTest(folder=str(folder)):
                code, output = self.run_discovery(folder)
                self.assertEqual(code, 0, output)
                self.assertIn("Ran 104 tests", output)

    def test_one_problem_from_each_supported_folder(self):
        for folder in self.locations:
            with self.subTest(folder=str(folder)):
                code, output = self.run_discovery(folder, "test_p3_sorts.py")
                self.assertEqual(code, 0, output)
                self.assertIn("Ran 15 tests", output)

    def test_checkpoint_filters_from_each_supported_folder(self):
        for folder in self.locations:
            with self.subTest(folder=str(folder)):
                code, output = self.run_discovery(
                    folder, "test_p5_min_heap.py", ("-k", "TestIndexArithmetic")
                )
                self.assertEqual(code, 0, output)
                self.assertIn("Ran 4 tests", output)
                code, output = self.run_discovery(
                    folder, "test_p5_min_heap.py",
                    ("-k", "TestEmptyHeap", "-k", "TestInsert"),
                )
                self.assertEqual(code, 0, output)
                self.assertIn("Ran 10 tests", output)

    def test_explicit_clone_path_from_parent(self):
        code, output = self.run_discovery(self.parent, start=self.repo.name)
        self.assertEqual(code, 0, output)
        self.assertIn("Ran 104 tests", output)

    def test_zip_folder_name_from_parent(self):
        with tempfile.TemporaryDirectory(prefix="csc225 zip ") as folder:
            shutil.copytree(self.repo, Path(folder) / (self.repo.name + "-main"))
            code, output = self.run_discovery(folder)
            self.assertEqual(code, 0, output)
            self.assertIn("Ran 104 tests", output)

    def test_unfinished_student_code_reports_failures(self):
        target = self.practice / "p1_bank_account.py"
        reference = target.read_bytes()
        try:
            shutil.copy2(SOURCE / "exam1/practice/p1_bank_account.py", target)
            code, output = self.run_discovery(self.parent, "test_p1_bank_account.py")
            self.assertEqual(code, 1, output)
            self.assertIn("Ran 22 tests", output)
            self.assertIn("FAILED", output)
            self.assertNotIn("No module named", output)
        finally:
            target.write_bytes(reference)


if __name__ == "__main__":
    unittest.main()
