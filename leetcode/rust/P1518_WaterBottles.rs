// https://leetcode.com/problems/water-bottles/
// Difficulty: Easy

struct Solution;

impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut total_drunk: i32 = num_bottles;
        let mut empty_bottles: i32 = num_bottles;
        while empty_bottles >= num_exchange {
            let new_bottles: i32 = empty_bottles / num_exchange;
            total_drunk += new_bottles;
            empty_bottles = empty_bottles % num_exchange + new_bottles;
        }
        total_drunk
    }

    // O(1) space and time;
    // came across it via code review in Gemini.
    pub fn num_water_bottles_o1(num_bottles: i32, num_exchange: i32) -> i32 {
        return num_bottles + (num_bottles - 1) / (num_exchange - 1);
    }
}

fn main() {
    let test_cases = vec![(9, 3, 13), (15, 4, 19), (5, 5, 6), (2, 3, 2)];

    for (num_bottles, num_exchange, expected) in test_cases {
        println!(
            "Input: {} {} Output: {} Output O1: {} Expected: {}",
            num_bottles,
            num_exchange,
            Solution::num_water_bottles(num_bottles, num_exchange),
            Solution::num_water_bottles_o1(num_bottles, num_exchange),
            expected
        );
    }
}
