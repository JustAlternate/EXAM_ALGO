def suite_collatz(N):
    if N == 1:
        return 1
    if N % 2 == 0:
        return 1 + suite_collatz(N//2)
    return 1 + suite_collatz(3*N + 1)


print("Question 1")  # 6171 : 262

biggest = (0, 0)
for i in range(1, 10_000+1):
    total = suite_collatz(i)
    print(i, total)

print("Question 2")  # 8400511 : 686

biggest = (0, 0)
for i in range(1, 10_000_000+1):
    total = suite_collatz(i)
    if total >= biggest[1]:
        print(i, total)
        biggest = i, total
