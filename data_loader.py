import pandas as pd

def load_data():
    mylist = []

    for chunk in pd.read_csv('sorted_preprocessed_cyberlen_df.csv', chunksize=20000):
        mylist.append(chunk)

    big_data = pd.concat(mylist, axis=0)
    del mylist
    return big_data

df = load_data()
