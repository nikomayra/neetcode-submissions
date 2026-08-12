class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate_digits(digits: List[str]):
            hash_map = {key: 0 for key in ["1","2","3","4","5","6","7","8","9"]}
            for digit in digits:
                if digit == ".": continue
                if hash_map.get(digit,1) == 0:
                    hash_map[digit] += 1
                else:
                    return False
            return True

        rows = board
        cols = []
        for c in range(9):
            col = []
            for r in range(9):
                col.append(board[r][c])
            cols.append(col)

        zones = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                zone_idx = (r // 3) * 3 + (c // 3)
                zones[zone_idx].append(board[r][c])

        # Validate rows
        for row in rows:
            if not validate_digits(row):
                return False 

        # Validate cols
        for col in cols:
            if not validate_digits(col):
                return False 
        
        # Validate 3x3 zones
        for zone in zones:
            if not validate_digits(zone):
                return False 

        return True