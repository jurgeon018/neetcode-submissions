class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for row_index in range(9):
            for col_index in range(9):
                num = board[row_index][col_index]
                
                if num == ".":
                    continue
                
                box_index = (row_index // 3) * 3 + (col_index // 3)
                
                # If number already exists in rows, cols, or box → invalid
                if (
                    num in rows[row_index] 
                    or num in cols[col_index] 
                    or num in boxes[box_index]
                ):
                    return False
                
                # Add the number to tracking sets
                rows[row_index].add(num)
                cols[col_index].add(num)
                boxes[box_index].add(num)
        
        return True

