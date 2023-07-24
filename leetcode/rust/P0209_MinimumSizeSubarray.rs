// https://leetcode.com/problems/minimum-size-subarray-sum/

struct Solution;

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = 0;
        let mut crt_sum: i32 = 0;

        let num_sz: i32 = nums.len() as i32;
        let mut min_len: i32 = num_sz + 1;

        while right < num_sz {
            while right < num_sz && crt_sum < target {
                crt_sum += nums[right as usize];
                right += 1;
            }

            if crt_sum >= target {
                min_len = std::cmp::min(min_len, right - left);
            }

            while left < right && crt_sum >= target {
                crt_sum -= nums[left as usize];
                left += 1;
                if crt_sum >= target {
                    min_len = std::cmp::min(min_len, right - left);
                }
            }
        }
        return min_len % (num_sz + 1);
    }
}

fn main() {
    println!(
        "Input: {:?} Output: {} Expected: {}",
        vec![2, 3, 1, 2, 4, 3],
        Solution::min_sub_array_len(7, vec![2, 3, 1, 2, 4, 3]),
        2
    );
}
