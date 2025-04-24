# Algorithms

Computer science can be thought of as having two complementary sides. 
On one side, there's coding—the set of tools we use to instruct machines. 
These include fundamental concepts like variables, loops, and conditional
statements (if/else) which we have studied exclusively so far in this class.

On the other side, we study how these tools can be combined and structured to
perform sophisticated operations. This is the realm of algorithms, where 
the goal is to solve problems efficiently, whether by speeding things up,
reducing the resources used, or enabling new capabilities altogether.

To illustrate these two sides, let's look at the problem of searching. 
First, we’ll review the straightforward search technique we’ve used in
previous classes: an algorithm that checks for the presence of an item in 
a list, one element at a time.

## Linear Search

Recall that, for all the amazing things a computer can do, it's basically 
a very simple machine that only understands a small number of instructions.
There are also many limitations, one of them being that a computer program
can only operate, or look at "one thing" at a time.  This makes looking 
for a specific item in a long list a laborious process.  We can describe
the process as follows:

```python
list_of_items = ['it', 'was', 'the', 'season', 'of', 'light', 'it', 'was', 'the', 'season', 'of', 'darkness']

def find_item_in_list(target):
    for item in list_of_items:
        if target == item:
            return True
    return False
```

The above algorithm is called "linear search".  You can visit [here](https://env3d.github.io/algorithm-binary-search/animate.html) and click the "Run Linear Search"
or the "Step Linear Search" button to see how it works.

<iframe width="100%" height="800" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=list_of_items%20%3D%20%5B'it',%20'was',%20'the',%20'season',%20'of',%20'light',%20'it',%20'was',%20'the',%20'season',%20'of',%20'darkness'%5D%0A%0Adef%20find_item_in_list%28target%29%3A%0A%20%20%20%20for%20item%20in%20list_of_items%3A%0A%20%20%20%20%20%20%20%20if%20target%20%3D%3D%20item%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20return%20False%0A%20%20%20%20%0Afind_item_in_list%28'light'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


### Questions (best if multiple choice)

 1. Which line performs the actual comparison between the target and each item in the list?
 1. How many times does this comparison happen for the above example? 
 1. The number of comparisons depends on the target item.  
    What is the number of comparisons for the above list if the target is at the end?
 1. For a list of N items, what is the minimum number of comparisons?
 1. For a list of N items, what is the maximum number of comparisons?

## Binary Search

Then, we’ll introduce binary search. It uses the exact same coding building
blocks (variables, loops, conditionals), but by arranging them differently, we can achieve dramatically faster performance. This highlights the power 
of algorithms: even simple tools, when structured wisely, can lead to 
huge improvements.

Let's start with a simple thought experiment.  Recall that in lab 9, we implement
an algorithm to search for the lowest rated movie from a list of movies, our solution 
uses linear search.  To find the minimum rating, we will need to look over the entire
list of movies.  So for a list of N movies, we will need to perform N comparisons.

## Table 1: **Unsorted List (Linear Search)**
| Index | Movie Title         | Rating |
|-------|---------------------|--------|
| 0     | *Inception*         | 7.5    |
| 1     | *The Dark Knight*   | 8.2    |
| 2     | *Interstellar*      | 6.9    |
| 3     | *Dunkirk*           | 9.1    |
| 4     | *Tenet*             | 5.4    |

  - **Process**: Linear search will compare each movie's rating to find the lowest.
  - **Number of Comparisons**: For 5 movies, it will perform 5 comparisons.

But what happens if the movies list is sorted by ratings?  In that case, we don’t need to search because the lowest-rated movie is already at the front of the list.

### Table 2: **Sorted List (Binary Search Assumption)**
| Index | Movie Title         | Rating |
|-------|---------------------|--------|
| 0     | *Tenet*             | 5.4    |
| 1     | *Interstellar*      | 6.9    |
| 2     | *Inception*         | 7.5    |
| 3     | *The Dark Knight*   | 8.2    |
| 4     | *Dunkirk*           | 9.1    |

  - **Process**: Since the list is sorted, the lowest rating is at index `0`.
  - **Number of Comparisons**: **0** (no need to compare; the first item is the lowest).

Here's the rub: you don't get something for nothing.  In order to improve on
linear search, we will have to make an assumption that the list we are searching
has already been sorted.

Now, let's introduce the binary search algorithm to find the presence of a word in 
a sentence.  Below is the formal description:

> Binary search is an efficient algorithm for finding an item in a sorted list. Below are the high-level steps:
> 
> 1. Compare the target value to the middle element of the list.
> 2. If the target matches the middle element, the search is complete.
> 3. If the target is smaller than the middle element, eliminate the right half of the list.
> 4. If the target is larger than the middle element, eliminate the left half of the list.
> 5. Repeat the process until the target is found or the search range is empty.
> 
> ### Key Assumption:
> - The list must be sorted for binary search to work.

You can visit [here](https://env3d.github.io/algorithm-binary-search/animate.html) and click the "Run Binary Search"
or the "Step Binary Search" button to see how it works.

Or if you prefer code:

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=list_of_items%20%3D%20%5B'it',%20'was',%20'the',%20'season',%20'of',%20'light',%20'it',%20'was',%20'the',%20'season',%20'of',%20'darkness'%5D%0Alist_of_items%20%3D%20sorted%28list_of_items%29%0A%0Adef%20find_item_in_list%28target%29%3A%0A%20%20%20%20left,%20right%20%3D%200,%20len%28list_of_items%29%20-%201%0A%20%20%20%20while%20left%20%3C%3D%20right%3A%0A%20%20%20%20%20%20%20%20mid%20%3D%20%28left%20%2B%20right%29%20//%202%0A%20%20%20%20%20%20%20%20item%20%3D%20list_of_items%5Bmid%5D%0A%20%20%20%20%20%20%20%20if%20item%20%3D%3D%20target%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20elif%20item%20%3C%20target%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20left%20%3D%20mid%20%2B%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20right%20%3D%20mid%20-%201%0A%20%20%20%20return%20False%0A%20%20%20%20%0Afind_item_in_list%28'light'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=24&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

NOTE: Not only do we need to sort the list, the code is also considerably more complex.  
This is very typical of advanced algorithms - they are often much more complex in its 
implementation.

### Questions

 1. How many times does this loop happen for the above example? 
 1. The number of loops executed depends on the target item.  
    What is the number of loops for the above list if the target is at the end?
 1. For a list of N items, what is the minimum number of comparisons?
 1. For a list of N items, what is the maximum number of comparisons?


# Real Life Example

Finally, let's look at a real life example of how binary search is vastly more 
efficient than linear search. 

In the program game.py, I implemented an real-time
animation loop where a character in the middle of the screen walks along a path
with buildings in the background. 

The buildings locations are stored in a list, with each number representing the
presence of a building in the x-coordinate.  For example, the following list
shows that there are 10 buildings in the game:

```
[10, 50, 120, 200, 250, 310, 400, 450, 500, 600]
```

Because the screen can only show a limited number of buildings, we only want
to retrieve buildings that are closed to our character location. For example, 
if our character is at location 300, then we may only want to show buildings
in location 250 and 310.  Since this is a real-time animation (i.e. a game)
we will need to perform this serach 30 times per second for the animation
to be smooth.

Modern computers are really fast so you actually won't see any difference 
until we have a really really long list.

Run `python game.py`, there's a total of 1 million buildings in this program,
but only a small number is shown based on the character location.  Use the
spacebar to switch between algorithms and you will see the dramatic difference!
