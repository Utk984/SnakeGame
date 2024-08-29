# 🐍 SnakeGame 🐍

Plaksha University Semester V (Monsoon 2024)
AI3022 Search Methods in AI - Professor Deepak Khemani

## ISSUES
- [ ] User args to define snake pos and game pos
- [ ] Snake starts at length 0, can start from length 3 or 4
- [x] If you go back into the snake, the snake dies
- [x] If you go off the board, the snake pops from other side (can change that)
- [x] No MoveGen or goaltest functions
- [x] No documentation of our work

## Assignment 1 
### Part 1
Choose a new problem that can be posed as a state space search problem.

    Design a domain representation for the state to facilitate defining the following:

    Devise a MoveGen or a neighbourhood function to take a given state as an argument and return the set of neighbouring states. Eliminate states that do not respect the domain constraints. For example, the lion should not be left alone with the goat in the MGLC problem.

    Devise a GoalTest function that accepts a state as input and returns true if the state is a goal state, and false otherwise.

Think about how a user can be allowed to specify the start state. For example, a state in an instance of a water jug problem with the jug sizes and contents being user-defined. Also, how can a user specify the goal state. For example, how much water is to be measured.

Submit a short description of your problem and the representation scheme.

Credit will be assigned for choosing a new and interesting domain. Do not choose examples used in the class or commonly found in textbooks.

The assignment has to be done in groups of 2. Only 1 member from each group needs to submit the assignment.

### Part 2
For your chosen problem in part 1

    implement the Depth First Search Algorithm
    implement the Breadth First Search Algorithm
    define a heuristic function and implement the Best First Search Algorithm

Submit your code by the due date (no extensions). Along with the code, submit a small report describing your implementation and also performance of the three programs on the same problem, or a set of problems. Program demonstrations may be scheduled in due course

