import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int result;
    static boolean[][] graphA;
    static boolean[][] graphB;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        result = 0;
        // n = number of vertices
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graphA = new boolean[n][m];
        graphB = new boolean[n][m];
        for (int i=0; i<n; i++){
            char[] tmpChar = br.readLine().toCharArray();
            for (int j=0; j<m; j++) {
                graphA[i][j] = tmpChar[j] == '1';
            }

        }
        for (int i=0; i<n; i++) {
            char[] tmpChar = br.readLine().toCharArray();
            for (int j=0; j<m; j++) {
                graphB[i][j] = tmpChar[j] == '1';
            }
        }
        // A에서 B로 변환하는데 필요한 최소 연산 횟수를 구하기
        // 3*3 크기의 부분 그래프를 모두 뒤집는다.
        // 바꿀 수 없으면 -1을 출력
        for (int i=0; i<n-2; i++) {
            for (int j=0; j<m-2; j++) {
                if (graphA[i][j] != graphB[i][j]) {
                    flip(i, j);
                    result++;
                }
            }
            if (graphA[i][m-2] != graphB[i][m-2] || graphA[i][m-1] != graphB[i][m-1]) {
                break;
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (graphA[i][j] != graphB[i][j]) {
                    result = -1;
                    break;
                }
            }
        }
        System.out.println(result);
    }
    private static void flip(int x, int y) {
        for (int i=x; i<x+3; i++) {
            for (int j=y; j<y+3; j++) {
                graphA[i][j] = !graphA[i][j];
            }
        }
    }

}