# GoIT Algo HW-09  
## Greedy Algorithms and Dynamic Programming

This homework is about comparing two different ways of solving the coin change problem.
The task is simple: given a fixed set of coins, we need to return change for a specific amount.

The available coin denominations are:
[50, 25, 10, 5, 2, 1]

Two approaches were implemented: a greedy algorithm and a dynamic programming solution.

---

## Greedy approach

The greedy algorithm works by always taking the largest possible coin first.
It reduces the remaining amount step by step until the total sum is reached.

This solution is very fast and easy to understand.
For the given coin set, it also produces an optimal result.

**Time complexity:** O(n), where n is the number of coin types.

**Pros:**
- very fast
- simple logic
- good choice for real cash systems with fixed coins

**Cons:**
- may not work optimally for other coin systems

---

## Dynamic programming approach

The dynamic programming solution calculates the minimum number of coins needed for every value from 0 up to the target amount.
Based on these intermediate results, it builds the final solution.

This approach always finds the optimal result, but it needs more time and memory.

**Time complexity:** O(amount × n)

**Pros:**
- always optimal
- works with any coin denominations

**Cons:**
- slower than greedy
- uses extra memory

---

## Comparison

When the amount becomes large, the greedy algorithm is noticeably faster.
It does not try all possible combinations, which makes it more efficient.

The dynamic programming solution is more reliable in general, but for large amounts it becomes less practical.

---

## Conclusion

For this specific task and coin set, the greedy algorithm is the better option.
It is fast, simple, and gives the correct result.
Dynamic programming is still useful when correctness is more important than performance or when the coin system is unknown.

---

## Example

Amount: 113

Greedy result:
{50: 2, 10: 1, 2: 1, 1: 1}

Dynamic programming result:
{50: 2, 10: 1, 2: 1, 1: 1}
