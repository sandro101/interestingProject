import numpy as np 
class RotateImage:
    def rotate(self, matrix):
        rows = []
        num_rows = matrix.shape[0] 
        for row in range(num_rows):       
            cols = np.asarray(matrix[:, row][::-1]).flatten()
            rows.append(cols)
        return np.matrix(rows)
          
print(RotateImage().rotate(np.matrix('1 2; 3 4')) == (np.matrix('3 1; 4 2')));

