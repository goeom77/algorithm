import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

//        정점 개수 n, 간선 개수 m, 시작 정점 v
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        boolean[][] graph = new boolean[n+1][n+1];
        for (int i=0; i <m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = true;
            graph[b][a] = true;
        }

        boolean[] log = new boolean[n+1];
        Stack<Integer> stack = new Stack<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.add(v);


        // 기본값 설정
        String result = v + " ";
        log[v] = true;
        stack.push(v);
        // DFS
        while (!stack.empty()) {
            int tmp = stack.pop();
            if (!log[tmp]) {
                result += tmp + " ";
                log[tmp] = true;
            }
            for(int i=0; i<=n; i++) {
                if (graph[tmp][i] && !log[i]) {
                    stack.push(tmp);
                    stack.push(i);
                    break;
                }
            }
        }
        System.out.println(result);
        // 기본값 재설정
        result = v + " ";
        log = new boolean[n+1];
        log[v] = true;
        // BFS
        while (!queue.isEmpty()){
            int tmp = queue.poll();
            if (!log[tmp]) {
                result += tmp + " ";
                log[tmp] = true;
            }
            for(int i=0; i<=n; i++) {
                if (graph[tmp][i] && !log[i]) {
                    queue.add(i);
               }
            }
        }
        System.out.println(result);
    }

}