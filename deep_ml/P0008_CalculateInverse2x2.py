# https://www.deep-ml.com/problems/8
# Difficulty: Medium

import torch
import jax
import jax.numpy as jnp

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return None
    a, b = matrix[0]
    c, d = matrix[1]
    det = a * d - b * c
    if det == 0:
        return None
    inv_det = 1.0 / det
    return [[d * inv_det, -b * inv_det], [-c * inv_det, a * inv_det]]

def inverse_2x2_torch(matrix) -> torch.Tensor | None:    
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return None
    m = torch.as_tensor(matrix, dtype=torch.float)
    # Your implementation here
    det_m = m[0][0] * m[1][1] - m[1][0] * m[0][1]
    if det_m == 0:
        return None
    return 1. / det_m * torch.tensor([[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]])

def inverse_2x2_jax(matrix) -> list[list[float]] | None:
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return None
    m = jnp.array(matrix, dtype=jnp.float32)
    # Your implementation here
    det_m = jax.numpy.linalg.det(m)
    if det_m == 0:
        return None
    return (1. / det_m * jnp.array([[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]])).tolist()


if __name__ == "__main__":
    for matrix, expected in [
        ([[4, 7], [2, 6]], [[0.6, -0.7], [-0.2, 0.4]]),
        ([[1, 2], [3, 4]], [[-2.0, 1.0], [1.5, -0.5]]),
        ([[1, 2], [2, 4]], None),  # Singular matrix
        ([[1]], None),  # Not 2x2
        ([[1, 2, 3], [4, 5, 6]], None),  # Not 2x2
    ]:
        actual = inverse_2x2(matrix)
        print(f"inverse_2x2({matrix}) = {actual}, expected {expected}")
        actual_torch = inverse_2x2_torch(matrix)
        print(f"inverse_2x2_torch({matrix}) = {actual_torch}, expected {expected}")
        actual_jax = inverse_2x2_jax(matrix)
        print(f"inverse_2x2_jax({matrix}) = {actual_jax}, expected {expected}")