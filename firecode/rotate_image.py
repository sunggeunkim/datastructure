def rotate_image(image_matrix):
    if image_matrix == None:
        return None
    n = len(image_matrix)
    if n == 0 or n == 1:
        return image_matrix
    
    new_image_matrix = [x[:] for x in image_matrix]
    
    i = n - 1
    m = 0
    while i > 0:
        for j in range(i):
            new_image_matrix[m][j+1] = image_matrix[m][j]
            new_image_matrix[j+1][n-m-1] = image_matrix[j][n-m-1]
            new_image_matrix[n-m-1][j] = image_matrix[n-m-1][j+1]
            new_image_matrix[j][m] = image_matrix[j+1][m]
            
            
        m += 1
        i -= 2
    return new_image_matrix
