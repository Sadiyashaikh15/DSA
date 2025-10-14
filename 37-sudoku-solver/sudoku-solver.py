class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and find empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def get_candidates(r, c):
            """Return possible valid digits for this cell."""
            box_index = (r // 3) * 3 + (c // 3)
            return {str(d) for d in range(1, 10)} - rows[r] - cols[c] - boxes[box_index]

        def solve():
            if not empties:
                return True

            # Pick the cell with the fewest possibilities (MRV heuristic)
            empties.sort(key=lambda pos: len(get_candidates(*pos)))
            r, c = empties.pop(0)

            box_index = (r // 3) * 3 + (c // 3)
            for ch in get_candidates(r, c):
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box_index].add(ch)

                if solve():
                    return True

                # Backtrack
                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[box_index].remove(ch)

            # Put cell back if not solved
            empties.insert(0, (r, c))
            return False

        solve()