import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Integer.max;
import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            int n = parseInt(br.readLine());
            int[][] student = new int[n][2];
            for (int j=0; j<n; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                student[j][0] = parseInt(st.nextToken());
                student[j][1] = parseInt(st.nextToken());
            }
            int visited = n+1;
            int result = 0;
            // int[][] 를 정렬하려면?

            Arrays.sort(student, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return Integer.compare(o1[0],o2[0]);
                }
            });
            // 1, 2열 두개다보다 작은 사람이 있다면 그사람을 빼고 모두 카운트해야한다.
            // 정렬한 순서로 가져오되, 2열이 앞사람보다 작다면? 그사람은 빼야한다.
            for (int[] value: student) {
                if (value[1] < visited) {
                    visited = value[1];
                    result += 1;
                }
            }
            System.out.println(result);

        }
    }
}