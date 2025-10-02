// https://leetcode.com/problems/water-bottles-ii
// Difficulty: Medium

struct Solution;

impl Solution {
    pub fn max_bottles_drunk(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut total_drunk = num_bottles;
        let mut num_empty = num_bottles;
        let mut num_exchange_local = num_exchange;
        while num_empty >= num_exchange_local {
            num_empty = num_empty - num_exchange_local + 1;
            total_drunk += 1;
            num_exchange_local += 1;
        }
        total_drunk
    }
}

fn main() {
    let test_cases = vec![
        (13, 6, 15),
        (10, 3, 13),
        (37, 29, 38),
        (2, 3, 2),
        (99, 5, 109),
        (100, 3, 112),
    ];

    for (num_bottles, num_exchange, expected) in test_cases {
        println!(
            "Input: {} {} Output: {} Expected: {}",
            num_bottles,
            num_exchange,
            Solution::max_bottles_drunk(num_bottles, num_exchange),
            expected
        );
    }
}
