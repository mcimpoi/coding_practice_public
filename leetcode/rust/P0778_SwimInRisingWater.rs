// https://leetcode.com/problems/swim-in-rising-water
// Difficulty: Hard

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    // intuition: always expand the
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let n: usize = grid.len(); // n x n grid

        let mut water_level: i32 = 0;
        let mut min_heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; n];

        min_heap.push(Reverse((grid[0][0], 0, 0)));
        visited[0][0] = true;

        const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

        while !min_heap.is_empty() {
            if let Some(Reverse((crt_level, crt_r, crt_c))) = min_heap.pop() {
                water_level = water_level.max(crt_level);
                if crt_r == n - 1 && crt_c == n - 1 {
                    return water_level;
                }
                for (dr, dc) in DIRECTIONS {
                    let (next_r_i32, next_c_i32) = (crt_r as i32 + dr, crt_c as i32 + dc);
                    if next_r_i32 >= 0
                        && next_r_i32 < n as i32
                        && next_c_i32 >= 0
                        && next_c_i32 < n as i32
                    {
                        let (next_r, next_c) = (next_r_i32 as usize, next_c_i32 as usize);
                        if !visited[next_r][next_c] {
                            min_heap.push(Reverse((grid[next_r][next_c], next_r, next_c)));
                            visited[next_r][next_c] = true;
                        }
                    }
                }
            }
        }

        unreachable!();
    }
}

fn main() {
    let test_cases = vec![
        (vec![vec![0, 2], vec![1, 3]], 3),
        (
            vec![
                vec![0, 1, 2, 3, 4],
                vec![24, 23, 22, 21, 5],
                vec![12, 13, 14, 15, 16],
                vec![11, 17, 18, 19, 20],
                vec![10, 9, 8, 7, 6],
            ],
            16,
        ),
        (vec![vec![10, 12], vec![1, 11]], 11),
        (vec![vec![3]], 3),
    ];

    for (grid, expected) in test_cases {
        println!(
            "Input: {:?} Output: {} Expected: {}",
            grid,
            Solution::swim_in_water(grid.clone()),
            expected
        );
    }
}
