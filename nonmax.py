import numpy as np

def non_max_suppression(img, D):
    M, N = img.shape[:2]
    Z = np.zeros((M,N), dtype=np.int32)
    Z = Z.reshape(M,N,1)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
               #angle 0
                if (0 <= angle[i][j][0] < 22.5) or (157.5 <= angle[i][j][0] <= 180.0):
                    q = img[i][j+1][0]
                    r = img[i][j-1][0]
                #angle 45
                elif (22.5 <= angle[i][j][0] < 67.5):
                    q = img[i+1][j-1][0]
                    r = img[i-1][j+1][0]
                #angle 90
                elif (67.5 <= angle[i][j][0] < 112.5):
                    q = img[i+1][j][0]
                    r = img[i-1][j][0]
                #angle 135
                elif (112.5 <= angle[i][j][0] < 157.5):
                    q = img[i-1][j-1][0]
                    r = img[i+1][j+1][0]

                if (img[i][j][0] >= q) and (img[i][j][0] >= r):
                    Z[i][j][0] = img[i][j][0]
                else:
                    Z[i][j][0] = 0

            except IndexError as e:
                pass
    
    return Z