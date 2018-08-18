import gzip
import pandas as pd
import csv

# input datapath
dpath = ""
# file list
fn_list = "gaia_source_list.dat"
# output file
fn_o = "GDR2_Mgiant_candidate.csv"
fo = open(fn_o,'w')

with open(dpath+fn_list) as fi:
    line = fi.readline()
    df = pd.read_csv(line[:-1], compression='gzip', header=0,    sep=',' , error_bad_lines=False)
    datas = df.query("bp_rp>2.5 & e_bp_min_rp_val<0.2 & phot_g_mean_mag>10 & phot_g_mean_mag<20 & parallax>0 & parallax<0.25")
    datas.to_csv(fo)
    line = fi.readline()
    while (len(line)>0 ):
        df = pd.read_csv(line[:-1], compression='gzip', header=0,    sep=',' , error_bad_lines=False)
        datas = df.query("bp_rp>2.5 & e_bp_min_rp_val<0.2 & phot_g_mean_mag>10 & phot_g_mean_mag<20 & parallax>0 & parallax<0.25")
        datas.to_csv(fo,header=False)
        del datas,df
        line = fi.readline()