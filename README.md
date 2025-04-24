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

The above algorithm is called "linear search".  You can visit 
https://env3d.github.io/algorithm-binary-search/animate.html and click the "Run Linear Search"
or the "Step Linear Search" button to see how it works.

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=list_of_items%20%3D%20%5B'it',%20'was',%20'the',%20'season',%20'of',%20'light',%20'it',%20'was',%20'the',%20'season',%20'of',%20'darkness'%5D%0A%0Adef%20find_item_in_list%28target%29%3A%0A%20%20%20%20for%20item%20in%20list_of_items%3A%0A%20%20%20%20%20%20%20%20if%20target%20%3D%3D%20item%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20return%20False%0A%20%20%20%20%0Afind_item_in_list%28'light'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


Then, we’ll introduce binary search. It uses the exact same coding building
blocks (variables, loops, conditionals), but by arranging them differently, we can achieve dramatically faster performance. This highlights the power 
of algorithms: even simple tools, when structured wisely, can lead to 
huge improvements.