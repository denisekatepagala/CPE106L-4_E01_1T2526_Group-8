def mean(values):
    if not values:
        return 0
    total = sum(values)
    count = len(values)
    return total / count

def median(values):
    if not values:
        return 0
    sorted_values = sorted(values)
    size = len(sorted_values)
    middle_index = size // 2
    if size % 2 == 0:
        return (sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2
    else:
        return sorted_values[middle_index]

def mode(values):
    if not values:
        return 0
    frequency = {}
    for v in values:
        frequency[v] = frequency.get(v, 0) + 1
    max_freq = max(frequency.values())
    modes = [v for v, count in frequency.items() if count == max_freq]
    return modes[0]  # return first mode if multiple exist

def main():
    sample_data = [12, 23, 443, 54, 12, 324, 53, 42, 54, 65]
    print("Sample data:", sample_data)
    print("Mean:", mean(sample_data))
    print("Median:", median(sample_data))
    print("Mode:", mode(sample_data))

if __name__ == "__main__":
    main()
