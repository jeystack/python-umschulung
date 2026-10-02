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

**Known limitations:**
- Entering text instead of a number crashes the program (`ValueError`
  from `int()`). Handling this with `try`/`except` is planned for
  Programming 2.

## Assignment: Palindrom (`palindrom.py`)

**Task:** Implement a Python program that checks
whether a given word is a palindrome.
A palindrome is a word that reads the same forwards
and backwards.

Your program should ask the user for a word and then
output whether or not that word is a palindrome.

**What I learned:**
- Reading user input with `input()` and normalizing it
with `.lower()`, so upper and lower case don't matter
- Reversing a string with slicing `[::-1]`
- Separating display and comparison: the original input is kept
for the output, a lowercase copy is used for the comparison
- Comparing values with `==` (not `=`, which is assignment)
- Formatting output with f-strings
- Branching with `if` / `else`

**Test cases (checked manually):**
| Input | Expected | Rule tested |
|-------|----------|-------------|
| Anna  | "Anna is a palindrome" | case is ignored, original spelling kept in output |
| Otto  | Palindrome | even number of letters |
| Radar | Palindrome | odd number of letters, middle letter stays |
| Haus  | Not a palindrome | reversed word differs |

**Known limitations:**
- An empty input is reported as a palindrome, because an empty string
  reversed is still an empty string (`"" == ""` is `True`). The task
  doesn't require input validation, so I documented it instead.