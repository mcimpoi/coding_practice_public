// https://leetcode.com/problems/successful-pairs-of-spells-and-potions
// Difficulty: Medium

struct Solution;
impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let mut potions = potions;
        potions.sort();

        let mut result: Vec<i32> = vec![0; spells.len()];
        for idx in 0..spells.len() {
            let target: i64 = (success + (spells[idx] as i64) - 1) / (spells[idx] as i64);
            let mut left: i32 = 0;
            let len_i32 = potions.len() as i32;
            let mut right: i32 = len_i32 - 1;
            let mut first_index: i32 = len_i32;

            while left <= right {
                let mid = left + (right - left) / 2;
                if (potions[mid as usize] as i64) >= target {
                    first_index = mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            result[idx] = len_i32 - first_index;
        }
        result
    }
}

fn main() {
    println!(
        "Input: {:?}, {:?}, {} Output: {:?} Expected: {:?}",
        vec![5, 1, 3],
        vec![1, 2, 3, 4, 5],
        7,
        Solution::successful_pairs(vec![5, 1, 3], vec![1, 2, 3, 4, 5], 7),
        vec![4, 0, 3]
    );
}
