
import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N 사람 수, J 김지민 위치, H 임한수 위치
        int N = Integer.parseInt(st.nextToken());
        int J = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        // 몇 라운드에서 J, H 대결 하는가
        int answer = 0;

        // J, H 위치가 같으면 게임 종료
        while (J != H) {
            J = (J + 1) / 2;
            H = (H + 1) / 2;
            answer++;
        }
        System.out.println(answer);
    }
}