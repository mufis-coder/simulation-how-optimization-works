import numpy as np

def objective_function(X, Y):
     return 30 - (np.square(X-3.14) + np.square(Y - 2.72) + np.sin(3*X + 1.41) + 
                  np.sin(4*Y - 1.73) - np.cos(1.5*X - 1.21) - np.cos(1.2*Y + 1.7) + X)