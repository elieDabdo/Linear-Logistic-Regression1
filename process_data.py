import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

def clean(file, out, split):
    if ".xlsx" in file:
        dataframe = pd.read_excel(file)
        #compute statistics for numerical data
        dataframe["Y1"].hist(bins = 50)
        mean = dataframe["Y1"].mean()
        std = dataframe["Y1"].std()
        plt.title('Y1 Output Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["Y2"].hist(bins = 50)
        mean = dataframe["Y2"].mean()
        std = dataframe["Y2"].std()
        plt.title('Y2 Output Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X1"].hist(bins = 20)
        mean = dataframe["X1"].mean()
        std = dataframe["X1"].std()
        plt.title('X1 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X2"].hist(bins = 20)
        mean = dataframe["X2"].mean()
        std = dataframe["X2"].std()
        plt.title('X2 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X3"].hist(bins = 20)
        mean = dataframe["X3"].mean()
        std = dataframe["X3"].std()
        plt.title('X3 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X4"].hist(bins = 20)
        mean = dataframe["X4"].mean()
        std = dataframe["X4"].std()
        plt.title('X4 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X5"].hist(bins = 20)
        mean = dataframe["X5"].mean()
        std = dataframe["X5"].std()
        plt.title('X5 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X6"].hist(bins = 20)
        mean = dataframe["X6"].mean()
        std = dataframe["X6"].std()
        plt.title('X6 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X7"].hist(bins = 20)
        mean = dataframe["X7"].mean()
        std = dataframe["X7"].std()
        plt.title('X7 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        dataframe["X8"].hist(bins = 20)
        mean = dataframe["X8"].mean()
        std = dataframe["X8"].std()
        plt.title('X8 Feature Distribution')
        plt.xlabel('Value (mean: {}, std: {})'.format(mean, std))
        plt.ylabel('Count')
        plt.show()
        #standardization to make features have mean of 0, std. dev of 1
        #formula is x_std = (x - mean) / std
        for column in dataframe.columns:
            if "Y" in column: continue
            mean = dataframe.loc[:, column].mean()
            std = dataframe.loc[:, column].std()
            dataframe.loc[:, column] = dataframe.loc[:, column].map(lambda x : (x-mean)/std)
    else:
        dataframe = pd.read_csv(file, header=None)
        #compute statistics for discrete data
        dataframe[6].hist(bins = 3)
        plt.title('Class Distribution')
        plt.xlabel('Class')
        plt.ylabel('Count')
        plt.show()
        
        dataframe[0].value_counts().plot(kind='bar')
        plt.title('Industrial Risk Feature Distribution')
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.show()
        dataframe[1].value_counts().plot(kind='bar')
        plt.title('Management Risk Feature Distribution')
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.show()
        dataframe[2].value_counts().plot(kind='bar')
        plt.title('Financial Flexibility Feature Distribution')
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.show()
        dataframe[3].value_counts().plot(kind='bar')
        plt.title('Credibility Feature Distribution')
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.show()
        dataframe[4].value_counts().plot(kind='bar')
        plt.title('Competitiveness Feature Distribution')
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.show()
        dataframe[5].value_counts().plot(kind='bar')
        plt.title('Operating Risk Feature Distribution')
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.show()
    dataframe = dataframe.sample(frac=1).reset_index(drop=True) 
    print(dataframe)
    length = len(dataframe)
    with open(out + "_train.sav", 'wb') as handle:
        pickle.dump(dataframe[:int(length*split)], handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open(out + "_test.sav", 'wb') as handle:
        pickle.dump(dataframe[int(length*split):], handle, protocol=pickle.HIGHEST_PROTOCOL)
    


classification_file = "raw_datasets\Qualitative_Bankruptcy.data.txt"
regression_file = "raw_datasets\ENB2012_data.xlsx"

clean(classification_file, "clean_data/Qualitative_Bankruptcy", 0.8)
clean(regression_file, "clean_data/ENB2012_data", 0.8)