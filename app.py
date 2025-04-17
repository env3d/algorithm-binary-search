import re
import time

words = re.findall(r'\b\w+\b', open('moby-dick.txt').read().lower())
words_sorted = sorted(words)

def search(target, delay=0.001):
    for word in words:        
        if word == target:
            return True
        time.sleep(delay)
    return False

def binary_search(target, delay=0.001):
    left, right = 0, len(words_sorted) - 1
    while left <= right:
        time.sleep(delay)  # Add delay per comparison
        mid = (left + right) // 2
        if words_sorted[mid] == target:
            return True
        elif words_sorted[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(binary_search('captain'))
