# Programmierung 1

Assignments from my Python class. Each section
describes the task and what I learned from it.

## Assigment: Schaltjahr (`schaltjahr.py`)

**Task:** Implement the a Python program that checks
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