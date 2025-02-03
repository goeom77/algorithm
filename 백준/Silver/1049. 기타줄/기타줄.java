
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        // N개의 기타줄, M개의 브랜드 기타줄
        // 6개씩 가격, 낱개 가격
        int minSet = 1000;
        int minOne = 1000;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            minSet = Math.min(minSet, Integer.parseInt(st.nextToken()));
            minOne = Math.min(minOne, Integer.parseInt(st.nextToken()));
        }
        int answer = 0;
        // 1. 6개 가격이 낱개 가격보다 싸다면
        if (minSet < minOne * 6) {
            answer += (N / 6) * minSet;
        } else {
            answer += (N / 6) * minOne * 6;
        }
        // 2. 낱개로 살 때 낱개 가격이 6개보다 싸다면
        if (minOne * (N % 6) < minSet) {
            answer += minOne * (N % 6);
        } else {
            answer += minSet;
        }
        System.out.println(answer);
    }
}