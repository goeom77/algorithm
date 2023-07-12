import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;



public class Main {
    private static void printAnswer(long value) {
        System.out.print(value);
        System.out.print(" ");
    }
    private static void possible(long sumValue, long lenValue) {
        if (lenValue > 100) {
            System.out.print(-1);
            System.out.print(" ");
        } else {
            if (lenValue % 2 == 0) {
                // 짝수이면
                long tmp = sumValue - (lenValue/2);
                if ((tmp % lenValue) == 0) {
                    long start = (tmp/lenValue) - (lenValue/2) +1;
                    if (start < 0) {
                        possible(sumValue, 101);
                    } else {
                        for (long i=0;i<lenValue;i++) {
                            printAnswer(start + i);
                        }
                    }
                } else {
                    possible(sumValue, lenValue + 1);
                }
            } else {
                // 홀수이면
                if ((sumValue % lenValue) == 0) {
                    long start = (sumValue/lenValue) - ((lenValue-1)/2);
                    if (start < 0) {
                        possible(sumValue, 101);
                    } else {
                        for (long i=0;i<lenValue;i++) {
                            printAnswer(start + i);
                        }
                    }
                } else {
                    possible(sumValue, lenValue + 1);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] sList = br.readLine().split(" ");
        long N = Long.parseLong(sList[0]);
        long L = Long.parseLong(sList[1]);
        // 길이가 적어도 L이면서 합이 N인 가장 짧은 연속된 정수 리스트 구하기
        // 길이가 홀수인 경우 가운데수로 딱 나눠 떨어져야 한다.
        // 길이가 짝수인 경우 중심으로부터 길이/2 만큼 크거나 작아야 한다.
        // 홀수이면 길이로 나눠서 떨어지는지 알아보기!
        // 짝수이면 길이/2로 빼고 그 수가 길이로 나눠서 떨어지는지 알아보기!
        // 길이가 100보다 작거나 같으면 출력, 크면 -1로 출력
        possible(N,L);
        System.out.println();
    }
}