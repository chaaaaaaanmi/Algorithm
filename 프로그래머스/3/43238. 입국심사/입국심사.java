class Solution {
    
    public long solution(int n, int[] times) {
        
        long start = 1; // 최소 시간
        
        int maxTime = 0;
        for (int time : times) {
            maxTime = Math.max(maxTime, time);
        }
        
        long end = (long) maxTime * n; // 최대 시간
        long answer = end;

        // 이진 탐색 시작
        while (start <= end) {
            long mid = (start + end) / 2;
            long count = getCount(mid, times); // mid 시간 동안 몇 명 심사 가능한가
            
            // 주어진 사람 수보다 크거나 같으면 오른쪽 날리고
            if (count >= n) {
                answer = mid;
                end = mid - 1; // 다시 탐색 조건 설정
            }
            // 주어진 사람 수보다 작으면 왼쪽 날리기
            else {
                start = mid + 1;
            }
        }
        
        return answer;
    }
    
    
    public long getCount(long midTime, int[] times) {
        long total = 0;
        for (int t : times) {
            total += midTime / t;
        }
        return total;
    }
}