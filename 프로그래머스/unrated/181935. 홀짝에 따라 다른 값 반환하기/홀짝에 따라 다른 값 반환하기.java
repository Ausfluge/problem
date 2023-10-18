class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if (n % 2 == 0) {
            for (int i = 0; i <= n; i++) {
                if (i % 2 == 0) {
                    answer += Math.pow(i, 2);
                }
                else {
                    answer += 0;
                }
            }
        }
        else {
            for (int i = 0; i <= n; i++) {
                if (i % 2 == 1) {
                    answer += i;
                }
                else {
                    answer += 0;
                }
            }
        }
        
        return answer;
    }
}