import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('haberman.csv')
df.columns = ["age", "operation_year", "aln", "survival_status"]
# here aln = axillary_lymph_node (Doctor ni bhasha)
df.head()

print(df)
