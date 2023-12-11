import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static String[] memory;
    static int result;
    static boolean[] alphabet = new boolean[26];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        result = 0;
        // n = number of vertices
        n = Integer.parseInt(st.nextToken());
        memory = new String[n];
        for (int i = 0; i < n; i++) {
            memory[i] = br.readLine();
        }
        for(String word : memory){
            // split한 대문자를 왼쪽부터 오른쪽으로 확인해보고 alphabet에 체크되어있지 않으면 []감싼다음 출력
            if( word == null) {
                System.out.println();
                continue;
            }
            String[] tmp = word.split(" ");
            StringBuilder tmp2 = new StringBuilder();
            // 첫글자를 []로 감싸고 나머지는 그대로 출력
            boolean flag = true;
            for(String s : tmp){

                if (!flag) {
                    tmp2.append(s).append(" ");
                    continue;
                }
                if(!alphabet[s.toLowerCase().charAt(0)-'a']){
                    alphabet[s.toLowerCase().charAt(0)-'a'] = true;
                    tmp2.append("[").append(s.charAt(0)).append("]").append(s.substring(1)).append(" ");
                    flag = false;
                }else{
                    tmp2.append(s).append(" ");
                }
            }
            // 첫글자로 해결되지 않는 경우
            if(flag) {
                tmp2 = new StringBuilder();
                int editIdx = 0;
                for (int i=0; i < word.length(); i++) {
                    if(word.charAt(i) == ' ') continue;
                    if(!alphabet[word.toLowerCase().charAt(i) - 'a']) {
                        editIdx = i;
                        alphabet[word.toLowerCase().charAt(i) - 'a'] = true;
                        break;
                    }
                }

                for (int i=0; i<word.length(); i++) {
                    if(editIdx == 0) {
                        tmp2.append(word.charAt(i));
                        continue;
                    }
                    if (i == editIdx) {
                        tmp2.append("[").append(word.charAt(i)).append("]");
                    } else {
                        tmp2.append(word.charAt(i));
                    }
                }
            }
            System.out.println(tmp2);
        }

    }


}