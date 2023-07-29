import json
import pandas as pd
df=pd.read_excel('./data/freight costs.xlsx', engine='openpyxl')
l=[]
with open("../app/src/freight.json", "w") as write_file:
    for i in range(len(df)):
        di={}
        for j in df.loc[[i]]:
            if j=="Freight Costs ($/Container)":
                k="Freight"
            else:
                k=j
            di[k]=str(df[j][i])
        l.append(di)
    json.dump(l, write_file)