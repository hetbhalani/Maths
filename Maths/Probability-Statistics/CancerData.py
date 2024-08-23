import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('haberman.csv')
df.columns = ["age", "operation_year", "aln", "survival_status"]
# here aln = axillary_lymph_node (Doctor ni bhasha)

df['survival_status'] = df['survival_status'].map({1:'yes', 2:'no'})
# to replace data

print(df['survival_status'].value_counts())
# yed and no count

status_yes = df[df['survival_status'] == 'yes']
print(status_yes.describe())
status_no = df[df['survival_status'] == 'no']
print(status_no.describe())
# to print data of yes/no

df.head()
# print(df.describe())
# print(df)

plt.grid(True)
sns.FacetGrid(df,hue='survival_status', height=5).map(sns.distplot, 'age').add_legend()
plt.show()