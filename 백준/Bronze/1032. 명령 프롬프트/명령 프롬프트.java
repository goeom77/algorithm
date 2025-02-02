import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // a_z . ? 만 나올 때 모두 나오게 하는 방법
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N-1];
        String answer = br.readLine();
        char[] answerArr = answer.toCharArray();
        for (int i = 0; i < N-1; i++) {
            words[i] = br.readLine();
        }

        for (String word : words) {
            char[] wordArr = word.toCharArray();
            for (int i = 0; i < wordArr.length; i++) {
                if (answerArr[i] == '?') {
                    continue;
                }
                else if (wordArr[i] == answerArr[i]) {
                    continue;
                }
                else {
                    answerArr[i] = '?';
                }
            }
        }
        for (int i = 0; i < answerArr.length; i++) {
            System.out.print(answerArr[i]);
            if (i == answerArr.length - 1) {
                System.out.println();
            }
        }

    }
}