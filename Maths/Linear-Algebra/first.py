import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,40,100)

d_r = 2.5*t
d_p = 3*(t-5)

fig, ax  = plt.subplots()
plt.title = ("A Bank Robber Caught")
plt.xlabel = ("Time (in minutes)")
plt.ylabel = ("Distence (in kms)")
ax.set_xlim(0,40)
ax.set_ylim(0,100)
ax.plot(t,d_r, c='red')
ax.plot(t,d_p, c='green')
plt.axvline(x=30, color='purple', linestyle='--')
plt.axhline(y = 75, color='purple', linestyle='--')

plt.show()