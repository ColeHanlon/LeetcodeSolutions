public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.Length - 1;

        int ans = 0;
        while(low <= high){
            int mid = low + (high - low)/2;
            if(nums[mid] == target){
                ans = mid;
                break;
            }else if(nums[mid] > target){
                high = mid - 1;
            }else{
                ans = mid + 1;
                low = mid + 1;
            }
        }
        return ans;
    }
}