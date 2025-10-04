// https://leetcode.com/problems/trapping-rain-water-ii
// Difficulty: Hard

use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        let n_rows: usize = height_map.len();
        let n_cols: usize = height_map[0].len();

        let mut total_water: i32 = 0;
        let mut boundary = BinaryHeap::new();

        let mut visited: Vec<Vec<i32>> = vec![vec![0; n_cols]; n_rows];

        for r in 1..n_rows - 1 {
            boundary.push((-height_map[r][0], r, 0));
            visited[r][0] = 1;
            boundary.push((-height_map[r][n_cols - 1], r, n_cols - 1));
            visited[r][n_cols - 1] = 1;
        }

        for c in 1..n_cols - 1 {
            boundary.push((-height_map[0][c], 0, c));
            visited[0][c] = 1;
            boundary.push((-height_map[n_rows - 1][c], n_rows - 1, c));
            visited[n_rows - 1][c] = 1;
        }

        // add corners; this was to avoid check if visited
        boundary.push((-height_map[0][0], 0, 0));
        boundary.push((-height_map[n_rows - 1][0], n_rows - 1, 0));
        boundary.push((-height_map[0][n_cols - 1], 0, n_cols - 1));
        boundary.push((-height_map[n_rows - 1][n_cols - 1], n_rows - 1, n_cols - 1));

        visited[0][0] = 1;
        visited[0][n_cols - 1] = 1;
        visited[n_rows - 1][0] = 1;
        visited[n_rows - 1][n_cols - 1] = 1;

        const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

        while !boundary.is_empty() {
            if let Some((min_boundary_height, crt_r, crt_c)) = boundary.pop() {
                let min_boundary_height = -min_boundary_height;
                for (dr, dc) in DIRECTIONS {
                    let (next_r, next_c) =
                        ((crt_r as i32 + dr) as usize, (crt_c as i32 + dc) as usize);
                    if next_r > 0
                        && next_r < n_rows
                        && next_c > 0
                        && next_c < n_cols
                        && visited[next_r][next_c] == 0
                    {
                        let neigh_height = height_map[next_r][next_c];
                        if neigh_height < min_boundary_height {
                            total_water += min_boundary_height - neigh_height;
                        }
                        boundary.push((
                            std::cmp::min(-min_boundary_height, -neigh_height),
                            next_r,
                            next_c,
                        ));
                        visited[next_r][next_c] = 1;
                    }
                }
            }
        }
        total_water
    }
}

fn main() {
    let test_cases = vec![
        (
            vec![
                vec![1, 4, 3, 1, 3, 2],
                vec![3, 2, 1, 3, 2, 4],
                vec![2, 3, 3, 2, 3, 1],
            ],
            4,
        ),
        (
            vec![
                vec![12, 13, 1, 12],
                vec![13, 4, 13, 12],
                vec![13, 8, 10, 12],
                vec![12, 13, 12, 12],
                vec![13, 13, 13, 13],
            ],
            14,
        ),
        (
            vec![
                vec![9, 9, 9, 9],
                vec![9, 0, 0, 9],
                vec![9, 0, 0, 9],
                vec![9, 9, 9, 9],
            ],
            36,
        ),
    ];

    for (height_map, expected) in test_cases {
        println!(
            "Input: {:?} Output: {} Expected: {}",
            height_map,
            Solution::trap_rain_water(height_map.clone()),
            expected
        );
    }
}
