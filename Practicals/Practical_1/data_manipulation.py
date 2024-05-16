import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv(r"C:\Users\jtbar\Desktop\Semester_1_of_Mechatronic_Engineering\COMP4702\COMP4702_repo\Practicals\Practical_1\pokemonsrt.csv")
# df = df.drop(labels=["percentage_male", "type2"], axis='columns')
# df = df.dropna()

fillMostFrequent = SimpleImputer(missing_values=pd.NA, strategy="most_frequent")
fillMean = SimpleImputer(missing_values=pd.NA, strategy="mean")

for column in df:
    if isinstance(df[column][1], str):
        df[column] = pd.DataFrame(fillMostFrequent.fit_transform(df[column]))
    else :
        df[column] = pd.DataFrame(fillMean.fit_transform(df[column]))



# print(f"{df.head()}\n")
# print(f"{df.info()}\n")
# print(f"{df.isnull().sum()}\n")
# for column in df:
#     print(f"{df[column].describe()}\n")