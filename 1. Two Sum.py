class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashSet<Integer> s = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            s.add(nums[i]);
        }
        int a, t;
        for (int i = 0; i < nums.length; i++) {
            a = nums[i];
            t = target - a;
            if (s.contains(t)) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[j] == t) {
                        return new int[]{i, j};
                    }
                }
            }
        }
        return nums;
    }
}
