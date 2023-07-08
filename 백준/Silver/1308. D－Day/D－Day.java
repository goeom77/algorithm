import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.stream.Stream;

public class Main {
    static int monthToDay(int[] special_year,int[] month_day, int[] all) {
        int day = all[2];
        if (special_year[all[0]] == 1) {
            month_day[2] = 29;
        }
        for (int i=1;i<all[1];i++) {
            day += month_day[i];
        }
        return day;
    }
     static long yearToDay(int[] special_year,int sum_year_day,int[] all,int all_day) {
        long day = all_day;
        for (int i=1; i<all[0];i++) {
            day += special_year[i];
            day += sum_year_day;
        }
        return day;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String first = br.readLine();
        int[] now = Stream.of(first.split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        String second = br.readLine();
        int[] d = Stream.of(second.split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] month_day = {0,31,28,31,30,31,30,31,31,30,31,30,31};
        int sum_year_day = 0;
        for (int i= 0; i<=12; i++) {
            sum_year_day += month_day[i];
        }

        int[] special_year = new int[10001];
        for (int i= 0;i<=10000;i++) {
            if (i%400 == 0) {
                special_year[i] = 1;
            } else if (i%100 == 0) {
                continue;
            } else if (i%4 == 0) {
                special_year[i] = 1;
            }
        }
        String answer;
        int now_day = monthToDay(special_year,month_day,now);
        int d_day = monthToDay(special_year,month_day,d);
        if ((now[0] + 1000 < d[0]) || (((now[0] + 1000) == d[0]) && (d_day >= now_day))) {
            answer = "gg";
        } else {
            long all_now = yearToDay(special_year,sum_year_day,now,now_day);
            long all_d = yearToDay(special_year,sum_year_day,d,d_day);
            long tmp = all_d - all_now;
            answer = "D-" + String.valueOf(tmp);
        }

        System.out.println(answer);
    }
}