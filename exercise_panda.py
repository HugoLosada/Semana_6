import pandas as pd
import matplotlib.pyplot as plt

data = {
     'years': ['2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014'],
    'goals': [8,17,16,38,47,53,73,60,41]
 }

df = pd.DataFrame(data)

#sns.lineplot(data=df, x='years', y='goals')
plt.plot(df['years'], df['goals'])
plt.xlabel('years')
plt.ylabel('goals')
plt.title('Messi goals per year')
plt.show()