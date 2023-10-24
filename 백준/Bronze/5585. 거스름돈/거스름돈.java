import java.io.*;
import java.util.*;


public class Main {
    static int n;
    static int remainN;
    static int total;
    static int[] coins = {500,100,50,10,5,1};
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        remainN = 1000 - n;
        for (int i=0; i<6; i++) {
            if (remainN ==0) break;
            int tmp = (int) (remainN / coins[i]);
            if (tmp >0) {
                total += tmp;
                remainN -= (coins[i]*tmp);
            }
        }
        bw.write(String.valueOf(total));
        bw.flush();
        bw.close();
    }
}