class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        int l=nums.size();
        
        for (int i=0;i<l;i++){
            int t=target-nums[i];
            if (m.find(t)!=m.end()){
                return {m[t],i};
            }
            m[nums[i]]=i;
        }
        
        return {0};
    }
};