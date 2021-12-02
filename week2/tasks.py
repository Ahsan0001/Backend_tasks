empty_graph = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]

simple_graph = [[0,1,1,1],
               [1,0,1,0],
               [1,1,0,0],
               [1,0,0,0]]


grid_3_3 = [[0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 0]]

DEGREE = \
  [('degree', (empty_graph, 0), 0),
   ('degree', (simple_graph, 1), 2),
   ('degree', (grid_3_3, 0), 2),
   ('degree', (grid_3_3, 1), 3),]

IS_PATH = \
  [('is_path', (empty_graph, [0,1]), False),
   ('is_path', (simple_graph, [0,1,2]), True),
   ('is_path', (simple_graph, [0,1,2,0]), True),
   ('is_path', (simple_graph, [0,1,2,0,3]), False),
   ('is_path', (grid_3_3, [1,2,5,4,7,6]), True),
   ('is_path', (grid_3_3, [1,2,5,4,1,0]), False)]

def degree(graph, vertex):
    """
    return the degree of the given vertex in the given graph
    >>> degree(empty_graph, 0)
    0
    >>> degree(simple_graph, 1)
    2
    >>> degree(grid_3_3, 0)
    2
    >>> degree(grid_3_3, 1)
    3
    """
    pass

def is_path(graph, path):
    """
    returns whether the path exists in the given graph
    >>> is_path(empty_graph, [0,1])
    False
    >>> is_path(simple_graph, [0,1,2])
    True
    >>> is_path(simple_graph, [0,1,2,0])
    True
    >>> is_path(simple_graph, [0,1,2,0,3])
    False
    >>> is_path(grid_3_3, [1,2,5,4,7,6])
    True
    >>> is_path(grid_3_3, [1,2,5,4,1,0])
    False
    """
    pass
# Task 3
def print_as_grid(graph, n):
    """
    Input : Grid graph (graph), number of columns (n)
    Effect: Prints the graph organised as grid
    """
    
    def index(r, c):
        return r*n + c
    
    m = len(graph) // n
    
    for i in range(m):
        for j in range(n):
            print('*', end='')
            k = index(i, j)
            if j < n-1 and graph[k][index(i, j+1)]:
                print('---', end='')
            else:
                print('   ', end='')
        print('\n', end='')
        if i < m - 1:
            for j in range(n):
                k = index(i, j)
                if graph[k][index(i + 1, j)]:
                    print('|', end='')
                else:
                    print(' ', end='')
                if j < n-1:
                    print('   ', end='')
            print('\n', end='')




def grid_graph(m, n):
    """
     Implement a function grid graph(m, n) that takes as input two positive
     integers, and returns the adjacency matrix of a m by n grid graph, i.e., a graph with m*n vertices that, when
     drawn on a regular m by n grid, has edges exactly between vertices that lie and neighbouring points on the grid
     >>> grid_graph(1,1)
     [[0]]
     >>> grid_graph(3,3)
     [[0, 1, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 1, 0]]
     >>> grid_graph(2,8)
     [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]]
     >>> grid_graph(6,3)
     [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
     >>> grid_graph(2, 3)
     >>> print_as_grid(grid_graph(2, 3), 3)
     *---*---*
     |   |   |
     *---*---*
     >>> print_as_grid(grid_graph(3,2), 2)
     *---*
     |   |
     *---*
     |   |
     *---*
     >>> print_as_grid(grid_graph(5, 10), 10)
     *---*---*---*---*---*---*---*---*---*
     |   |   |   |   |   |   |   |   |   |
     *---*---*---*---*---*---*---*---*---*
     |   |   |   |   |   |   |   |   |   |
     *---*---*---*---*---*---*---*---*---*
     |   |   |   |   |   |   |   |   |   |
     *---*---*---*---*---*---*---*---*---*
     |   |   |   |   |   |   |   |   |   |
     *---*---*---*---*---*---*---*---*---*
    """
    pass
    

from collections import deque
from graphs import neighbours, print_grid_traversal
import graphs

def bfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> bfs_traversal(g, 0, {12})
    [0, 1, 2, 12]
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---004---003---005---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---006---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass

def dfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {9, 40, 49}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   005---006---008---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   007   009---010---011---012---013---014   
    """
    pass

def bfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, bfs_path(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass

def dfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_path(g, 0, [9, 39]))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---004---005---006---007---008---009   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   010   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   011---012   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass


# Easy Tasks

"""
### is_in()
Write a function is in(char, string) that models a limited version of the behavior of the in keyword (for
more details, refer to the Python docs). You may not use the in keyword in this function.

Input: a string char of a single character (you may limit to alphanumeric), and a string string comprising
both upper and lower case alphanumeric and non-alphanumeric characters.

Output: a boolean, True if char is found in string; otherwise False.

Note: the matching behaviour to be implemented here is different to the matching behaviour of Python’s in
keyword.

### is_sorted()

There is no built-in function that checks whether a sequence is sorted. Write a function is sorted(seq) that
checks whether a given sequence of sortable elements is sorted from smallest to largest.

Input: a sequence seq of comparable elements.

Output: a boolean, True if for all items in the list, the item at index i is less than or equal to the item at
index i + 1; otherwise False.

Note: Remember that a sequence can be a list, a string, a tuple, or a range, so this function must work for all
these types.


### abs()
Write a function abs(x) that models a limited version of the behavior of the built-in function (it is not necessary
to deal with complex numbers).

Input: a float or integer x.

Output: a number of the same type (float or integer) as x, that is the absolute value of x.

###all()
Write a function all(lst) that models a limited version of the behaviour of the built-in function. You may
use the built-in function bool().

Input: a sequence (list) of objects lst.

Output: a boolean, True if all objects in lst have a truth value of True; otherwise False.

###any()
Write a function any(lst) that models a limited version of the behaviour of the built-in function. You may
use the built-in function bool().

Input: a sequence (list) of objects lst.

Output: a boolean, True if at least one object in lst have a truth value of True; otherwise False.

Hint: Think about the behaviour of the function for the empty list as input.

###max()
Write a function max(lst) that models a limited version of the behaviour of the built-in function. In Python,
the max() function is capable of significantly more - read about it here.

Input: a non-empty sequence (list) of comparable objects lst.

Output: the largest item in lst.

###min()
Write a function min(lst) that models a limited version of the behaviour of the built-in function. In Python,
the min() function is capable of significantly more - read about it here.

Input: a non-empty sequence (list) of comparable objects lst.

Output: the smallest item in lst.

###reversed()
Write a function reversed(seq) that models a limited version of the behaviour of the built-in function. You
may not use list slicing (i.e. seq[::-1]) in this function, although it is a cool trick to know!

Input: a sequence seq.

Output: a new list containing all items in lst in reverse order.
Note: Remember that a sequence can be a list, a string, a tuple, or a range, so this function must work for all
these types.

###bin()

Write a function bin(x) that models the behavior of the built-in function.

Input: an integer x.

Output: a binary string representation of x.
Note: The output string should start with ”0b” to communicate it is a binary string (e.g. bin(3) returns
’0b11’). Negative integers and 0 are valid inputs.

###enumerate()
Write a function enumerate(seq[, start]) that models a limited version of the behavior of the built-in
function. In Python, enumerate() returns an enumerate object - enumerate is a specific type that is different
to the list type.

Input: a sequence seq, and an optional argument, an integer start. The default parameter value for start
is 0.

Output: a list of tuples, where each tuple is of the form (n, element). If start=0, n will be the index of
the element, otherwise n will be the index of the element, offset by start.

Note: For an example of enumerate, see the Python docs. Remember that a sequence can be a list, a string, a
tuple, or a range, so this function must work for all these types. If you use yield you must be able to explain
its behaviour to your instructor.

###filter()
Write a function filter(function, seq) that models the behavior of the built-in function.

Input: a function function and a sequence seq.

Output: a list of elements from seq that when used as input in function return a value that is evaluated
to True using Python’s standard truth testing procedure. The relative order between elements must be
maintained.

Note: Remember that a sequence can be a list, a string, a tuple, or a range, so this function must work for all
these types.

###map()
Write a function map(function, seq) that models a limited version of the behavior of the built-in function.

Input: a function function and a sequence seq.

Output: a list comprising the output of function for each element in seq. The order of seq must be
maintained. If seq is empty, return an empty list.

Note: Remember that a sequence can be a list, a string, a tuple, or a range, so this function must work for all
these types.

### lim_range()
Write a function lim range(start, stop[, step]) that models a limited version of the behavior of the sequence type. It is important that you do not name this function range as you are likely to use built-in range
in other functions, and having only a limited version will result in weird behaviour. In Python, range() returns
a range object - range is a specific type that is different to the list type.

Input: two integers, start and stop, and an optional argument, a non-zero integer step. The default
parameter value for step is 1.

Output: a list of integers, counting from start (inclusive) to stop (exclusive), increasing by step.

###round()
Write a function round(number[, ndigits]) that models the behavior of the built-in function.

Input: a float number, and an optional argument, a non-negative integer ndigits. The default parameter
value for ndigits is 0.

Output: if ndigits is 0, an integer, else a float, rounded to ndigits after the decimal point. If the first
dropped digit is greater than 5, round up; if the first dropped digit is less than 5, round down; else round
in such a way that the remaining digit in the smallest position is even.

###set()
Write a function set(lst) that models a limited version of the behavior of the built-in function. In Python,
set() returns a set object - set is a specific type that is different to the list type.

Input: a list lst.

Output: a list that contains the set of elements in lst (i.e.lst with duplicates removed). It is not important
to preserve order.

###sorted()
Write a function sorted(seq) that models a limited version of the behavior of the built-in function.

Input: a sequence seq.

Output: a list comprising the elements of seq in sorted order (i.e. for for all items in the returned list, the
item at index i is less than or equal to the item at index i + 1).

Note: Remember that a sequence can be a list, a string, a tuple, or a range, so this function must work for all
these types.

"""