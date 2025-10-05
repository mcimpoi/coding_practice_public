// https://leetcode.com/problems/pacific-atlantic-water-flow
// Difficulty: Medium

use std::collections::VecDeque;

struct Solution;

impl Solution {
    pub fn fill_(heights: &Vec<Vec<i32>>, row: i32, col: i32) -> Vec<Vec<i32>> {
        let n_rows = heights.len();
        let n_cols = heights[0].len();

        let mut visited: Vec<Vec<i32>> = vec![vec![0; n_cols]; n_rows];
        let mut q: VecDeque<(i32, i32)> = VecDeque::new();

        for r in 0..n_rows {
            q.push_back((r as i32, col));
            visited[r][col as usize] = 1;
        }
        for c in 0..n_cols {
            q.push_back((row, c as i32));
            visited[row as usize][c] = 1;
        }

        const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];
        while !q.is_empty() {
            if let Some((crt_r, crt_c)) = q.pop_front() {
                for (dr, dc) in DIRECTIONS {
                    let (next_r, next_c) = (crt_r + dr, crt_c + dc);
                    if next_r >= 0
                        && (next_r as usize) < n_rows
                        && next_c >= 0
                        && (next_c as usize) < n_cols
                        && visited[next_r as usize][next_c as usize] == 0
                        && heights[next_r as usize][next_c as usize]
                            >= heights[crt_r as usize][crt_c as usize]
                    {
                        visited[next_r as usize][next_c as usize] = 1;
                        q.push_back((next_r as i32, next_c as i32));
                    }
                }
            }
        }

        visited
    }

    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n_rows = heights.len();
        let n_cols = heights[0].len();
        let visited1 = Self::fill_(&heights, 0, 0);
        let visited2 = Self::fill_(&heights, n_rows as i32 - 1, n_cols as i32 - 1);

        let mut res = Vec::new();
        for r in 0..n_rows {
            for c in 0..n_cols {
                if visited1[r][c] == 1 && visited2[r][c] == 1 {
                    res.push(vec![r as i32, c as i32]);
                }
            }
        }

        res
    }
}

fn main() {
    let test_cases = vec![
        (
            vec![
                vec![1, 2, 2, 3, 5],
                vec![3, 2, 3, 4, 4],
                vec![2, 4, 5, 3, 1],
                vec![6, 7, 1, 4, 5],
                vec![5, 1, 1, 2, 4],
            ],
            vec![
                vec![0, 4],
                vec![1, 3],
                vec![1, 4],
                vec![2, 2],
                vec![3, 0],
                vec![3, 1],
                vec![4, 0],
            ],
        ),
        (
            vec![vec![2, 1], vec![1, 2]],
            vec![vec![0, 0], vec![0, 1], vec![1, 0], vec![1, 1]],
        ),
    ];

    for (heights, expected) in test_cases {
        println!(
            "Input: {:?} Output: {:?} Expected: {:?}",
            heights,
            Solution::pacific_atlantic(heights.clone()),
            expected
        );
    }
}
