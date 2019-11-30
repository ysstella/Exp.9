import pandas as pd
data1={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
data2={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
data3={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[80,95,79]}
data4={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
df1=pd.DataFrame(data1,columns=['Student','Math'])
df2=pd.DataFrame(data2,columns=['Student','Electronics'])
df3=pd.DataFrame(data3,columns=['Student','GEAS'])
df4=pd.DataFrame(data4,columns=['Student','ESAT'])
m1=df1.merge(df2)
m2=m1.merge(df3)
m3=m2.merge(df4)
melt=pd.melt(m3,id_vars=['Student'], value_vars=['Math','Electronics','GEAS','ESAT'], var_name='Subject', value_name='Grade')