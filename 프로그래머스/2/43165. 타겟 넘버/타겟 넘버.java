class Solution {
    static int lastId;
    static int answer;
    static int targetNum;
    static int[] numbersList;
    // 1. 하나씩 빼면서 dfs를 한다.
    public int solution(int[] numbers, int target) {
        answer = 0;
        lastId = numbers.length;
        targetNum = target;
        numbersList = numbers;
        dfs(0,0);
        return answer;
    }
    private static void dfs(int idx, int sum) {
        if (idx == lastId && sum == targetNum) {
            answer++;
            return;
        }
        if (idx == lastId) return;
        dfs(idx+1, sum+numbersList[idx]);
        dfs(idx+1, sum-numbersList[idx]);
        
    }
}