import numpy as np

class Cell():
    def __init__(self,x,y,puzzle):
        self.forbidden = []
        self.x = x
        self.y = y
        self.puzzle = puzzle
           
    def forbidden_list(self,puzzle):
        self.puzzle = puzzle
        rr, cc = (self.x // 3) * 3, (self.y // 3) * 3   
        self.forbidden =  ({self.puzzle[self.x][c] for c in range(9)} | {self.puzzle[r][self.y] for r in range(9)} | {self.puzzle[rr+r][cc+c] for r in range(3) for c in range(3)})  
        
    def add_to_forbidden(self,add):
        self.forbidden = (self.forbidden | {add})


def sudoku(puzzle):
    cells = np.zeros([9,9]).tolist()

    #df = pd.DataFrame
    ns = []
    ms = []
    for n in range(9):
        for m in range(9):
            if puzzle[n][m] == 0:
                ns.append(n)
                ms.append(m)
                cells[n][m] = (Cell(n,m,puzzle))
    x = 0
    while x<len(ns)+1:
        if len(cells[ns[x]][ms[x]].forbidden) == 0:
            cells[ns[x]][ms[x]].forbidden_list(puzzle)
        
        allowed = {1,2,3,4,5,6,7,8,9} - cells[ns[x]][ms[x]].forbidden
        #print(allowed)
        #backtrack
        if len(allowed) == 0:
            puzzle[ns[x-1]][ms[x-1]] = 0
            x = x-1            
        else:     
            cell = min(allowed)
            puzzle[ns[x]][ms[x]]  = cell
            cells[ns[x]][ms[x]].add_to_forbidden(cell)
            if x == len(ns)-1:
                print(puzzle)
                return(puzzle)
            x = x+1
            cells[ns[x]][ms[x]].forbidden_list(puzzle)
