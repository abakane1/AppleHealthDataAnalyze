import feather
data = feather.read_dataframe("HealthData/data.feather")
data.groupby("type").size()
print (data)