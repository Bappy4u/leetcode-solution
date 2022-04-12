class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        res = []
        rlen = len(board[0])
        
        # this functiona is to count all the neighbours who is live(1)
        def countLive(i, j):
            live = 0
            if i>0:
                if board[i-1][j]==1:
                    live +=1
                if j>0 and board[i-1][j-1]==1:
                    live +=1
                if j<rlen-1 and board[i-1][j+1]==1:
                    live +=1
            if i<len(board)-1:
                if board[i+1][j]==1:
                    live +=1
                if j>0 and board[i+1][j-1]==1:
                    live +=1
                if j<rlen-1 and board[i+1][j+1]==1:
                    live +=1

            if j>0 and board[i][j-1]==1:
                live +=1
            if j<rlen-1 and board[i][j+1]==1:
                live +=1
            return live
        
        # the condition for live or dead
        for i,b in enumerate(board):
            for j,v in enumerate(b):
                live = countLive(i, j)
                dead = 0
                if v==0 and live==3:
                    res.append(1)
                elif v==0:
                    res.append(0)
                else:
                    if live<2:
                        res.append(0)
                    elif live<4:
                        res.append(1)
                    else:
                        res.append(0)
                        
        # To replace the res value into the board                
        l, r = 0, rlen # length of a m
        for b in board:
            b[:]=res[l:r]
            l = r
            r +=rlen
                    
   
                    
                