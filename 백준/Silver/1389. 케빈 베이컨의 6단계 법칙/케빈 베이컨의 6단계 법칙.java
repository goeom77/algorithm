import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
//        케빈 베이컨의 6단계 법칙
//        모든 사람은 6단계 이내 아는사람이다. 두사람이 몇 단계에 이어질수 있는지 계산
//        케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램
//        1-3, 1-4, 2-3, 3-4, 4-5
//        1 -> 2 (1-3-2) 2, 1 -> 3 (1-3) 1, 1 -> 4 (1-4) 1, 1 -> 5 (1-4-5) 2 => 2+1+1+2 = 6
//        답은 복수일 수 있다. -> 번호가 가장 작은 사람이 답
//        n, m 100, 5000 (m개 줄에 연결 정보 줌)
//
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>(101);
        for (int i = 0; i<n+1 ; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        int result = 101;
        int result_value = Integer.MAX_VALUE;
        for (int i = 1; i<n+1 ; i++) {
//            i 가 1부터 최소인 값을 알기
            boolean[] visit = new boolean[n+1];
            Integer[] visit_sum = new Integer[n+1];
            Queue<Integer> queue = new LinkedList<>();
//            연결된것 부터 1로 넣고 1연결된것으로부터 2, 3, 찾기
            graph.get(i).forEach((e) -> {
                visit[e] = true;
                visit_sum[e] = 1;
                queue.add(e);
            });
            visit_sum[i] = 0;
            visit[i] = true;
            while (!queue.isEmpty()) {
                int tmp = queue.poll();
                graph.get(tmp).forEach((e) -> {
                    if(!visit[e]) {
                        visit[e] = true;
                        visit_sum[e] = visit_sum[tmp]+1;
                        queue.add(e);
                    }
                });
            }
            Integer tmp_result_sum = 0;
            for(int k=1;k<n+1;k++) {
                tmp_result_sum += visit_sum[k];
            }
            if(result_value > tmp_result_sum) {
                result = i;
                result_value = tmp_result_sum;
            }
        }


        System.out.println(result);
    }
}