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

## Assignment: Häufigstes Element (`haeufigstes_element.py`)

**Task:** Find the most frequent number in a list and print it
together with how often it occurs. Checked for several lists.

**What I learned:**
- My first tests were green even though there was a bug. The test
lists just happened to hide it.
- Variables like `max_counter` must be set back to 0 for every new
list. Otherwise the result of the previous list stays in them.
- The `if` check only needs to run once after the inner loop, because
only then `counter` is final. Checking inside the loop gave the same result,
just with more comparisons.
- I added the list `[9, 9, 8]` as a test, so the bug would show up
again if I ever make it again.

**Test cases (checked manually):**
| Input | Why this case | Expected | Actual |
|-------|---------------|----------|--------|
| `[1, 2, 2, 3, 4, 5, 2, 6]` | normal case (task) | 2, 3 times | 2, 3 times |
| `[7, 7, 3, 3, 7, 5, 5, 5, 7, 2]` | normal case (task) | 7, 4 times | 7, 4 times |
| `[9, 9, 8]` | lower max than the list before | 9, 2 times | 9, 2 times |
| `[1, 2]` | tie | 1, 1 time (first one wins) | 1, 1 time |
| `[]` | empty list | no result (not defined by the task) | 0, 0 times ⚠️ see Known limitations |

**Known limitations:**
- An empty list prints `0` and frequency `0`, even though there is
  no 0 in the list. The task doesn't ask for this case, so I only
  documented it.
- If two numbers are equally frequent, only the first one in the list
  is shown.
- The program counts every number again for every position, so it
  gets slow for very long lists. For this task that is fine.

  
## Assignment: Primzahlen (`primzahlen.py`)

**Task:** Ask the user for a number and print for every number from 2
up to it whether it is a prime number. At the end, print the list of
all prime numbers found.

**What I learned:**
- A yes/no question needs a yes/no variable. My first version counted
  divisors, but with `break` the counter can never go higher than 1.
  `is_prime` says directly what I want to know.
- `is_prime` starts as `True` and is only set to `False` when a divisor
  is found. It has to be reset for every new number.
- `range(2, i)` checks every number except 1 and `i` itself. These two
  always divide `i`, so they prove nothing.
- `break` stops the inner loop at the first divisor, because one divisor
  is enough to prove that a number is not prime.
- The 2 works without a special case: `range(2, 2)` is empty, so the
  inner loop never runs and `is_prime` stays `True`.

**Test cases (checked manually):**
| Input | Why this case | Expected | Actual |
|-------|---------------|----------|--------|
| 2 | smallest prime, inner loop never runs | `[2]` | `[2]` |
| 9 | odd number that is not prime | `[2, 3, 5, 7]` | `[2, 3, 5, 7]` |
| 25 | square of a prime | 25 is not prime | 25 is not prime |
| 12 | even number, many divisors | 12 is not prime | 12 is not prime |
| 13 | prime at the upper limit | 13 is prime | 13 is prime |
| 1 | no number to check | `[]` | `[]` |
| 0 | range is empty | `[]` | `[]` |

**Known limitations:**
- Entering text instead of a number crashes the program (`ValueError`
  from `int()`). Handling this with `try`/`except` is planned for
  Programming 2.
- For every number, all possible divisors up to `i - 1` are checked.
  That gets slow for large numbers. For this task that is fine.
