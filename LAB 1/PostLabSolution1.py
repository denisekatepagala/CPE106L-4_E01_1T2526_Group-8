def mean(nums):
    if not nums:
        raise ValueError("List is empty.")
    return sum(nums) / len(nums)

def median(nums):
    if not nums:
        raise ValueError("List is empty.")
    sorted_nums = sorted(nums)
    count = len(sorted_nums)
    mid = count // 2
    return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 if count % 2 == 0 else sorted_nums[mid]

def mode(nums):
    if not nums:
        raise ValueError("List is empty.")
    counts = {}
    for v in nums:
        counts[v] = counts.get(v, 0) + 1
    max_count = max(counts.values())
    winners = [v for v, c in counts.items() if c == max_count]
    return None if len(winners) == len(set(nums)) else winners[0]

def read_numbers():
    buf = []
    total = int(input("How many? "))
    for idx in range(1, total + 1):
        buf.append(float(input(f"Value #{idx}: ")))
    return buf

if __name__ == "__main__":
    numbers = read_numbers()
    print("\nMean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
