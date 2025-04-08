
import time


def search(target, delay=0.001):
    words = open('moby-dick-words.txt').read().split(' ') 
    for word in words:        
        if word == target:
            return True
        time.sleep(delay)
    return False

def binary_search(target, delay=0.001):
    sorted_list = open('moby-dick-words-sorted.txt').read().split(' ')
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        time.sleep(delay)  # Add delay per comparison
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(search('captain'))
