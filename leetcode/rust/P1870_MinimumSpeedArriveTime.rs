// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

struct Solution;

impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        let n = dist.len() as i32;

        if (hour <= (n - 1) as f64) {
            return -1;
        }

        let mut left: i32 = 1;
        let maxValue = dist.iter().max();
        let mut maxVal: i32 = -1;
        match maxValue {
            Some(max) => maxVal = *max,
            None => maxVal = -1,
        }

        let mut right: i32 = 1 + std::cmp::max(
            maxVal,
            (dist[(n - 1) as usize] as f64 / (hour - ((n - 1) as f64))).ceil() as i32,
        );

        let mut res: i32 = -1;

        while left <= right {
            let mut mid = (left + right) / 2;
            let mut crt_time: f64 = 0.0;

            for idx in 0..(n - 1) {
                crt_time += ((dist[idx as usize]) as f64 / mid as f64).ceil();
            }
            crt_time += dist[(n - 1) as usize] as f64 / mid as f64;

            if (crt_time <= hour) {
                res = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
}

fn main() {
    println!(
        "Input: {:?} {} Output: {} Expected: {}",
        vec![1, 3, 2],
        6.0,
        Solution::min_speed_on_time(vec![1, 3, 2], 6.0),
        1
    );
}
