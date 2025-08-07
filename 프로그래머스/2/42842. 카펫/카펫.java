class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        
        int total = brown + yellow;
        
        // 가로, 세로 최소 길이는 3
        for (int c = 3; c <= total; c++) {
            for (int r = 3; r <= total; r++) {
                if ((r-2)*(c-2) == yellow &&
                   (r*2)+(2*(c-2)) == brown) {
                    return new int[]{r, c};

                }
            }
        }
        
        return answer;
    }
}