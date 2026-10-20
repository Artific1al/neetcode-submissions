// import java.util.HashMap
// import java.util.Map

class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        Map<Integer, Boolean> hash = new HashMap<Integer, Boolean>();

        for(int i = 0; i< nums.length; i++){
            //check if the key already exists
            if(hash.containsKey(nums[i])){
                return true; // there is a duplicate number in the array
            }
            else{
                hash.put(nums[i], true);
            }
        }

        return false;

    }
}