import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

import static java.lang.Integer.max;
import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = parseInt(br.readLine());
        Long[] ropeList = new Long[n];
        for (int i=0;i<n;i++) {
            ropeList[i] = parseLong(br.readLine());
        }
        Long maxResult = 0L;
        // ropeList sort하기
        Arrays.sort(ropeList, Collections.reverseOrder());
        int m = 0;
        for (Long rope:ropeList) {
            m += 1;
            if ( rope*m > maxResult ) {
                maxResult = rope*m;
            }
        }
        System.out.println(maxResult);

    }
}