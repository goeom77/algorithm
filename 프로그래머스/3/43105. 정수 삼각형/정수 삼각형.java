import java.io.*;
import java.util.*;
class Solution {
    public int solution(int[][] triangle) throws Exception {
//  꼭대기에서 아래로 내려가는 경로 중 거쳐간 숫자 합 가장 큰 것
//  한칸 오른쪽 또는 왼쪽으로 내려갈 수 있다.
//  왼쪽, 오른쪽 두개 더해서 
        int n = triangle.length;
        int[][] memory = new int[n][n];
        memory[0][0] = triangle[0][0];
        for (int j=1; j < n; j++) {
            for (int i=0; i<= j; i++) {
                    if(i==0) {
                        memory[j][i] = triangle[j][i] + memory[j-1][i];
                    } else if(i == n-1) {
                        memory[j][i] = triangle[j][i] + memory[j-1][i-1];
                    } else {
                        memory[j][i] = Math.max(memory[j-1][i-1], memory[j-1][i])+triangle[j][i];
                    }
            }
        }
        int maxValue = 0;
        for(int a: memory[n-1]) {
            if(a>maxValue) {
                maxValue = a;
                
            }
        }
        
        return maxValue;
    }
}