import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int s;
    static int result;
    static int[] list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        result = 0;
        // n = number of vertices
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        list = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            list[i] = Integer.parseInt(st.nextToken());
        }

        // list의 부분수열의 합이 s가 되는 경우의 수를 구하시오.
        // 우선 list의 부분수열을 모두 구한다.
        dfs(0,0);
        // 공집합 제거
        if(s == 0) {
            result--;
        }
        System.out.println(result);


    }
    private static void dfs(int index, int sum) {

        if(index == n) {
            if(sum == s) {
                result++;
            }
            return;
        }
        dfs(index+1, sum+list[index]);
        dfs(index+1, sum);
    }
}