import pandas as pd
data={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
      'Dimension':['Length','Width','Height','Length','Width','Height'],
      'Value':[6,4,2,5,3,4]}
df=pd.DataFrame(data)
messy=df.pivot(index='Box', columns='Dimension', values='Value')