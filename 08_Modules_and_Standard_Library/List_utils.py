def find_max(items):
    return max(items)

def find_min(items):
    return min(items)

def remove_duplicates(items):
    return list(set(items))

def sort_list(items):
    return sorted(items)

def reverse_list(items):
    return items[::-1]

def sum_list(items):
    return sum(items)

def average_list(items):
    return sum(items) / len(items) if items else 0

def search_item(items, target):
    return target in items

def count_occurrences(items, target):
    return items.count(target)

def demo():
    numbers = [5, 3, 8, 3, 1, 5]

    print("=== List Utilities Demo ===")
    print(f"Original: {numbers}")
    print(f"Sorted: {sort_list(numbers)}")
    print(f"No duplicates: {remove_duplicates(numbers)}")


if __name__ == "__main__":
    demo()