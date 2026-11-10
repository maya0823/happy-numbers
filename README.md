# Happy Numbers

A happy number reaches 1 when you keep replacing it with the sum of the squares of its digits. Numbers that do not reach 1 enter a cycle instead.

This small script checks whether a number is happy, prints the sequence of digit-square sums, and can list every happy number up to a given limit.

## What you can learn

- How to break a number into digits with modulo and integer division
- Detecting cycles in a short sequence with a set
- Writing a small command-line tool with argparse

## Learning from mistakes

- Forgetting to stop at 1 means the sequence never ends for happy numbers.
- Using a list instead of a set for seen values makes cycle detection slower than it needs to be for this problem.

## How to run / usage

Requires Python 3.9+ (stdlib only).

Check one number and show its path:

```
python happy.py 19
```

List every happy number up to 100:

```
python happy.py --up-to 100
```

## Notes

The classic unhappy cycle is 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4. Any number that lands on one of these is unhappy.

## License

MIT
