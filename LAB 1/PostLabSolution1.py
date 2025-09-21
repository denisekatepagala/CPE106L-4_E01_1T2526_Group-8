def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        hi = arr[len(arr) // 2]
        lo = arr[len(arr) // 2 - 1]
        med = (hi + lo) / 2
    else:
        med = arr[len(arr) // 2]
    return med

def mean(arr):
    tot = sum(arr)
    return tot / len(arr)

def mode(arr):
    if not arr:
        return None
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    peak = max(freq.values())
    vals = [x for x, c in freq.items() if c == peak]
    if len(vals) == len(arr):
        return None
    return vals[0]

print("\n")
n = int(input('How many values do you want to enter? '))
arr = []
for k in range(n):
    arr.append(int(input('Enter a value for the list: ')))
print("\nList:", arr)
print("Mode:", mode(arr))
print("Median:", median(arr))
print("Mean:", mean(arr))

def mean(data):
    """Compute the mean of a list of numbers."""
    if not data:
        raise ValueError("The list of numbers is empty.")
    return sum(data) / len(data)

def median(data):
    """Compute the median of a list of numbers."""
    if not data:
        raise ValueError("The list of numbers is empty.")
    sorted_numbers = sorted(data)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(data):
    """Compute the mode of a list of numbers."""
    if not data:
        raise ValueError("The list of numbers is empty.")
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    peak = max(freq.values())
    vals = [x for x, c in freq.items() if c == peak]
    if len(vals) == len(data):
        return None
    return vals[0]

def get_user_input():
    """Get the size of the list and individual values from the user."""
    data = []
    n = int(input("\nEnter the size of the list: "))
    for i in range(n):
        val = float(input(f"Enter value {i + 1}: "))
        data.append(val)
    return data

if __name__ == "__main__":
    data_in = get_user_input()
    print("\nMean:", mean(data_in))
    print("Median:", median(data_in))
    print("Mode:", mode(data_in))

def mean(data):
    """Compute the mean of a list of numbers."""
    return sum(data) / len(data)

def median(data):
    """Compute the median of a list of numbers."""
    data.sort()
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

def enhanced_mode(data):
    """Compute the mode(s) of a list of numbers. Returns multiple modes if applicable."""
    if not data:
        raise ValueError("The list of numbers is empty.")
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    peak = max(freq.values())
    vals = [x for x, c in freq.items() if c == peak]
    if len(vals) == len(set(data)):
        return None
    return vals if len(vals) > 1 else vals[0]

n = int(input("\nHow many values do you want to enter? "))
data = []
for k in range(1, n + 1):
    suf = "th"
    if k == 1:
        suf = "st"
    elif k == 2:
        suf = "nd"
    elif k == 3:
        suf = "rd"
    val = float(input(f"Enter the {k}{suf} value: "))
    data.append(val)

print("\n" + "=" * 28)
print("Mean:", mean(data))
print("Median:", median(data))
print("Mode:", enhanced_mode(data))
