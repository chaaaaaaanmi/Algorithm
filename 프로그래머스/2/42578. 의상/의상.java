import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < clothes.length; i++) {
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0)+1);
        }
        
        int answer = 1;
        for (int count : map.values()) {
            answer *= (count + 1); // 해당 종류 의상 입지 않는 경우의 수 포함
        }
        
        return answer - 1; // 아무 의상도 고르지 않는 경우 제외
    }
}