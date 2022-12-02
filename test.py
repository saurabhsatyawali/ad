import pandas as pd
dict1={
  "name":["ram","mohan","sunil"],
  "marks":[89,7,87],
  "city":["delhi","mumbai","goa"]
}
df=pd.DataFrame(dict1)
df['name'][0]="ram changdra"
df.index=['first','second','third']
df.to_csv('new.csv')
