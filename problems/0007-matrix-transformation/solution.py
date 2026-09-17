import numpy as np

def transform_matrix(A: list[list[int|float]],
                     T: list[list[int|float]],
                     S: list[list[int|float]]):

    if len(T) != len(T[0]):
        return -1

    if len(T[0]) != len(A) or len(A[0]) != len(S):
        return -1

    Tnumpy = np.array(T)
    Snumpy = np.array(S)
    Anumpy = np.array(A)

    try:
        T_inv = np.linalg.inv(Tnumpy)
		np.linalg.inv(Snumpy)
        return ((T_inv @ Anumpy) @ Snumpy).tolist()

    except np.linalg.LinAlgError:
        return -1
	