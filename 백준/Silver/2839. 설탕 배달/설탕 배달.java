import java.io.*;
import java.util.*;


public class Main {
    static int n;
    static int total;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int tmp = n / 5;
        while(true) {
            if(tmp < 0) {
                total = -1;
                break;
            }
            if ((n - 5 * tmp) % 3 == 0) {
                total = tmp + (n - 5 * tmp)/3;
                break;
            }
            tmp -= 1;
        }

        bw.write(String.valueOf(total));
        bw.flush();
        bw.close();
    }
}