# Creator : Khady Gueye

"""
This program find best-case space complexity and worst-case space complexity.
"""


def variable_space(n, condition=True):
    """
    Uses O(1) space if condition=False,
    Uses O(n^2) space if condition=True.
    """
    if not condition:
        return 0  # O(1) space

    # Worst-case
    matrix = [[0] * n for _ in range(n)]
    return matrix
