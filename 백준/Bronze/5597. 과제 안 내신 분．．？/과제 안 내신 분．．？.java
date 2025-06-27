import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));

        HashSet<Integer> submit = new HashSet<>();
        for (int i = 0; i < 28; i++) {
            submit.add(Integer.parseInt(br.readLine()));
        }

        ArrayList<Integer> notSubmit = new ArrayList<>();
        for (int i = 1; i < 31; i++) {
            if (!submit.contains(i)) {
                notSubmit.add(i);
            }
        }

        System.out.println(notSubmit.get(0));
        System.out.println(notSubmit.get(1));
    }
}
