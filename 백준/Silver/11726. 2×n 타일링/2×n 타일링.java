import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] array = new int[1001];
        array[1] = 1;
        array[2] = 2;
        array[3] = 3;
        array[4] = 5;
        array[5] = 8;
        for (int i=6; i<=n; i++) {
            array[i] = (array[i-1]+array[i-2] ) % 10007;
        }
        System.out.println(array[n]);

    }
}