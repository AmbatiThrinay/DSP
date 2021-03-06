# Importing necessary libraries
import streamlit as st
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
plt.style.use(['science', 'notebook', 'grid'])

# Extract PPG signal from .mat file
ppg_signal_path = 'ppg_random_noise.mat'
ppg_signal = scipy.io.loadmat(ppg_signal_path)['ppg_random'].T

# Moving Average Filter 
def moving_avg_filter(x,w):
    ppg_filtered = []
    for i in range(w,x.shape[0]+1):
        # Taking a window of length M
        window_sum = sum(x[i-w:i])/w
        ppg_filtered.append(window_sum)
    time = np.arange(ppg_signal.shape[0])/100
    time = time[w-1:]
    return time,np.array(ppg_filtered)

# Plotting the original PPG signal and filtered PPG signal
def draw_plot(m):
    fig = plt.figure(figsize=(11,9))
    plt.title(f"M-point moving average filtering")
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    t,amplitude = moving_avg_filter(ppg_signal,m)
    plt.plot(t,amplitude,label = f'filtered PPG signal, M={m}')
    plt.plot(np.arange(ppg_signal.shape[0])/100,ppg_signal,label = 'original PPG signal',alpha=0.6)
    plt.legend()
    plt.grid()
    st.pyplot(fig)

## App for GUI

st.markdown('''
**Name**	: Ambati Thrinay Kumar Reddy

**Roll No**: 121901003
### Problem Statement
Design and Implement M-point moving average filter to smooth out the high-frequency noises. Obtain the outputs of the moving average filter with M=10, 25, 50, 100 for the 5 second PPG signal [Fs=100 Hz].

---

Difference equation of *Simple Causal Moving Average filter*''')
st.latex(r'''
\begin{aligned} y[n] = \displaystyle{\frac{1}{M} \sum_{k=0}^{M-1}x[n-k]}\quad\quad \end{aligned}''')
st.markdown('''
**Example** : Difference equation of 5 point moving Average filter (M=5)''')
st.latex(r'''
\begin{aligned} y[n] 
&= \displaystyle{\frac{1}{5} \sum_{k=0}^{4}x[n-k]} \\ 
&= \displaystyle{\frac{1}{5} \left(x[n] + x[n-1] + x[n-2] + x[n-3] + x[n-4] \right) } \end{aligned} \quad\quad''')
st.markdown('''
The *recursive form* for above moving average filter''')
st.latex(r'''
\begin{aligned} y[n] = y[n-1] + \frac{1}{5}x[n] - \frac{1}{5}x[n-5] \end{aligned}
''')
m = st.sidebar.slider('Window length (M)',5,100,10,5)
draw_plot(m)
