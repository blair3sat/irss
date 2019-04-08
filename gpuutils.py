import numpy as np
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import skcuda.fft as cu_fft
import skcuda.linalg as culinalg
import skcuda.misc as cumisc

def fft(x):
    x = gpuarray.to_gpu(x)
    y = gpuarray.empty(len(x)//2 + 1, np.complex64)
    plan_forward = cu_fft.Plan(x.shape, np.float32, np.complex64)
    cu_fft.fft(x, y, plan_forward)
    return np.array(y)