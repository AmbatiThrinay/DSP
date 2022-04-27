import streamlit as st
import scipy.io
from scipy import signal
import matplotlib.pyplot as plt
plt.style.reload_library()
plt.style.use(['science', 'notebook', 'grid'])
import numpy as np

# ppg signal file path
ppg_signal_path = 'ppg_random_noise.mat'
ppg_signal = scipy.io.loadmat(ppg_signal_path)['ppg_random'].T

def ppg_smooth(x,w):
    ppg_avg = []
    for i in range(w,x.shape[0]+1):
        window = sum(x[i-w:i])/w
        ppg_avg.append(window)
    time = np.arange(ppg_signal.shape[0])/100
    time = time[w-1:]
    return time,np.array(ppg_avg)

def draw_plot(m):
    fig = plt.figure(figsize=(11,9))
    plt.title(f"M-point moving average filter")
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    t,amplitude = ppg_smooth(ppg_signal,m)
    plt.plot(t,amplitude,label = f'filtered PPG signal, M={m}')
    plt.plot(np.arange(ppg_signal.shape[0])/100,ppg_signal,label = 'original PPG signal',alpha=0.6)
    plt.legend()
    plt.grid()
    st.pyplot(fig)

## App

st.title('Moving Average Filter')
st.markdown('''
**Name**	: Ambati Thrinay Kumar Reddy
**Roll No**: 121901003
## Problem Statement
Design and Implement M-point moving average filter to smooth out the high-frequency noises. Obtain the outputs of the moving average filter with M=10, 25, 50, 100 for the 5 second PPG signal [Fs=100 Hz].

Difference equation of Simple Causal Moving Average filter''')
st.latex(r'''
\begin{aligned} y[n] = \displaystyle{\frac{1}{M} \sum_{k=0}^{M-1}x[n-k]}\quad\quad \end{aligned}''')
st.markdown('''
Example : difference equation of 5 point moving Average filter (M=5)''')
st.latex(r'''
\begin{aligned} y[n] &= \displaystyle{\frac{1}{5} \left(x[n] + x[n-1] + x[n-2] + x[n-3] + x[n-4] \right) } \\ &= 0.2 \left(x[n] + x[n-1] + x[n-2] + x[n-3] + x[n-4] \right) \end{aligned} \quad\quad''')
st.markdown('''
The recursive form of moving average filter''')
st.latex(r'''
\begin{aligned} y[n] = y[n-1] + \frac{1}{5}x[n] - \frac{1}{5}x[n-5] \end{aligned}
''')
m = st.sidebar.slider('Window length (M)',5,100,10,5)
draw_plot(m)
