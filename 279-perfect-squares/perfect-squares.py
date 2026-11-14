class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, n + 1):
            square = i**2
            if square > n:
                break
            squares.append(square)

        min_squares = [float('inf')] * (n + 1)
        min_squares[0] = 0

        for w in range(1, n + 1):
            for sq in squares:
                if w - sq >= 0:
                    min_squares[w] = min(min_squares[w], min_squares[w - sq] + 1)

        return min_squares[n]