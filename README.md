# IE7374 - MLOps Lab 1

## Overview
This lab demonstrates the foundational MLOps workflow including virtual environment setup, version control with GitHub, unit testing with Pytest and Unittest, and CI/CD automation using GitHub Actions.

## Project Structure
```
IE7374-Lab1/
├── src/
│   └── calculator.py       # Calculator functions
├── test/
│   ├── test_pytest.py      # Pytest test cases
│   └── test_unittest.py    # Unittest test cases
├── .github/
│   └── workflows/
│       ├── pytest_action.yml    # GitHub Actions for Pytest
│       └── unittest_action.yml  # GitHub Actions for Unittest
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Kranthi0011/IE7374-Lab1.git
cd IE7374-Lab1
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv lab_01
source lab_01/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Calculator Functions
The `src/calculator.py` file contains the following functions:

- `fun1(x, y)` — Returns the sum of x and y
- `fun2(x, y)` — Returns the difference of x and y
- `fun3(x, y)` — Returns the product of x and y
- `fun4(x, y)` — Returns the combined result of fun1, fun2, and fun3

## Running Tests

### Using Pytest
```bash
pytest test/test_pytest.py
```

### Using Unittest
```bash
python -m unittest discover -s test -p "test_unittest.py"
```

## GitHub Actions
This project includes two automated CI workflows that trigger on every push to the `main` branch:

- **Testing with Pytest** — Runs all Pytest test cases and uploads an XML report as an artifact
- **Python Unittests** — Runs all Unittest test cases

## Author
Kranthi Kiran  
Northeastern University — IE7374 MLOps# IE7374-Lab1
