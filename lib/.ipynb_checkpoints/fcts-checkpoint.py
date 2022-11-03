import numpy as np
import iris
import iris.plot as iplt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import warnings
import pickle
import copy
import sys, os

warnings.filterwarnings("ignore")
plt.ion()
plt.close('all')
nWTs     = 9    # number of weather types
brewer_cmap = plt.get_cmap('brewer_RdBu_11') 
RdBu = plt.get_cmap('brewer_RdBu_11') 
cw = plt.get_cmap('coolwarm') 

def create_filenames(wt):
    """
    Creates filesnames for
    f_wdmean
    f_wdmeantot
    f_std_wdmean
    f_perc_lwd
    f_percmean_lwd
    f_std_perc_lwd
    """
    filepath = '/nobackup/rossby22/sm_ramfu/windenergy_project/clusters/'
    path_wr = "/nobackup/rossby22/sm_elema/weathertypedata/"
    f = {}
    # the files with the daily mean windspeed at 100m associated to every weather type 
    f["f_wdmean"]     = filepath + "mean.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    # total mean of daily mean over the whole time period
    f["f_wdmeantot"]  = path_wr+ "totalmean.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    # standard deviation of every one of them (files contain one timestep, meaning only the standard deviation of mean wind speed at 100m).
    f["f_std_wdmean"] = filepath  + "std.mean.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    #  percentage of the days with wind lower than 4.5m/s associated to every weather type
    f["f_perc_lwd"]   = filepath + "prop_lows.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    #  temporal mean of percentage of the days with wind lower than 4.5m/s associated to every weather type
    f["f_percmean_lwd"] =  path_wr+"totalmean.prop_lows.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    # standard deviation of percentage of the days with wind lower than 4.5m/s associated to every weather type
    f["f_std_perc_lwd"] = filepath +"std.prop_lows.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    # coefficient of variance of the absolute wind speeds per grid point
    f["CoV"]            =  path_wr + "CoV.winds.wt{}.wind_speedm_NEU-3_ECMWF-ERAINT_evaluation_r1i1p1_HCLIMcom-HCLIM38-AROME_x2yn2v1_3hr_1998-2018.nc".format(wt)
    return f



def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()
    

def getwrHCLIM(num):
    """
    Input: WR ERA
    Output. WR HCLIM
    """
    #dict: HCLIM:ERA
    wr = {1:3, 2:9,3:7,4:8,5:4,6:10,7:6,8:2,9:5, 10:1}
    return list(wr.values()).index(num)

def getwrERA(num):
    """
    Input: WR HCLIM
    Output. WR ERA
    """
    #dict: HCLIM:ERA
    wr = {1:3, 2:9,3:7,4:8,5:4,6:10,7:6,8:2,9:5, 10:1}
    return wr[num]
