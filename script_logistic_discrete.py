import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Discrete logistic model (May, 1976)")

# input of the number of iterations and intrinsic growth rate
nIterations = st.slider('Enter the number of iterations:', min_value=2, max_value=100, value = 20, step=1)

r = st.slider('Enter the Intrinsic growth rate (r):', min_value=.95, max_value=4.0, value = 2.0, step=0.02)

def discr_log(x, r):
    return r*x*(1-x)


# initialize the state vector (and time)
state = np.zeros(nIterations + 1)
time = np.arange(0, nIterations+1, step = 1)
# define the initial condition
state[0] = .1
# fill the state vector with the logistic model
for i in range(nIterations):
    state[i+1] = discr_log(state[i], r)

# cobweb construction
cobx = np.repeat(state, 2)[0:-1]
coby = np.concatenate(([0], np.repeat(state, 2)[2:]))


# do the plotting ax1: cobweb, ax2: state vs time
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
statePlot = np.linspace(0, 1.0)
ax1.plot(cobx, coby, color = 'C1')
ax1.plot(statePlot, discr_log(statePlot, r), color = 'C0')
ax1.plot(statePlot, statePlot, color = 'C2')
ax1.grid()

ax2.plot(time, state, color = 'C1')
ax2.grid()

#fig.show()
st.pyplot(fig)






