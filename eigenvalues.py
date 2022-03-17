from sage.all import *

def calc_eigenvalues(det, x):
    return solve(det == 0, x)

def calc_determinant(mat):
    return mat.determinant()

def convert_matrix(mat, rowsandcols, x):
    return mat-(x*identity_matrix(rowsandcols))

if __name__ == "__main__":
    x = var('x')
    mat = matrix([[1,-3,3], [3, -5, 3], [6,-6,4]])
    mat = convert_matrix(mat, 3, x)
    det = calc_determinant(mat)
    print(det)
    print(calc_eigenvalues(det, x))
