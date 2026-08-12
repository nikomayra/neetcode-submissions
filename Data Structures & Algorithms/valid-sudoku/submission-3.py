class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # If one (or both?) central diagonal isn't consecutive but still valid does that mean all rows and columns would also be valid? probably not...
        # 49 -> 58
        # print(ord(board[0][0])- 48)
        # print(ord("9") - 48)

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
        cols = [list(col) for col in zip(*board)] # How to do this more native/explicit?
        zones = []
        for i in range(0, 9, 3):        # row band start: 0, 3, 6
            for j in range(0, 9, 3):    # col band start: 0, 3, 6
                zone = []
                for r in range(i, i + 3):
                    zone.extend(board[r][j:j+3])
                zones.append(zone)

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