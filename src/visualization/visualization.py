import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def hist(df: pd.DataFrame):
    plt.style.use('ggplot')

    names = list(df.columns)
    fig, ax = plt.subplots(3,3,figsize=(10, 10), layout='constrained')

    for i,ax in enumerate(ax.flat):
        ax.hist(x=df.iloc[:,i])
        ax.set_title(f'{names[i]}')   
    plt.show()
    
def kde_plot(df: pd.DataFrame):
    names = list(df.columns)

    fig, ax = plt.subplots(4,2,figsize=(10, 15), layout='constrained')
    for i,ax1 in enumerate(ax.flat):
        sns.kdeplot(data=df,
                    x=df.loc[df.Outcome == 0][names[i]],
                    ax=ax1,
                    linestyle="-",
                    label= 'No Diabetes'
                    )
        
        sns.kdeplot(data=df,
                    x=df.loc[df.Outcome == 1][names[i]],
                    ax=ax1,
                    linestyle="--",
                    label = 'Diabetes'
                    )
        #ax1.set_title(names[i])
        ax1.legend(loc='best')
        if i==7:
            break

    plt.show()