import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n, m이 공백으로 구분되어 입력됨 가로 세로 의미
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        // 2차원 배열 선언
        int[][] arr = new int[n][m];
        // 8*8 크기의 체스판을 만들어야 하므로 2차원 배열을 8*8 크기로 잘라서 저장할 배열 선언
        int[][] chess = new int[8][8];
        // chess를 1과 0으로 번갈아가면서 저장
        for(int i=0; i<8; i++) {
            for(int j=0; j<8; j++) {
                chess[i][j] = (i+j) % 2;
            }
        }
        // 2차원 배열 입력받기
        for(int i=0; i<n; i++) {
            String str = br.readLine();
            for(int j=0; j<m; j++) {
                arr[i][j] = str.charAt(j) == 'W' ? 0 : 1;
            }
        }
        int result = 64;
        // result가 64보다 작을 때, 체스판이 WB 교차로 바뀌는 개수를 체크해서 result에 저장
        for(int i=0; i<=n-8; i++) {
            for(int j=0; j<=m-8; j++) {
                int cnt1 = 0;
                int cnt2 = 0;
                // arr[i][j]가 0일때와 1일때 두가지 경우로 나눠서 체크
                for(int k=i; k<i+8; k++) {
                    for(int l=j; l<j+8; l++) {
                        if(arr[k][l] == chess[k-i][l-j]) cnt1++;
                        if(arr[k][l] != chess[k-i][l-j]) cnt2++;
                    }
                }

                result = Math.min(result, Math.min(cnt1, cnt2));
            }
        }
        System.out.println(result);
    }
}