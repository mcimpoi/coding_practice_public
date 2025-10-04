// https://leetcode.com/problems/container-with-most-water
// Difficulty: Medium

struct Solution;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;
        let mut max_area: i32 = 0;
        while left < right {
            max_area = std::cmp::max(
                max_area,
                (right - left) as i32 * std::cmp::min(height[left], height[right]),
            );
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        max_area
    }
}

fn main() {
    let test_cases = vec![
        (vec![1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        (vec![1, 1], 1),
        (vec![4, 3, 2, 1, 4], 16),
        (vec![1, 2, 3, 4, 5, 6, 7, 6, 4, 3, 2, 1], 21),
    ];

    for (height, expected) in test_cases {
        println!(
            "Input: {:?} Output: {} Expected: {}",
            height,
            Solution::max_area(height.clone()),
            expected
        );
    }
}
