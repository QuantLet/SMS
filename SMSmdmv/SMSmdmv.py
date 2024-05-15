#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:49:11 2024

@author: raulbag
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Number of samples and correlation
n = 100
rho = 0.9

# Mean vectors
mean_x = np.array([0, 0])
mean_y = np.array([4, 0])

# Covariance matrix
sigma = np.array([[1, rho], [rho, 1]])

# Generate random samples
x = multivariate_normal.rvs(mean=mean_x, cov=sigma, size=n)
y = multivariate_normal.rvs(mean=mean_y, cov=sigma, size=n)

# Combine x and y for plotting limits
xy = np.vstack([x, y])

# Plotting
plt.figure(dpi=900)
plt.scatter(x[:, 0], x[:, 1], color='red', s=10)
plt.scatter(y[:, 0], y[:, 1], color='blue', s=10)

# Setting plot limits
plt.xlim(np.min(xy[:, 0])-1, np.max(xy[:, 0])+1)
plt.ylim(np.min(xy[:, 1])-1, np.max(xy[:, 1])+1)

# Labels
plt.xlabel('x1, y1')
plt.ylabel('x2, y2')

plt.savefig('PySMSMdmv.png', format='png', dpi=900, transparent=True)
plt.show()
