import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.math.BigInteger;


public class Main {
    private static String[] Add(String[] fArray, String val) {
        String[] aArray = new String[fArray.length + 1];
        for(int index = 0; index < fArray.length; index++) {
            aArray[index] = fArray[index];
        }
        aArray[fArray.length] = val;
        return aArray;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] answer = {};
//        n개 중 k개를 순서 없이 선택하는 방법의 수 nCk
        while(true) {
            String s = br.readLine();
            String[] sList = s.split(" ");
            long n = Long.parseLong(sList[0]);
            long k = Long.parseLong(sList[1]);
            if (n == 0 && k == 0) {
                br.close();
                break;
            }
            BigInteger topValue = BigInteger.ONE;
            BigInteger underValue = BigInteger.ONE;
            k = Math.min(k,n-k);
            for (int i = 1;i<=k;i++) {
                topValue = topValue.multiply(BigInteger.valueOf(n));
                underValue = underValue.multiply(BigInteger.valueOf(i));
                n--;
            }
            BigInteger tmp = topValue.divide(underValue);
            answer = Add(answer, String.valueOf(tmp));
        }
        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
    }
}