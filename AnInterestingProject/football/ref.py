import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def compare_ref_to_avg(df, referee):
    dfRef = df[df['Referee'] == referee]    
    df = df.corr('pearson')
    dfRef = dfRef.corr('pearson')
    return dfRef - df

def plot(df, ref):
    plt.figure(1)
    plt.pcolor(df, cmap='RdBu_r', vmin=-1, vmax=1)
    plt.colorbar()
    plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
    plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
    plt.title('{} convergence from "average" referee'.format(ref))
    plt.show()

def get_data():
    DATA_SET = '../data/E0.csv'
    DATA_SET_1 = '../data/E0 (1).csv'
    DATA_SET_2 = '../data/E0 (2).csv'
    DATA_SET_3 = '../data/E0 (3).csv'
    DATA_SET_4 = '../data/E0 (4).csv'
    
    DATA_SET_C = '../data/EC.csv'
    DATA_SET_C2 = '../data/EC (2).csv'
    DATA_SET_C3 = '../data/EC (3).csv'
    DATA_SET_C4 = '../data/EC (4).csv'
    
    df0 = pd.read_csv(DATA_SET)
    df1 = pd.read_csv(DATA_SET_1)
    df2 = pd.read_csv(DATA_SET_2)
    df3 = pd.read_csv(DATA_SET_3)
    df4 = pd.read_csv(DATA_SET_4)
    
    dfC0 = pd.read_csv(DATA_SET_C)
    dfC2 = pd.read_csv(DATA_SET_C2)
    dfC3 = pd.read_csv(DATA_SET_C3)
    dfC4 = pd.read_csv(DATA_SET_C4)
    
    df = pd.concat([
        df0, 
        df1, 
        df2, 
        df3, 
        df4,
        dfC0, 
        dfC2, 
        dfC3, 
        dfC4
        ])
    df = df[df0.columns]
    return df[df.columns[3:23]]

df = get_data()
df = df[['Referee', 'FTR', 'HY', 'HR', 'AY', 'AR']]
ref_count = df.groupby(['Referee']).count()
refs = ref_count.loc[ref_count['HR'] >= 10].AR.index.unique()
df = df.loc[df['Referee'].isin(refs)]
ref_diff = df.groupby(['Referee']).mean() - df.mean()
p1 = plt.bar(np.arange(len(ref_diff.index)), ref_diff['AY'], color='#d62728');
p2 = plt.bar(np.arange(len(ref_diff.index)), ref_diff['HY']);
plt.legend((p1, p2), ('Away', 'Home'))
#plt.pcolor(ref_diff, cmap='RdBu_r', vmax=1, vmin=-1)
#plt.colorbar()
#plt.yticks(np.arange(0.1, len(ref_diff.index), 1), ref_diff.index)
plt.xticks(np.arange(0.5, len(ref_diff.index)), ref_diff.index, rotation='vertical')
plt.show()

#refs = df.Referee.unique()
#for ref in refs:
#    plot(compare_ref_to_avg(get_data(), ref), ref)



