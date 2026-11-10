#!/usr/bin/env python3
"""
Happy numbers: numbers that reach 1 by repeatedly summing the squares of their digits.
"""

def sum_of_squares(n: int) -> int:
    """Return the sum of the squares of the digits of n."""
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def is_happy(n: int) -> bool:
    """Return True if n is a happy number."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1


def sequence(n: int) -> list[int]:
    """Return the sequence of numbers until it cycles or reaches 1."""
    path = []
    seen = set()
    while n not in seen:
        path.append(n)
        if n == 1:
            break
        seen.add(n)
        n = sum_of_squares(n)
    if n != 1 and n in seen:
        # mark the cycle start if needed, but for display just stop
        path.append(n)
    return path


def happy_up_to(limit: int) -> list[int]:
    """Return all happy numbers from 1 to limit inclusive."""
    return [i for i in range(1, limit + 1) if is_happy(i)]


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Explore happy numbers."
    )
    parser.add_argument(
        "n",
        nargs="?",
        type=int,
        help="Check a single number and show its sequence",
    )
    parser.add_argument(
        "--up-to",
        type=int,
        metavar="LIMIT",
        help="List all happy numbers up to LIMIT",
    )
    args = parser.parse_args()

    if args.up_to is not None:
        if args.up_to < 1:
            print("Limit must be at least 1")
            return
        happies = happy_up_to(args.up_to)
        print(f"Happy numbers from 1 to {args.up_to}:")
        print(" ".join(str(h) for h in happies))
        print(f"Count: {len(happies)}")
        return

    if args.n is None:
        parser.print_help()
        return

    if args.n < 1:
        print("Number must be positive")
        return

    seq = sequence(args.n)
    print(f"Sequence for {args.n}:")
    print(" -> ".join(str(x) for x in seq))
    if seq[-1] == 1:
        print("Happy")
    else:
        print("Not happy (cycle detected)")


if __name__ == "__main__":
    main()
