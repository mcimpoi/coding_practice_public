// https://leetcode.com/problems/sign-of-the-product-of-an-array/

struct Solution;

impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut neg: i32 = 0;
        for num in nums {
            if num == 0 {
                return 0;
            }
            if num < 0 {
                neg = 1 - neg;
            }
        }
        if neg == 1 {
            return -1
        } else {
            return 1
        }
    }
}

fn main() {
    println!("Input: {:?} Output: {} Expected: {}", vec![1,5,2,-3], Solution::array_sign(vec![1,5,2,-3]), -1);
}