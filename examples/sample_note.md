# Binary Search Algorithm

Binary search is an efficient algorithm for finding an element in a sorted array. It works by repeatedly dividing the search interval in half.

## Time Complexity
- **Time**: O(log n)
- **Space**: O(1)

## How It Works
1. Compare the target with the middle element
2. If they match, return the index
3. If target is less than middle, search left half
4. If target is greater than middle, search right half
5. Repeat until element is found or search space is empty

## Implementation

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element not found
```

## Key Points
- **Requirement**: Array must be sorted
- **Efficiency**: Much faster than linear search for large arrays
- **Use Cases**: Finding elements in sorted data, implementing set operations

## Common Mistakes
1. Off-by-one errors in boundary conditions
2. Forgetting to handle the case when element is not found
3. Not considering integer overflow in mid calculation 