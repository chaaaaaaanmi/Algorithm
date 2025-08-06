import java.io.*;

public class Main {

    static int n;
    static int[] arr;
    static int[] op;

    static int max = -1000000000;
    static int min = 1000000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new int[n];
        String[] s = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        op = new int[4];
        String[] ss = br.readLine().split(" ");
        for (int i = 0; i < 4; i++) {
            op[i] = Integer.parseInt(ss[i]);
        }

        // arr의 첫 인덱스의 값은 sum에 미리 넣어두기
        // 그래서 시작도 index 1부터
        solve(1, arr[0]);
        System.out.println(max);
        System.out.println(min);
    }

    static void solve(int numIdx, int sum) {

        // 모든 수를 계산하면 최댓값, 최솟값 갱신
        if (numIdx == n) {
            max = Math.max(max, sum);
            min = Math.min(min, sum);
            return;
        }

        // 사용 가능한 연산자가 있으면 재귀
        for (int i = 0; i < 4; i++) {
            if (op[i] > 0) {
                op[i]--;
                solve(numIdx+1, calculator(numIdx, sum, i));
                // 사용했던거 복구
                op[i]++;
            }
        }
    }

    static int calculator (int numIdx, int sum, int opIdx) {

        if (opIdx == 0) {
            sum += arr[numIdx];
        }

        if (opIdx == 1) {
            sum -= arr[numIdx];
        }

        if (opIdx == 2) {
            sum *= arr[numIdx];
        }

        if (opIdx == 3) {
            if (sum < 0) {
                sum = -(-sum / arr[numIdx]);
            }
            else {
                sum /= arr[numIdx];
            }
        }

        return sum;
    }
}