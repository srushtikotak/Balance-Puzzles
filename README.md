# Balance-Puzzles
CSCI 603 - Computational Problem Solving - LAB 8

### Implementation
You will implement two classes, Beam and Weight, and a main function that reads a balance
puzzle from a file and verifies it and draws it.

A balance puzzle will be defined in a file as a list of beams, one per line of the file. Each
beam will have a name followed by a list of things attached, and where they are attached:

name   dist1   hanger1   dist2   hanger2   ...

You may assume that each name is B followed by a number, except for the topmost beam
which is simply called B. All distances will be integers and all hangers will be either previously-
defined beam names or positive integers representing weights. For example, the left puzzle
in question 1 of problem solving will be represented as:

B1 -2 6 -1 3 3 5

B2 -1 4 1 2 2 1

B3 -1 B2 1 7

B -1 B1 1 B3

You should read this data in and construct the appropriate objects to represent it. Some
puzzles will be given in which a single weight is given as -1, representing an empty pan. You
can assume that there is an integer that can be put in that spot to make the puzzle balance,
and your code must compute the value.

The ordering of the data file guarantees that when a beam is given, you can then determine
the left-right extent that it will take up and the scale at which you will need to draw it.
In particular, note that the scale factor required for each beam is based on the extents of
the things that hang from it, and the extent of a beam is based on the scale factor and the
extents of the things that hang from it. Weights (as in the problem solving) can be assumed
to have zero left-to-right extent.

Once you have read in the entire puzzle and computed the scale for each beam, your code
should open a turtle window and draw the balance puzzle. This should be implemented as a
draw function within the Beam class (perhaps with a small external helper function), rather
than external to the class. You can use the turtle.write function to write the values of the
weights | you may need to play around a little with turtle motions to get the text to appear
where you want it. The actual drawing should be done simply by calling draw on beam B,
which will then call the draw function on those things hanging from it, and so on. Make sure
that you get your preconditions and postconditions correct for all drawing functions!
