from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 예외 처리: 시작점이나 끝점이 1이면 경로 없음
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        # 8방향 (상하좌우 + 대각선)
        dr = [0, 1, 1, 1, 0, -1, -1, -1]
        dc = [1, 1, 0, -1, -1, -1, 0, 1]

        # BFS 큐: (행, 열, 현재까지의 거리)
        queue = deque()
        queue.append((0, 0, 1))  # 시작 위치 (0, 0)에서 거리 1부터 시작

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while queue:
            cur_r, cur_c, dist = queue.popleft()

            # 도착 지점에 도달하면 거리 반환
            if cur_r == n - 1 and cur_c == n - 1:
                return dist

            # 8방향 탐색
            for i in range(8):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]

                if 0 <= next_r < n and 0 <= next_c < n:
                    if not visited[next_r][next_c] and grid[next_r][next_c] == 0:
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c, dist + 1))

        # 도달 못하면 -1
        return -1
