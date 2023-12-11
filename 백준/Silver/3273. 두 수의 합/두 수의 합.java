import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n = number of vertices
        int n = Integer.parseInt(st.nextToken());
       // n개의 수를 띄어쓰기로 파싱해서 리스트로 받아오기
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        // 두수의 합 구하기
        Arrays.sort(arr);
        int sum = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        int result = 0;
        int left = 0;
        int right = n-1;
        while(left<right) {
            int temp = arr[left] + arr[right];
            if(temp == sum) {
                result++;
                left++;
                right--;
            } else if(temp < sum) {
                left++;
            } else {
                right--;
            }
        }
        System.out.println(result);
    }
}