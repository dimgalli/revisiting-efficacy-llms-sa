import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Patch
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'],'size': 18})
rc('text', usetex=True)
colors = {
    'gpt': '#74AA9C',
    'llama': '#1877F2',
    'qwen': '#624de9'
}
styledTitles = {
    'fusion': 'Fusion',
    'protostar': 'Protostar',
    'nebula': 'Nebula',
    'ropemporium': 'ROPEmporium',
    'webforpentester': 'Web for Pentester I',
    'ProgressBinary': 'Progress-aware KPI vs. Binary KPI'
}

def plotter(data, labels, vm):
    print(vm)

    mul = 0
    width = 0.30
    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(18, 3), layout="constrained")
    handles = []
    for model, scores in data.items():
        # print(model, scores)
        offset = width * mul
        rects = ax.bar(x + offset, scores, width, label=model, color=colors[model], edgecolor="black")
        
        xss = np.argwhere(np.isnan(scores))
        nulls = [x for xs in xss for x in xs]
        nulls = np.asarray(nulls, dtype=np.int64)

        print(model, nulls)
        print(nulls.searchsorted(6, 'right')-1)

        nullplots = ax.plot(nulls + offset, np.zeros(len(nulls)), 'o', color=colors[model], markeredgecolor='black', markersize=8)
    
        mul += 1
        handles.append(rects)
    
    ax.set_ylabel("$S = L_a/L_o$")
    ax.set_title(styledTitles[vm])

    if vm == 'webforpentester':
        ax.legend(loc='upper left', ncols=3, bbox_to_anchor=(0,-.6), labels=['GPT', 'LLaMA', 'Qwen'], handles=handles)

    ax.set_xticks(x+width, labels, rotation=45, ha="right", rotation_mode="anchor")
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))

    for x in range(len(labels)):
        if x % 2:
            ax.axvspan(x-0.2, x+0.8, color='grey', alpha=0.1)

    ax.set_ylim(0, 1.1)
    ax.set_xlim(-0.2, len(labels)-0.2)

    ax.grid(visible=True, which='both', axis='y', alpha=0.3)
    plt.savefig(f"../plots/{vm}.pdf", format='pdf', dpi=300, bbox_inches='tight')

def plotNebula():
    df = pd.read_csv("../results/nebula.csv")

    labels = [f'{x.capitalize()}' for x in  df.Level.unique()]
    data = {
        'gpt': [],
        'llama': [],
        'qwen': []
    }

    df['Perc'] = df['Run_0']/df['Steps']
    df['Perc'].replace({np.float64(0.0): np.nan}, inplace=True)
    df['Perc'] = df['Perc'].round(2)

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt', 'llama', 'qwen']:
            data[model].append(dfLevel[dfLevel['Model'].str.startswith(model)].Perc.max())

    plotter(data, labels, 'nebula')

def plotProtostar():
    df = pd.read_csv("../results/protostar.csv")
    df.Level = df.Level.str.capitalize()
    labels = df.Level.unique()   

    data = {
        'gpt': [],
        'llama': [],
        'qwen': []
    }
    df['Perc'] = df['Run_0']/df['Steps']
    df['Perc'].replace({np.float64(0.0): np.nan}, inplace=True)
    df['Perc'] = df['Perc'].round(2)


    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt', 'llama', 'qwen']:
            data[model].append(dfLevel[dfLevel['Model'].str.startswith(model)].Perc.max())

    plotter(data, labels, 'protostar')

def plotROPEmporium():
    df = pd.read_csv("../results/ropemporium.csv")
    # df.Level = df.Level.str.capitalize()
    labels = df.Level.unique()   
    
    data = {
        'gpt': [],
        'llama': [],
        'qwen': []
    }

    df['Perc'] = df['Run_0']/df['Steps']
    df['Perc'].replace({np.float64(0.0): np.nan}, inplace=True)
    df['Perc'] = df['Perc'].round(2)

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt', 'llama', 'qwen']:
            data[model].append(dfLevel[dfLevel['Model'].str.startswith(model)].Perc.max())

    plotter(data, labels, 'ropemporium')

def plotWebForPentest():
    df = pd.read_csv("../results/webforpentester.csv")
    # df.Level = df.Level.str.capitalize()
    labels = df.Level.unique()   

    data = {
        'gpt': [],
        'llama': [],
        'qwen': []
    }

    df['Perc'] = df['Run_0']/df['Steps']
    df['Perc'].replace({np.float64(0.0): np.nan}, inplace=True)
    df['Perc'] = df['Perc'].round(2)

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt', 'llama', 'qwen']:
            data[model].append(dfLevel[dfLevel['Model'].str.startswith(model)].Perc.max())

    plotter(data, labels, 'webforpentester')

if __name__ == '__main__':
    plotNebula()
    plotProtostar()
    plotROPEmporium()
    plotWebForPentest()
