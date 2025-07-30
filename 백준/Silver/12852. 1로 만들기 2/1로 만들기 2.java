import java.io.*;
import java.util.*;

public class Main {

    public static Queue<Integer> q = new LinkedList<>();
    public static int[] dist; // 최소 연산 횟수
    public static int[] path; // 경로 추적
    public static boolean[] visited; // 방문 체크용

    public static void bfs(int start) {
        q.offer(start); // 시작점 큐에 넣어두기
        visited[start] = true; // 시작점 방문 체크

        while (!q.isEmpty()) {
            int node = q.poll();

            // 1이 되면 종료
            if (node == 1) {
                break;
            }

            int next = node - 1;
            if (next >= 1 && !visited[next]) {
                dist[next] = dist[node] + 1;
                path[next] = node;
                q.offer(next);
                visited[next] = true;
            }

            if (node % 3 == 0) {
                int next3 = node / 3;
                if (next3 >= 1 && !visited[next3]) {
                    dist[next3] = dist[node] + 1;
                    path[next3] = node;
                    q.offer(next3);
                    visited[next3] = true;
                }
            }

            if (node % 2 == 0) {
                int next2 = node / 2;
                if (next2 >= 1 && !visited[next2]) {
                    dist[next2] = dist[node] + 1;
                    path[next2] = node;
                    q.offer(next2);
                    visited[next2] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        dist = new int[n+1];
        path = new int[n+1];
        visited = new boolean[n+1];
        bfs(n);

        // 경로 역추적
        int current = 1;
        ArrayList<Integer> result = new ArrayList<>();

        while (current != 0) {
            result.add(current);
            current = path[current];
        }

        System.out.println(dist[1]);
        Collections.reverse(result);
        for (Integer i : result) {
            System.out.print(i + " ");
        }
    }
}