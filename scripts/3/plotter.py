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
colorsFocus = {
    'gpt-4.1': '#74AA9C',
    'llama3.1:8b': '#1877F2',
    'Progress-aware': '#74AA9C',
    'Binary': '#CD5C5C'
}
styledTitles = {
    'fusion': 'Fusion',
    'protostar': 'Protostar',
    'nebula': 'Nebula',
    'ropemporium': 'ROPEmporium',
    'webforpentester': 'Web for Pentester I',
    'ProgressBinary': 'Progress-aware KPI vs. Binary KPI'
}

def plotterFocus(data, labels, vm):
    mul = -0.25
    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(18, 3), layout="constrained")
    handles = []
    
    for model, scores in data.items():
        print(model, scores)

        for ix, level in enumerate(scores, 0):
            print(level, scores[level])

            vplot = ax.violinplot(scores[level], positions=[ix+mul], orientation='vertical', showmeans=False, showmedians=False)

            for pc in vplot['bodies']:
                pc.set_facecolor(colorsFocus[model])

            for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
                if partname in vplot:
                    vp = vplot[partname]
                    vp.set_color(colorsFocus[model])
                    vp.set_linewidth(2) # Optional: make the lines a bit thicker
            
            plt.scatter([ix+mul]*len(scores[level]), scores[level], c=colorsFocus[model])
            
        mul *= -1
    
    ax.set_ylabel("$S = L_a/L_o$")
    if vm != 'ProgressBinary':
        ax.set_title(styledTitles[vm])

    if vm == 'webforpentester':
        legend_elem = [Patch(facecolor=colorsFocus['gpt-4.1'], edgecolor='black', label='GPT-4.1'),
                       Patch(facecolor=colorsFocus['llama3.1:8b'], edgecolor='black', label='LLaMA3.1:8b')]
        
        ax.legend(loc='upper left', ncols=2, bbox_to_anchor=(0,-.8), labels=['GPT-4.1', 'LLaMA3.1:8b'], handles=legend_elem)
    elif vm == 'ProgressBinary':
        legend_elem = [Patch(facecolor=colorsFocus['Progress-aware'], edgecolor='black', label='Progress-aware'),
                       Patch(facecolor=colorsFocus['Binary'], edgecolor='black', label='Binary')]
        
        ax.legend(loc='best', ncols=2, labels=['Progress-Aware KPI', 'Binary KPI'], handles=legend_elem)

    ax.set_xticks(x, labels, rotation=45, ha="right", rotation_mode="anchor")

    ax.yaxis.set_minor_locator(MultipleLocator(0.25))

    for x in range(len(labels)):
        if x % 2:
            ax.axvspan(x-0.5, x+0.5, color='grey', alpha=0.1)

    ax.set_ylim(-0.1, 1.1)
    ax.set_xlim(-0.5, len(labels)-0.5)
    ax.grid(visible=True, which='both', axis='y', alpha=0.3)
    ax.grid(visible=True, which='both', axis='x', alpha=0.3)

    plt.savefig(f"../plots/Focus{vm.capitalize()}.pdf", format='pdf', dpi=300, bbox_inches='tight')

def plotFocusNebula():
    df = pd.read_csv("../results/nebula.csv")

    labels = [f'{x.capitalize()}' for x in  df.Level.unique()]
    data = {
        'gpt-4.1': {},
        'llama3.1:8b': {},
    }

    df = df[df['Model'].isin(['gpt-4.1', 'llama3.1:8b'])]
    
    for run in range(1,6):
        df[f'Perc{run}'] = df[f'Run_{run}']/df['Steps']
        # df[f'Perc{run}'].replace({np.float64(0.0): np.nan}, inplace=True)
        df[f'Perc{run}'] = df[f'Perc{run}'].round(2)  
 

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt-4.1', 'llama3.1:8b']:
            data[model][level] = [dfLevel[dfLevel['Model'] == model][f'Perc{x}'].values[0] for x in range(1,6)]

    plotterFocus(data, labels, 'nebula')

def plotFocusProtostar():
    df = pd.read_csv("../results/protostar.csv")

    labels = [f'{x.capitalize()}' for x in  df.Level.unique()]
    data = {
        'gpt-4.1': {},
        'llama3.1:8b': {},
    }

    df = df[df['Model'].isin(['gpt-4.1', 'llama3.1:8b'])]
    
    for run in range(1,6):
        df[f'Perc{run}'] = df[f'Run_{run}']/df['Steps']
        # df[f'Perc{run}'].replace({np.float64(0.0): np.nan}, inplace=True)
        df[f'Perc{run}'] = df[f'Perc{run}'].round(2)  
 

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt-4.1', 'llama3.1:8b']:
            data[model][level] = [dfLevel[dfLevel['Model'] == model][f'Perc{x}'].values[0] for x in range(1,6)]

    plotterFocus(data, labels, 'protostar')

def plotFocusROPEmporium():
    df = pd.read_csv("../results/ropemporium.csv")

    labels = [f'{x.capitalize()}' for x in  df.Level.unique()]
    data = {
        'gpt-4.1': {},
        'llama3.1:8b': {},
    }

    df = df[df['Model'].isin(['gpt-4.1', 'llama3.1:8b'])]
    
    for run in range(1,6):
        df[f'Perc{run}'] = df[f'Run_{run}']/df['Steps']
        # df[f'Perc{run}'].replace({np.float64(0.0): np.nan}, inplace=True)
        df[f'Perc{run}'] = df[f'Perc{run}'].round(2)  
 

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt-4.1', 'llama3.1:8b']:
            data[model][level] = [dfLevel[dfLevel['Model'] == model][f'Perc{x}'].values[0] for x in range(1,6)]

    plotterFocus(data, labels, 'ropemporium')

def plotFocusWebForPentester():
    df = pd.read_csv("../results/webforpentester.csv")

    labels = [f'{x.capitalize()}' for x in  df.Level.unique()]
    data = {
        'gpt-4.1': {},
        'llama3.1:8b': {},
    }

    df = df[df['Model'].isin(['gpt-4.1', 'llama3.1:8b'])]
    
    for run in range(1,6):
        df[f'Perc{run}'] = df[f'Run_{run}']/df['Steps']
        # df[f'Perc{run}'].replace({np.float64(0.0): np.nan}, inplace=True)
        df[f'Perc{run}'] = df[f'Perc{run}'].round(2)  
 

    for level in df.Level.unique():
        dfLevel = df[df.Level == level]
        for model in ['gpt-4.1', 'llama3.1:8b']:
            data[model][level] = [dfLevel[dfLevel['Model'] == model][f'Perc{x}'].values[0] for x in range(1,6)]

    plotterFocus(data, labels, 'webforpentester')

if __name__ == '__main__':
    plotFocusNebula()
    plotFocusProtostar()
    plotFocusROPEmporium()
    plotFocusWebForPentester()
