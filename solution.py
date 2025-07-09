def solution(board):
    R, C = len(board), len(board[0])

    def in_bounds(r, c):
        return 0 <= r < R and 0 <= c < C

    def iter():
        board_changed = False
        explosions = []

        for r in range(R - 2, -1, -1):
            for c in range(C):
                if board[r][c] != '#' or board[r + 1][c] == '#':
                    continue

                board_changed = True
                board[r][c] = '-'

                if board[r + 1][c] == '-':
                    board[r + 1][c] = '#'
                else:
                    explosions.append((r + 1, c))

        for r, c in explosions:
            for r, c in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1), (r + 1, c), (r + 1, c - 1), (r, c - 1)]:
                if in_bounds(r, c) and board[r][c] == '#':
                    board[r][c] = '-'

        if board_changed:
            iter()

    iter()

    return board
