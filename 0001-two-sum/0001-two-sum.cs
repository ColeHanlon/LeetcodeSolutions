public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> vals_index = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++){
            int needed_index = -1;
            if(vals_index.TryGetValue(target - nums[i], out needed_index)){
                return new int[2]{needed_index, i};
            }
            else{
                vals_index[nums[i]] = i;
            }
        }

        return new int[2];
    }
}