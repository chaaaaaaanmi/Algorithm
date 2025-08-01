import java.io.*;
import java.util.*;

public class Main {

    static int[][] miro;

    // 상 우 하 좌
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static int[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        miro = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                miro[i][j] = line.charAt(j) - '0';
            }
        }

        visited = new int[n][m];

        bfs(0, 0, n, m);
        System.out.println(visited[n-1][m-1]);
    }

    static void bfs(int start_r, int start_c, int n, int m) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{start_r, start_c});
        visited[start_r][start_c] = 1;

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int r = temp[0];
            int c = temp[1];

            // 종료 조건
            if (r == n-1 && c == m-1) {
                break;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                // 범위 체크
                if (0 <= nr && nr < n && 0 <= nc && nc < m) {
                    // 이동 가능한 칸인지, 방문한 적 있는지
                    if (miro[nr][nc] == 1 && visited[nr][nc] == 0) {
                        q.offer(new int[]{nr, nc});
                        visited[nr][nc] = visited[r][c] + 1;
                    }
                }
            }
        }
    }
}