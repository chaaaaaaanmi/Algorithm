import java.io.*;

public class Main {

    static int n;
    static int s;
    static int[] arr;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        s = Integer.parseInt(input[1]);

        String[] nums = br.readLine().split(" ");
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(nums[i]);
        }

        count = 0;
        solve(0, 0, 0);
        System.out.println(count);
    }

    static void solve(int idx, int sum, int selected) {

        if (idx == n) {
            if (sum == s && selected > 0) {
                count++;
            }
            return;
        }

        // 현재 원소 포함 O
        solve(idx + 1, sum + arr[idx], selected + 1);
        // 현재 원소 포함 X
        solve(idx + 1, sum, selected);
    }
}