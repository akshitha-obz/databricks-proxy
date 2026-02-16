data = [1, 2, 3]

# Safe index access with bounds checking
def safe_get_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None  # or raise custom exception or handle differently

# Example usage
element = safe_get_element(data, 10)
if element is not None:
    print(element)
else:
    print(f"Index {10} is out of range. List has {len(data)} elements.")