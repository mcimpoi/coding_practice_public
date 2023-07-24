// https://leetcode.com/problems/find-the-highest-altitude/

struct Solution;

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut crt: i32 = 0;
        let mut max_altitude: i32 = 0;

        for g in gain {
            crt += g;
            max_altitude = std::cmp::max(crt, max_altitude);
        }
        return max_altitude;
    }
}

fn main() {
    println!(
        "Input: {:?} Output: {} Expected: {}",
        vec![-5, 1, 5, 0, -7],
        Solution::largest_altitude(vec![-5, 1, 5, 0, -7]),
        1
    );
}
