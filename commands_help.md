# Pytest Command Line Examples

### 1. Basic Commands
Run all tests in the current directory:
    pytest

Run tests in a specific file:
    pytest tests/test_api.py

Run a specific test function in a file:
    pytest tests/test_api.py::test_specific_function

---

### 2. Selecting Tests
Run tests that match an expression (e.g., function names containing "user"):
    pytest -k "user"

Run tests that match "user" but exclude "admin":
    pytest -k "user and not admin"

---

### 3. Marking and Filtering Tests
Run tests with a specific marker (e.g., `smoke`):
    pytest -m "smoke"

Combine markers and expressions:
    pytest -k "user" -m "smoke"

List all defined markers in the project:
    pytest --markers

---

### 4. Test Reporting
Verbose output (show test names and status):
    pytest -v

Quiet mode (minimal output):
    pytest -q

Suppress warnings:
    pytest --disable-warnings

Generate a JUnit XML report:
    pytest --junit-xml=report.xml

Generate an HTML report (requires `pytest-html`):
    pytest --html=report.html

---

### 5. Test Collection
Show the list of collected tests without running them:
    pytest --collect-only

Run only the tests that failed in the last run:
    pytest --lf

Run the last failed tests first, followed by all others:
    pytest --ff

Ignore a specific path during test collection:
    pytest --ignore=tests/old_tests

---

### 6. Debugging and Development
Start the debugger on test failures:
    pytest --pdb

Pause at the start of every test for debugging:
    pytest --trace

Show fixture setup and teardown for each test:
    pytest --setup-show

Only show setup information without running tests:
    pytest --setup-only

---

### 7. Coverage Analysis
Measure test coverage for a module (requires `pytest-cov`):
    pytest --cov=my_project

Generate a coverage report in HTML:
    pytest --cov=my_project --cov-report=html

Generate a coverage report in XML (useful for CI/CD):
    pytest --cov=my_project --cov-report=xml

---

### 8. Plugins and Extensions
Disallow unregistered markers:
    pytest --strict-markers

Generate an HTML report (requires `pytest-html`):
    pytest --html=report.html

Generate a JUnit XML report:
    pytest --junit-xml=report.xml

---

### 9. Parallel Execution
Run tests in 4 parallel threads (requires `pytest-xdist`):
    pytest -n 4

Distribute tests across processors (auto-detection):
    pytest -n auto

---

### 10. Running Specific Test Types
Run all tests in the `tests/` directory:
    pytest tests/

Run tests in a specific file:
    pytest tests/test_api.py

Run tests marked with `smoke` but exclude those marked with `regression`:
    pytest -m "smoke and not regression"

---

### Combining Multiple Options
Example combining several options:
    pytest -k "user and not admin" -m "smoke" --disable-warnings --maxfail=3 -v

This:
- Runs tests matching "user" in the name but excludes "admin".
- Only includes tests marked with `smoke`.
- Suppresses warnings.
- Stops after 3 failures.
- Outputs verbose details.
