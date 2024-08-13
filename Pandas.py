import pandas as pd



print(pd.__version__)




mydataset =["BMW", "Volvo", "Ford"]

myvar = pd.Series(mydataset,index=["1st","2nd","3rd"])

print(myvar)




dataset={"day1":430,"day2":320,"day3":852}
var = pd.Series(dataset)
print(var[0:2])





dataset= {
    "Cars":["BMW","Nissan","Toyota"],
    "MOdel":[2024,2023,1999]
}
df = pd.DataFrame(dataset)
print(df.loc[0])





df = pd.read_json('dwsample1-json.json')

print(df.to_string)




df = pd.read_json("123.json")

print(df)







