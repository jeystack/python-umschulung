# Programmierung 1

Assignments from my Python class. Each section
describes the task and what I learned from it.

## Assignment: Schaltjahr (`schaltjahr.py`)

**Task:** Implement a Python program that checks
whether a given year is a leap year.
A year is a leap year:

- It is divisible by 4,
- But not divisible by 100, unless it is also divisible
by 400.

Your program should ask the user for a year and then output whether or not that year is a leap year.

**What I learned:**
- Reading user input with `input()` and converting it to a number
with `int()`
- The modulo operator `%` to check divisibility
- Combining conditions with `and` / `or` - `and` binds stronger
than `or`, so the condition works without parentheses
- Branching with `if` / `else`

**Test cases (checked manually):**
| Input | Expected | Rule tested |
|-------|----------|-------------|
| 2023  | No leap year | not divisible by 4 |
| 2024  | Leap year | divisible by 4, not by 100 |
| 1900  | No leap year | divisible by 100, not by 400 |
| 2000  | Leap year | divisible by 400 |