import numpy as np

def initiateBoard(arr):
    for i in range(len(arr)):
        row = "|";
        for y in range(len(arr[i])):
            value = arr[i][y] if arr[i][y] > 10 else " "
            row += str(value) + "|";
            # print(arr[i][y]);
        print(row)
        print("=======")


arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
x, y = np.shape(arr);
totalCell = x * y;
filledCell = 0;
turn = 0;
while filledCell < totalCell:
    initiateBoard(arr);
    currPlayer = 1 if (turn % 2) else 2;
    answer = input("Where do you wanna go? player " + str(currPlayer) + "\n")
    # print(answer);
    x, y = answer;
    x = x - 1;
    y = y - 1;
    print(x, y)
    arr[x, y] = 11 if currPlayer == 1 else 22;
    turn = turn + 1;