class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy==fy:
            return t!=1
        m = max(abs(fx-sx), abs(fy-sy))
        if t>=m:
            return True
        else:
            return False
