// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

struct Solution;

impl Solution {
    pub fn valid_partition(nums: Vec<i32>) -> bool {
        if nums.len() == 0 {
            return true;
        }
        if nums.len() == 1 {
            return false;
        }

        let mut good: Vec<bool> = vec![false; nums.len()];
        good[1] = nums[0] == nums[1];

        if nums.len() == 2 {
            return good[1];
        }

        good[2] = (nums[0] == nums[1] && nums[1] == nums[2])
            || (nums[2] == nums[1] + 1 && nums[1] == nums[0] + 1);

        for i in 3..nums.len() {
            good[i] = (good[i - 2] && nums[i] == nums[i - 1])
                || (good[i - 3]
                    && ((nums[i] == nums[i - 1] && nums[i - 1] == nums[i - 2])
                        || (nums[i] - 1 == nums[i - 1] && nums[i - 2] == nums[i] - 2)));
        }
        return good[good.len() - 1];
    }
}

fn main() {
    println!(
        "Input: {:?} Output: {} Expected: {}",
        vec![1, 2, 3, 3, 4, 5],
        Solution::valid_partition(vec![1, 2, 3, 3, 4, 5]),
        true
    );
}
