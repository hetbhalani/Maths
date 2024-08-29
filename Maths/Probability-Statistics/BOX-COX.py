from scipy import stats
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211)
x = stats.loggamma.rvs(5, size=500) + 5
prob = stats.probplot(x,dist=stats.norm, plot=ax1)
ax1.set_xlabel('')
ax1.set_title('BOX-COX')
plt.show()