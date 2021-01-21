# madfibonacci
Coursework Instructions
In a Crazynacci Sequence, every number is the sum of the three previous ones. However, the sequence resets every time the resulting number is lower than -125. When that
happens, the current element is i + 10, where i is the number of times the sequence was
reset.
We will start the sequence with 0, -1, -2. For example:
0, -1, -2, -3, -6, -11, -20, -37, -68, -125, 11, 12, -102, -79, 13, 14, -52, ...
• Write an iterative function crazyIter(x) that, given a number (positive integer) x,
prints in order the xth first numbers in the Crazynacci Sequence.
Every number must be followed by a comma, except for the last one. (1%)
• Write a recursive solution crazyRecur(x) that, given a number (positive integer) x,
prints in order the xth first numbers in the Crazynacci Sequence.
Every number must be followed by a comma, except for the last one.
Important! In order to enforce a recursive solution, the code must not contain any
loops. That is, the “for” and the “while” commands are not going to be accepted.
Also note that solutions that are too inefficient are not going to be accepted, as it
will time out in large test cases.
Hint 1: The crazyRecur(x) function, by itself, does not have to be recursive. It can
call a second function, which contains the recursive code.
Hint 2: Use a different idea than the one applied in the Fibonacci example.
