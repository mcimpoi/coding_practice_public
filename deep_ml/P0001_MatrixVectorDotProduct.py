# https://www.deep-ml.com/problems/1
# Difficulty: Easy

import torch
import jax

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a) == 0 or len(a[0]) != len(b):
        return [-1]
    return [sum(x * y for x, y in zip(row, b)) for row in a]

def matrix_dot_vector_torch(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a) == 0 or len(a[0]) != len(b):
        return [-1]
    a_tensor = torch.tensor(a)
    b_tensor = torch.tensor(b)
    result_tensor = torch.matmul(a_tensor, b_tensor)
    return result_tensor.tolist()


def matrix_dot_vector_jax(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a) == 0 or len(a[0]) != len(b):
        return [-1]
    a_array = jax.numpy.array(a)
    b_array = jax.numpy.array(b)

    result_array = jax.numpy.dot(a_array, b_array)
    return result_array.tolist()

if __name__ == "__main__":
    for a, b, expected in [
        ([[1, 2, 3], [4, 5, 6]], [7, 8, 9], [  74, 173]),
        ([[1, 2], [3, 4]], [5, 6], [17, 39]),
        ([[1, 2]], [3, 4], [11]),
        ([], [1, 2], [-1]),
        ([[1, 2]], [3], [-1]),
    ]:
        actual = matrix_dot_vector(a, b)
        print(f"matrix_dot_vector({a}, {b}) = {actual}, expected {expected}")
        actual_torch = matrix_dot_vector_torch(a, b)
        print(f"matrix_dot_vector_torch({a}, {b}) = {actual_torch}, expected {expected}")
        actual_jax = matrix_dot_vector_jax(a, b)
        print(f"matrix_dot_vector_jax({a}, {b}) = {actual_jax}, expected {expected}")