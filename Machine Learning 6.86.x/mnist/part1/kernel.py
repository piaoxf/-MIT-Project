import numpy as np

### Functions for you to fill in ###



def polynomial_kernel(X, Y, c, p):
    """
        Compute the polynomial kernel between two matrices X and Y::
            K(x, y) = (<x, y> + c)^p
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            c - a coefficient to trade off high-order and low-order terms (scalar)
            p - the degree of the polynomial kernel

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    kernel_matrix = np.dot(X, Y.T) + c
    kernel_matrix = np.power(kernel_matrix, p)
    
    return kernel_matrix



def rbf_kernel(X, Y, gamma):
    """
        Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            gamma - the gamma parameter of gaussian function (scalar)

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    # (n,m)のカーネル行列を初期化
    kernel_matrix = np.zeros((X.shape[0], Y.shape[0]))
    for i in range(X.shape[0]):
        for j in range(Y.shape[0]):
            # ユークリッド距離の2乗を計算し、ガウスカーネルを計算
            kernel_matrix[i, j] = np.exp(-gamma * np.linalg.norm(X[i] - Y[j]) ** 2)
    return kernel_matrix

    # より効率的な実装
    # x_norm = np.sum(X ** 2, axis=1).reshape(-1, 1) # 各 x_iのノルムの2乗(n, 1)
    # y_norm = np.sum(Y ** 2, axis=1).reshape(1, -1) # 各 y_iのノルムの2乗(1, m)

    # # ユークリッド距離の2乗を計算 ||X-Y||^2 = ||X||^2 + ||Y||^2 - 2<X, Y>
    # dist = x_norm + y_norm - 2 * np.dot(X, Y.T) 

    # # ガウスカーネルを計算
    # kernel_matrix = np.exp(-ganma * dist)
    # return kernel_matrix
