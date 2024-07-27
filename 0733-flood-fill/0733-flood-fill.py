class Solution:
    def floodFill(self, img : List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        n,m = len(img),len(img[0])
        incolor = img[sr][sc]

        def fun(r,c):
            if r < 0 or r >= n: return
            if c < 0 or c >= m : return 

            if img[r][c] == color: return
            if img[r][c] != incolor: return

            img[r][c] = color

            fun(r-1,c)
            fun(r+1,c)
            fun(r,c+1)
            fun(r,c-1)
        fun(sr,sc)

        return img
        


        