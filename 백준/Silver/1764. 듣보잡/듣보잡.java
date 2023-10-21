import java.io.*;
import java.util.*;


public class Main {
    static int n;
    static int m;
    static HashMap<String,Boolean> noListen;
    static ArrayList<String> result;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n = 듣도 못한 사람
        // m = 보도 못한 사람
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        noListen = new HashMap<>();
        result = new ArrayList<>();
        // 사전 순으로 겹치는 사람을 가져온다.
        for (int i=0; i<n; i++) {
            noListen.put(new StringTokenizer(br.readLine()).nextToken(), true);
        }
        for (int j=0; j<m; j++) {
            String value = new StringTokenizer(br.readLine()).nextToken();
            try {
                if (noListen.get(value)) {
                    result.add(value);
                }
            } catch(Exception e) {
                continue;
            }

        }

        Collections.sort(result);
        System.out.println(result.size());
        for(String re:result) {
            System.out.println(re);
        }

    }
}