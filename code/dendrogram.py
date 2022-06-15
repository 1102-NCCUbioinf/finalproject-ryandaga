
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Script so useful.')
parser.add_argument("--gene", default = 'Obp')

args = parser.parse_args()
gene_cluster = args.gene

directory = "data/"

dsec_tw_m_df = pd.read_csv(directory + "D. sec - TW - M - R1", sep="\t")
dsec_tw_f_df = pd.read_csv(directory + "D. sec - TW - F - R1", sep="\t")
dsec_jp_m_df = pd.read_csv(directory + "D. sec - JP - M - R1", sep="\t")
dsec_jp_f_df = pd.read_csv(directory + "D. sec - JP - F - R1", sep="\t")
dsim_jp_m_df = pd.read_csv(directory + "D. sim - JP - M - R1", sep="\t")
dsim_jp_f_df = pd.read_csv(directory + "D. sim - JP - F - R1", sep="\t")


dsec_tw_m_df = dsec_tw_m_df[dsec_tw_m_df['gene_id'].notna()]
dsec_tw_f_df = dsec_tw_f_df[dsec_tw_f_df['gene_id'].notna()]
dsec_jp_m_df = dsec_jp_m_df[dsec_jp_m_df['gene_id'].notna()]
dsec_jp_f_df = dsec_jp_f_df[dsec_jp_f_df['gene_id'].notna()]
dsim_jp_m_df = dsim_jp_m_df[dsim_jp_m_df['gene_id'].notna()]
dsim_jp_f_df = dsim_jp_f_df[dsim_jp_f_df['gene_id'].notna()]


dsec_tw_m_df.rename(columns={'gene_short_name': 'gene_name'}, inplace=True)
dsec_tw_f_df.rename(columns={'gene_short_name': 'gene_name'}, inplace=True)
dsec_jp_m_df.rename(columns={'gene_short_name': 'gene_name'}, inplace=True)
dsec_jp_f_df.rename(columns={'gene_short_name': 'gene_name'}, inplace=True)
dsim_jp_m_df.rename(columns={'gene_short_name': 'gene_name'}, inplace=True)
dsim_jp_f_df.rename(columns={'gene_short_name': 'gene_name'}, inplace=True)


dsec_tw_m_df = dsec_tw_m_df[['gene_id', 'gene_name', 'FPKM']]
dsec_tw_f_df = dsec_tw_f_df[['gene_id', 'gene_name', 'FPKM']]
dsec_jp_m_df = dsec_jp_m_df[['gene_id', 'gene_name', 'FPKM']]
dsec_jp_f_df = dsec_jp_f_df[['gene_id', 'gene_name', 'FPKM']]
dsim_jp_m_df = dsim_jp_m_df[['gene_id', 'gene_name', 'FPKM']]
dsim_jp_f_df = dsim_jp_f_df[['gene_id', 'gene_name', 'FPKM']]


dmel_m = pd.read_excel(directory + "D. mel.xlsx")
dmel_m.rename(columns={'Gene ID': 'gene_id', 'Gene Name': 'gene_name'}, inplace=True)
dmel_f = pd.read_excel(directory + "D. mel.xlsx")
dmel_f.rename(columns={'Gene ID': 'gene_id', 'Gene Name': 'gene_name'}, inplace=True)


dmel_m = dmel_m[['gene_id', 'gene_name', 'Male (FPKM)']]
dmel_m.rename(columns={'Male (FPKM)': 'FPKM'}, inplace=True)
dmel_f = dmel_f[['gene_id', 'gene_name', 'Female (FPKM)']]
dmel_f.rename(columns={'Female (FPKM)': 'FPKM'}, inplace=True)

ortho_df = pd.read_csv(directory + "ortho.csv", sep=",")
ortho_df.rename(columns={'#gene': 'gene_name'}, inplace=True)
dsec_dict = dict(zip(ortho_df.Dsec, ortho_df.gene_name))
dmel_dict = dict(zip(ortho_df.Dmel, ortho_df.gene_name))
dsim_dict = dict(zip(ortho_df.Dsim, ortho_df.gene_name))


# Get gene_short_name from the gene_name_dict
dsec_tw_m_df['gene_name'] = dsec_tw_m_df["gene_id"].apply(lambda x: dsec_dict.get(x))
dsec_tw_f_df['gene_name'] = dsec_tw_f_df["gene_id"].apply(lambda x: dsec_dict.get(x))
dsec_jp_m_df['gene_name'] = dsec_jp_m_df["gene_id"].apply(lambda x: dsec_dict.get(x))
dsec_jp_f_df['gene_name'] = dsec_jp_f_df["gene_id"].apply(lambda x: dsec_dict.get(x))
dsim_jp_m_df['gene_name'] = dsim_jp_m_df["gene_id"].apply(lambda x: dsim_dict.get(x))
dsim_jp_f_df['gene_name'] = dsim_jp_f_df["gene_id"].apply(lambda x: dsim_dict.get(x))


dmel_m['gene_name'] = dmel_m["gene_id"].apply(lambda x: dmel_dict.get(x))
dmel_f['gene_name'] = dmel_f["gene_id"].apply(lambda x: dmel_dict.get(x))




dsec_tw_m_df = dsec_tw_m_df[dsec_tw_m_df['gene_name'].notna()]
dsec_tw_f_df = dsec_tw_f_df[dsec_tw_f_df['gene_name'].notna()]
dsec_jp_m_df = dsec_jp_m_df[dsec_jp_m_df['gene_name'].notna()]
dsec_jp_f_df = dsec_jp_f_df[dsec_jp_f_df['gene_name'].notna()]
dsim_jp_m_df = dsim_jp_m_df[dsim_jp_m_df['gene_name'].notna()]
dsim_jp_f_df = dsim_jp_f_df[dsim_jp_f_df['gene_name'].notna()]


dmel_m = dmel_m[dmel_m['gene_name'].notna()]
dmel_f = dmel_f[dmel_f['gene_name'].notna()]


dsec_tw_m_df['species'] = 'Dsec_M_TW'
dsec_tw_f_df['species'] = 'Dsec_F_TW'
dsec_jp_m_df['species'] = 'Dsec_M_JP'
dsec_jp_f_df['species'] = 'Dsec_F_JP'
dsim_jp_m_df['species'] = 'Dsim_M_JP'
dsim_jp_f_df['species'] = 'Dsim_F_JP'
dmel_m['species'] = 'Dmel_M'
dmel_f['species'] = 'Dmel_F'


df_list = [dsec_tw_m_df, dsec_tw_f_df, dsec_jp_m_df, dsec_jp_f_df, dsim_jp_m_df, dsim_jp_f_df, dmel_m, dmel_f]
merged_species = pd.concat(df_list)

merged_species = merged_species[merged_species['gene_name'].notna()]


df_toMap = merged_species.loc[
    (merged_species['gene_name'].str.startswith(gene_cluster, na=False)), ['species', 'gene_name', 'FPKM']]


df_toMap['rank'] = df_toMap.groupby('species')['FPKM'].rank(ascending=True, method='dense', pct=True)

df = df_toMap.pivot(index='gene_name', columns=("species"), values='rank').fillna(0)

# plot with euclidean distance
sns.clustermap(df, metric="euclidean", cmap='autumn_r', yticklabels=True)
plt.savefig(str('results/'+gene_cluster + '_cluster.png'))
plt.show()




