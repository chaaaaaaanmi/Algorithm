import java.io.*;
import java.util.*;

public class Main {

    static char[][] building;
    static boolean[][] visited;
    static String[] resultList;
    static int time;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        resultList = new String[tc]; // 출력값 모아둘 배열

        // 테케 시작
        for (int t = 0; t < tc; t++) {

            String[] s = br.readLine().split(" ");
            int w = Integer.parseInt(s[0]);
            int h = Integer.parseInt(s[1]);

            // building 입력 받기
            building = new char[h][w];
            for (int i = 0; i < h; i++) {
                String line = br.readLine();
                for (int j = 0; j < w; j++) {
                    building[i][j] = line.charAt(j);
                }
            }

            // 함수 호출
            String result = bfs(w, h);
            resultList[t] = result;
        }

        for (String s : resultList) {
            System.out.println(s);
        }
    }

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static String bfs(int w, int h) {
        Queue<int[]> fireQ = new LinkedList<>();
        Queue<int[]> sgQ = new LinkedList<>();

        // 변수 초기화
        visited = new boolean[h][w];
        time = 0;

        // 불, 상근이 좌표 찾기
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (building[i][j] == '*') {
                    fireQ.offer(new int[]{i, j});
                }
                if (building[i][j] == '@') {
                    sgQ.offer(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }

        while (!sgQ.isEmpty()) {
            time++;

            // 불 먼저
            int fireQSize = fireQ.size();
            for (int i = 0; i < fireQSize; i++) {
                int[] temp = fireQ.poll();
                int r = temp[0];
                int c = temp[1];

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    // 범위 체크
                    if (0 <= nr && nr < h && 0 <= nc && nc < w) {
                        // . 이거나 @
                        if (building[nr][nc] == '.' || building[nr][nc] == '@') {
                            building[nr][nc] = '*';
                            fireQ.offer(new int[]{nr, nc});
                        }
                    }
                }
            }

            // 상근이 이동
            int sgQSize = sgQ.size();
            for (int i = 0; i < sgQSize; i++) {
                int[] temp = sgQ.poll();
                int r = temp[0];
                int c = temp[1];

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    // 범위 체크
                    if (0 <= nr && nr < h && 0 <= nc && nc < w) {
                        // 빈 공간이고 방문한 적 없으면 갈 수 있다.
                        if (building[nr][nc] == '.' && !visited[nr][nc]) {
                            sgQ.offer(new int[]{nr, nc});
                            visited[nr][nc] = true;
                        }
                    }

                    // 범위를 벗어나면 탈출
                    else {
                        return String.valueOf(time);
                    }
                }
            }
        }

        return "IMPOSSIBLE";
    }
}