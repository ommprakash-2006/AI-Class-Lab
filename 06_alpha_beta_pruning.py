 
# alpha beta pruning function
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    # Base case: Leaf node reached
    if depth == height:
        return values[nodeIndex]
    if maximizingPlayer:
        best = float('-inf')    # -math.inf

        for i in range(2):
            value = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)

            # beta cut-off
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')     # math.inf

        for i in range(2):
            value = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)

            # alpha cut-off
            if beta <= alpha:
                break
        return best

# main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))
height = 3
result = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), height)
print("\nThe optimal value is:", result)


'''
Output:

Enter 8 leaf node values: 8 6 7 3 5 4 2 1

The optimal value is: 7
'''
