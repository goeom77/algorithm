import java.io.*;
import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer =0;
        int[] seats = {-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1};
        for (int lo: lost) {
            seats[lo] = 0;
        }
        for (int re: reserve) {
            seats[re] += 1;
        }
        for (int i=1; i<=n; i++) {
            if(seats[i]== 1) {
                answer +=1;
            }
            if(seats[i]== 2) {
                if(seats[i-1] == 0) {
                    seats[i-1] = 1;
                    answer +=2;
                } else if (seats[i+1] ==0) {
                    seats[i+1] = 1;
                    answer += 1;
                } else {
                    answer +=1;
                }
            }
        }
        return answer;
    }
}