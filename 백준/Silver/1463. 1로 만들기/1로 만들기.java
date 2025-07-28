import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[1000001];
        // dp 초기값 설정
        dp[2] = 1;
        dp[3] = 1;

        for (int i = 4; i < 1000001; i++) {
            dp[i] = 1 + dp[i-1];

            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i], 1 + dp[i/3]);
            }

            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i], 1 + dp[i/2]);
            }
        }

        System.out.println(dp[n]);
    }
}