import java.util.*;
import java.io.*;

public class Main {
    

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] arr = new int[n];
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < n; i += 1) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i += 1) {
            for (int j = 0; j < n; j += 1) {
                if (i == j) continue;

                int sum = 0;
                for (int k = 0; k < n; k += 1) {
                    if (k == i || k == j) continue;

                    sum += arr[k];
                }

                min = Math.min(min, Math.abs(sum - s));
            }
        }

        System.out.println(min);
    }
}