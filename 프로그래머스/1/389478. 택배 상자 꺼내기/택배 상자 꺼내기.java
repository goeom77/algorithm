
class Solution {
    public int solution(int n, int w, int num) {
        int answer = 1;
        int c = (int)Math.round(n/w+1);
        int[][] boxList = new int[c][w];
        boolean isRight = true;
        int tmpRow = 0;
        int tmpCol = 0;
        int resultRow = 0;
        int resultCol = 0;
        for (int i=1; i< n+1; i++) {
            if(i == num) {
                resultRow = tmpRow;
                resultCol = tmpCol;
            }
            if(isRight && tmpRow == w-1) {
                boxList[tmpCol][tmpRow] = i;
                tmpCol++;
                isRight = false;
            } else if(!isRight && tmpRow == 0) {
                boxList[tmpCol][tmpRow] = i;
                tmpCol++;
                isRight = true;
            } else if(isRight) {
                boxList[tmpCol][tmpRow] = i;
                tmpRow++;
            } else if(!isRight) {
                boxList[tmpCol][tmpRow] = i;
                tmpRow--;
            }
        }
        for (int i = resultCol+1; i < c; i++) {
            if (boxList[i][resultRow] != 0) {
                answer++;
            }
        }
        
        return answer;
    }
}