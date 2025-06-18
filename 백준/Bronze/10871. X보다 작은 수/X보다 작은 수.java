import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int x = Integer.parseInt(input[1]);

        String[] arr = br.readLine().split(" ");

        for (int i = 0; i < n; i++) {
            if (Integer.parseInt(arr[i]) < x) {
                System.out.print(arr[i] + " ");
            }
        }
    }
}
