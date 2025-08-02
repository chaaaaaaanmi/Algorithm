import java.io.*;
import java.util.*;

public class Main {

    static int[][] tomato;
    static int[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        tomato = new int[m][n];
        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                tomato[i][j] = Integer.parseInt(line[j]);
            }
        }

        visited = new int[m][n];
        bfs(n, m);
        int max = 0;
        boolean notTomato = false;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0) {
                    notTomato = true;
                }
                max = Math.max(max, visited[i][j]);
            }
        }
        if (notTomato) {
            System.out.println(-1);
        }
        else {
            System.out.println(max - 1);
        }
    }

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static void bfs(int n, int m) {
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 익은 토마토 q에 넣기
                if (tomato[i][j] == 1) {
                    q.offer(new int[]{i, j});
                    visited[i][j] = 1;
                }
                // 빈 칸도 방문한 척
                if (tomato[i][j] == -1) {
                    visited[i][j] = 1;
                }
            }
        }

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] temp = q.poll();
                int r = temp[0];
                int c = temp[1];

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    // 범위 체크
                    if (0 <= nr && nr < m && 0 <= nc && nc < n) {
                        if (visited[nr][nc] == 0) {
                            visited[nr][nc] = visited[r][c] + 1;
                            q.offer(new int[]{nr, nc});
                        }
                    }
                }
            }
        }
    }
}