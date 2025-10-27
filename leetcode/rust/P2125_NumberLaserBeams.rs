// https://leetcode.com/problems/number-of-laser-beams-in-a-bank
// Difficulty: Medium

struct Solution;

impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut prev_device_count: i32 = 0;
        let mut total_beams: i32 = 0;
        for row in bank {
            let n_devices = row.bytes().filter(|&b| b == b'1').count() as i32;

            if n_devices > 0 {
                total_beams += prev_device_count * n_devices;
                prev_device_count = n_devices;
            }
        }
        total_beams
    }
}

fn main() {
    let test_cases = vec![
        (vec!["011001", "000000", "010100", "001000"], 8),
        (vec!["000", "111", "000"], 0),
        (vec!["101", "010", "101"], 8),
        // You can easily add more cases here
        (vec!["1", "1", "1", "1"], 3), // (1*1) + (1*1) + (1*1) = 3
        (vec!["11", "00", "11"], 4),   // (2*2) = 4
        (vec!["111"], 0),              // Single row
        (vec!["000", "000"], 0),       // All empty
    ];
    for (test_case, expected) in test_cases {
        let input_vec: Vec<String> = test_case.iter().map(|s| s.to_string()).collect();
        let result = Solution::number_of_beams(input_vec);
        println!("Number of laser beams: {}, expected: {}", result, expected);
    }
}
