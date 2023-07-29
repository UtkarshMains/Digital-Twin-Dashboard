import json
import pandas as pd
df=pd.read_excel('./data/fixed cost.xlsx', engine='openpyxl')
l=[]
with open("../app/src/fixed_cost.json", "w") as write_file:
    for i in range(len(df)):
        di={}
        for j in df.loc[[i]]:
            if j=="Unnamed: 0":
                k="Country"
            else:
                k=j
            di[k]=str(df[j][i])
        l.append(di)
    json.dump(l, write_file)


