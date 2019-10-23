import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('AITA Morality Survey.csv', header = 0 )

# Store all column names into lists for simple use
#Empty dict to store column names and values in
cols = {}
#loop through each column name in the dataframe
for k in df.keys():
    cols[k] = []
    for v in df[k]:
        if v not in cols[k]:
            cols[k].append(v)

# value = list of column values (e.g. 'very liberal, liberal, etc')
#data = dataframe
# col = column header
#count_pol: output bar chart for input factors
def graph(data, col, colors= ['blue'], name ='default'):
    shape_list = []
    for v in cols[col]:
        # create series containing whether or not each column is true or false based on value passed
        is_value = data[col] == v
        #create a dataframe containing only rows that contain the passed value
        val_df = data[is_value]
        #append number of rows in the dataframe to a list
        shape_list.append(val_df.shape[0])
    plt.figure(figsize=(15,7.5))
    plt.barh(cols[col], shape_list, color = colors)
    plt.title(col)
    plt.xlabel = 'Responses'
    #Uncomment below to save graphs as an image
    #plt.savefig(name + '.png')
    plt.show()

while True:
    column = input('Please input the name of a column in the AITA database')
    if column in df.keys():
        graph(df, column)
    else:
        print("That column isn't in the database, please try again")
        continue
