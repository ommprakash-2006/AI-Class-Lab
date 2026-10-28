# AI-Class-Lab
### <b>ARTIFICIAL INTELLIGENCE - LABORATORY</b>
This repository is for LAB purposes only. (COLLEGE work)

<hr>

## **1. Write a program to implement BFS**

**AIM :** To implement BFS using Python.

**Theory :** Provide the concept, working principle, algorithm & applications before performing the experiment.

**Algorithm :**

1. Start
2. Accept input
3. Execute the logic
4. Display the result
5. Stop

<hr>

## **2. Write a program to implement DFS**

**AIM :** To implement DFS using Python.

**Theory :** Provide the concept, working principle, algorithm & applications before performing the experiment.

**Algorithm :**

1. Start
2. Accept input
3. Execute the logic
4. Display the result
5. Stop

<hr>

## **3. Hill Climbing Algorithm**

Hill climbing is the local search algorithm that repeatately moves to the neighbouring state with the highest value until no better neighbour exists.

**AIM:** To implement hill climbing algorithm using python.

**Theory:** Provide the concept, working principle, algorithm & applications before performing the experiment.

**Algorithm:**

1. Start
2. Accept input as Current State
3. Evaluate the objective function.
4. Generate neighbouring states.
5. Compare the neighbours with the current state.
6. Move to the neighbour with the highest value.
7. Repeat until no better neighbour exists or maximum iterations are reached.
8. Display the best solution.
9. Stop

<hr>

## **4. A * Algorithm**

It is a path finding algorithm that finds the shortest and the most efficent path from a start node to a goal node by using

g(n) - the actual cost from the start node to the current node

h(n) - the estimated cost from the current node to the goal (heuristic)

It chooses the node with the lowest total cost, calculated as **f(n) = g(n) + h(n)**

f(n) is total estimated cost

g(n) is actual cost so far

h(n) is estimated cost

"**Definition -** A* search is an informed search algorithm that finds the shortest path by combining the actual cost from the start node and the estimated cost to the goal."

<hr>

## **5. Min-Max Algorithm**

**AIM:**
To implement  Min-Max Algorithm using Python.

**Theory:**
It is a recursive search algorithm that chooses the optimal move for a player by assuming that the opponent will also play optimally. It aims to maximize the player's minimum guaranteed patoff while minimizing the opponent's maximum advantage.<br>
.....

**How it works:**

MAX player: Tries to choose the move with the highest possible score.<br>
MIN player: Tries to choose the move with the lowest possible score.<br>
.....

Example:

In a game Tic-Tac-Toe:<br>
The AI (MAX) examines all possible moves.<br>
It assumes the opponent (MIN) always make the best counter-move.<br>

**Definition:**

Min-Max is an AI search algorithm used in 2 player games that finds best move by maximizing the player's minimum gain while assuming the opponent always plays optimally.

<hr>

## **6. Alpha Beta Pruning**

**AIM:** <br>
To implement the Alpha-Beta Pruning algorithm using Python.

**Theory:** <br>
Alpha-Beta Pruning is an optimization of the Min-Max algorithm used in two-player games.

It avoids checking branches that cannot affect the final result, making Min-Max faster.
- Alpha (α): Best value found so far for MAX.
- Beta (β): Best value found so far for MIN.
- When α ≥ β, the remaining branch is pruned (not checked).

**Algorithm:** <br>
1. Start.
2. Set alpha = -∞ and beta = +∞.
3. If a leaf node is reached, return its value.
4. If it is MAX's turn:
    - Find the maximum value.
    - Update alpha.

5. If it is MIN's turn:
    - Find the minimum value.
    - Update beta.

6. If alpha >= beta, stop checking the remaining nodes (prune).
7. Return the optimal value.
8. Stop.

<hr>

## **7. 8-Queens Problem**

**AIM:** <br>
To implement 9-queens problem using Python using the backtracking technique and find a valid arrangement of 8 queens on an 8x8 chessboard such that no 2 queens attack each other.

**Problem Statement:** <br>
The 8 queens problem is the problem of placing 8 queens on an 8x8 chessboard such that no queens can attack each other.<br>
A queen can attack another queen if they are in same:<br>
Row, Column, Diagonal

**Theory:** <br>
Introduction - The 8 queens problem is a famous problem in AI and Computer Science. It is commonly used to demonstrate state-space search, constraints satisfaction and backtracking.

**Working Principle:** <br>
1. Start with an empty 8x8 chessboard
2. Begin from the first row
3. Try placing a queen in each column of the current row
4. Check whether position is safe
5. If the position is safe place the queen
6. Move to the next row
7. If no  safe position is available in the next row, remove the previously placed queen
8. Try another position for that queen
9. Continue until all 8 queens are successfully placed 

**Algorithm:** <br>
1. Start
2. Create an empty 8x8 chessboard
3. Try plaCING QUEENS from the first row
4. For each column in the curent row: <br>
Check whwther placing a queen is safe. <br>
Check the column. <br>
Check the upper-left diagonal. <br>
Check the upper-right diagonal. <br>
5. If the position is safe, place the queen.
6. Recursively move to the next row.
7. If all 8 rpws are successfully filled, display the board.
8. If no safe position is available: <br>
Remove the previously placed queen. <br>
Go back to previous row. <br>
Try another position. <br>
9. Repeat until a solution is found.
10. Stop

<hr>

## **8. Water-Jug Problem**

**AIM:** <br>
To implement the Water Jug Problem using Python and find a sequence of steps to obtain the required amount of water.

**Theory:** <br>
The Water Jug Problem is a classic AI search problem. We are given two jugs with fixed capacities and no measuring scale. The goal is to measure a specific amount of water by performing operations such as:
- Fill a jug completely.
- Empty a jug.
- Pour water from one jug into another.
The problem can be solved using BFS (Breadth-First Search) by treating each possible water level as a state.

**Algorithm:** <br>
1. Start with both jugs empty.
2. Represent the state as (jug1, jug2).
3. Add the starting state to a queue.
4. Generate possible states by: 
    - Filling either jug.
    - Emptying either jug.
    - Pouring one jug into the other.
5. Mark each new state as visited.
6. Repeat until the required amount is obtained.
7. Print the steps.
8. Stop.

<hr>

## **9. Tic-Tac-Toe Game**

**AIM:** <br>
To design and implement a Tic-Tac-Toe game using Python, where two players can play alternately by placing X and O on a 3 × 3 game board, and the program determines the winner or draw.

**Theory:** <br>
Tic-Tac-Toe is a simple two-player strategy game played on a 3 × 3 grid. One player uses X and the other uses O. Players take turns placing their symbol in an empty position on the board.

**Working Principle:** <br>
The main objective is to get three same symbols in a row, either:
- Horizontally
- Vertically
- Diagonally
The program checks the board after every move to determine whether a player has won. If all nine positions are filled and no player has won, the game is declared a draw.

In Python, the game can be implemented using a list to store the board, loops to control the turns, and conditional statements to check the winning conditions.

**Algorithm:** <br>
1. Create a 3 × 3 empty board.
2. Display the board.
3. Ask the player to enter a position.
4. Place X or O in the selected position.
5. Check for a winning combination.
6. If a player wins, display the winner.
7. If all positions are filled, declare a draw.
8. Otherwise, switch the player and repeat.
9. Stop.

<hr>

## **10. Travelling Salesman Problem (TSP)**

**AIM:** <br>
To implement the Travelling Salesman Problem (TSP) using Python and find the minimum-cost route for visiting all cities exactly once and returning to the starting city.

**Theory:** <br>
The Travelling Salesman Problem is a common optimization problem in Artificial Intelligence. A salesman has to visit a number of cities, visiting each city exactly once, and finally return to the starting city.

The objective is to find the shortest possible route with minimum total travel cost.

For a small number of cities, TSP can be solved using Brute Force, where all possible routes are checked and the route with the minimum cost is selected.

**Algorithm:** <br>
1. Start.
2. Take the number of cities and their distance matrix.
3. Generate all possible routes starting from the first city.
4. Calculate the total cost of each route.
5. Add the cost of returning to the starting city.
6. Select the route with the minimum cost.
7. Display the best route and its cost.
8. Stop.

<hr>
