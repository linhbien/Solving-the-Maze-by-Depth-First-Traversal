from typing import List
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        m = len(maze)
        n = len(maze[0])
        stack = []
        seen = set()
        stack.append((start[0], start[1]))
        seen.add((start[0], start[1]))
        while stack:
            curr_i, curr_j = stack.pop()
            for d in directions:
                i = curr_i
                j = curr_j
                while 0 <= i < m and 0 <= j < n and maze[i][j] ==0:
                    i += d[0]
                    j += d[1]
                i -= d[0]
                j -= d[1]
                if i == destination[0] and j == destination[1]:
                    return True
                if (i,j) not in seen:
                    stack.append((i,j))
                    seen.add((i,j))
        return False

def main():
    test = Solution()
    print("Input: [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]")
    print("Output: ",test.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4]))

    print("Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]")
    print("Output: ",test.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4],[3,2]))

    print("Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]")
    print("Output: ",test.hasPath([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],[4,3],[0,1]))
main()