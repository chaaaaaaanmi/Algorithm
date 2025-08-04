import java.io.*;

public class Main {

    static int n;
    static int[] T;
    static int[] P;
    static int maxMoney;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        T = new int[n];
        P = new int[n];

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            T[i] = Integer.parseInt(line[0]);
            P[i] = Integer.parseInt(line[1]);
        }

        maxMoney = 0;
        solve(0, 0);
        System.out.println(maxMoney);
    }

    static void solve(int day, int money) {

        // 최대 일수 도달하면 maxMoney 갱신
        if (day >= n) {
            maxMoney = Math.max(money, maxMoney);
            return;
        }

        // 상담 0
        if (day + T[day] <= n) {
            solve(day + T[day], money + P[day]);
        }

        // 상담 X
        solve(day + 1, money);
    }
}