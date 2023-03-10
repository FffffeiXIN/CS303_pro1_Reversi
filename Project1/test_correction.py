import ab5
import numpy as np

if __name__ == "__main__":
    chessboard = np.array([[0, -1, -1, -1, -1, -1, -1, 0],
                           [1, 1, 1, 1, 1, -1, -1, -1],
                           [0, 1, -1, 1, -1, 1, -1, -1],
                           [0, -1, 1, 1, 1, 1, -1, -1],
                           [0, -1, -1, 1, -1, 1, -1, -1],
                           [0, -1, 1, 1, -1, 1, -1, -1],
                           [0, -1, -1, 1, 1, 1, -1, -1],
                           [0, -1, -1, 1, 1, 1, -1, 0]])
    a = ab5.AI(8, -1, 10)
    a.go(chessboard)
    print(a.candidate_list)