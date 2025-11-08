# Weekly Payments Generator (Python)

A simple Python script that simulates weekly payment slip generation for a workforce of 400 employees, assigning levels based on salary and gender conditions and printing a one-line payslip for each worker.

> File: `main.py`

## Overview

The script:
- Dynamically creates a list of 400 workers with random genders and salaries.
- Iterates over each worker and assigns an employee level based on rules.
- Prints a structured payment slip line per worker.
- Wraps execution in a `try/except` to surface unexpected errors.

## Features

- 400 workers generated automatically (IDs 1–400)
- Random gender: `Male` or `Female`
- Random salary: $1,000–$35,000
- Level assignment rules with precedence
- Compact textual output (one line per worker)

## Employee level rules

Levels are assigned inside the loop in this order:
1. If salary is > $10,000 and < $20,000 → level `A1`.
2. If salary is > $7,500 and < $30,000 and gender is `Female` → level `A5-F`.

Notes about the rules:
- Boundaries are strict. Salaries exactly equal to 7,500, 10,000, 20,000, or 30,000 do not qualify.
- Because rule 2 runs after rule 1, it can override `A1` for eligible female workers. Example: salary $18,000 and gender `Female` results in `A5-F`.
- If no rule matches, level remains `None`.

## Requirements

- Python 3.8+ (standard library only; uses `random`)

## How to run

From the repository root:

```bash
python main.py
```

The script will print 400 lines, one per worker.

## Sample output

Example lines (your output will vary due to randomness):

```
Payment Slip: ID=1, Name=Worker_1, Gender=Female, Salary=$18342, Level=A5-F
Payment Slip: ID=2, Name=Worker_2, Gender=Male,   Salary=$9123,  Level=None
Payment Slip: ID=3, Name=Worker_3, Gender=Male,   Salary=$15480, Level=A1
```

## Error handling

All logic is wrapped in a `try/except`. If an unexpected error occurs, you will see:

```
You encountered an error <error details>
```

## Customization

You can quickly tweak the script:

- Number of workers: change the `range(400)` to your desired count.
- Salary band: adjust `random.randint(1000, 35000)` to fit your pay scale.
- Reproducible runs: add a seed before generation, e.g. `random.seed(42)`.
- Level logic: convert the two `if` statements into `if/elif` if you want to prevent overrides, or keep as-is if `A5-F` should take precedence.