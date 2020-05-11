import pandas as pd
import os
from argparse import ArgumentParser, FileType
import seaborn as sns
import matplotlib.pyplot as plt

# Setting current working directory
pwd = os.getcwd()

##### File processing
parser = ArgumentParser(epilog=''' This program will plot violin plots for multiple data files''')

parser.add_argument('-fp', '--files_prefix', dest='files_prefix', nargs='?', type=str,
                    help= '''Prefix string of data files and we can generate other files names by looping over number 
                    of files''')

parser.add_argument('-num','--number', dest='num', type=float, nargs='+', help='''Input all the num values
                                                                            to get plots with short axis''')

# parsing all argparse arguments
data = parser.parse_args()

# Declaring empty DataFrame and median list
df_all_num_value = pd.DataFrame()

for num in data.num:

    # This line would generate data files by joining their prefixes and numbers such data_violin_plot_1.00
    file_name = data.files_prefix + "_" + str("{0:.2f}".format(num)) + '.dat'
    # These two lines will fetch data from all input files and arranges in form of tables
    dec = pd.read_csv(file_name, sep='\s+', usecols=[1], skiprows=1, header=None)
    df_all_num_value = pd.concat([df_all_num_value, dec], axis=1, ignore_index=True)

# This line would number each column
df_all_num_value.columns = ["num-1", "num-2", "num-3"]
print(df_all_num_value.head())

# To change the font size in whole grpah
sns.set(font_scale=2.5, style="ticks")
fig, ax = plt.subplots()
fig.set_size_inches(11.0, 8.0)

# Generating violin plot
sns.violinplot(data=df_all_num_value, inner="box", palette="Set2", scale="width", color="Blues", orient="v",  ax=ax)

# Adding labels with string "num-" and wrting needed text on the files.
ax.set_xticklabels([str("{0:.1f}".format(num)) for num in data.num], fontsize=20)
ax.set_ylabel("Values in the data files", fontsize=24, weight='bold')
fig.text(0.015,70,"(a)",fontdict={'fontsize':20})
fig.text(0.5, 0.025, "num-values", ha='center', fontsize=24, weight='bold')

sns.despine(right=True)
# fig.savefig("dist_bw_GAR_NHS_voilin_plot.tiff", dpi=600)
plt.show()
