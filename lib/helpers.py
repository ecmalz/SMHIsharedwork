"""
Helpers function for KLIV_elena project folder
including paths and some multiple used defs
"""
import sys, os
import pickle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


#GISdatapath     = "/home/sm_elema/KLIVEN/data/GISData/"
inddatapath     = "/nobackup/rossby22/sm_elema/KLIV_elena/data/ind_GEGIS/"
winddatapath    = "/nobackup/rossby22/sm_elema/KLIV_elena/data/wind_GEGIS/"
demanddatapath  = "/nobackup/rossby22/sm_elema/KLIV_elena/data/demand_GEGIS/"
solardatapath   = "/nobackup/rossby22/sm_elema/KLIV_elena/data/solar_GEGIS/"
datapath        = "/nobackup/rossby22/sm_elema/KLIV_elena/data/"
GAMSdatapath    = "/nobackup/rossby22/sm_elema/KLIV_elena/data/GAMSresults/"
plotpath        = "/nobackup/rossby22/sm_elema/KLIV_elena/plots/"


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
    path_wr = "/nobackup/rossby22/sm_elema/KLIV_elena/data/weathertypedata/"
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


def save_object(obj, name):
    try:
        with open(name, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
    return 0

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
    return 0

def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()

def get_GAMSregions():
    GAMSregions = {
    "DK1" : ["DK01", "DK02"],
    "DK2" : ["DK03", "DK04", "DK05"],
    "FI"  : ["FI19","FI20", "FI1B", "FI1C", "FI1D" ],
    "SE1" : ["SE22"],
    "SE2" : ["SE11","SE12","SE21","SE23","SE31"],
    "SE3" : ["SE32"],
    "SE4" : ["SE33"],
    "NO1" : ["NO02", "NO08", "NO09", "NO0A"],
    "NO2" : ["NO06"],
    "NO3" : ["NO07"],
    }

    NUT2el = sum(GAMSregions.values(), []) # NUT2 regions included

    return GAMSregions

def get_GISfilename(datainfo):
    if datainfo['model']=="ERA5":
        # historical data
        f = "GISdata_{}wind{}_{}.pkl". \
                    format(datainfo['SP'],datainfo['year'],datainfo['region'])
    else:    
        # rcp scenario data
        f = "GISdata_wind{}_{}_{}_{}_{}.pkl". \
                format(datainfo['SP'],datainfo['region'], datainfo['model'], datainfo['scenario'], datainfo['modelyear'])

    return f

def reg_colors():
    colors={
        "DK1":"aqua",
        "DK2": "blue",
        "SE1":"cornflowerblue",
        "SE2":"slategrey",
        "NO1":"blueviolet",
        "SE3":"coral",
        "SE4":"orange",
        "FI":"firebrick",
        "NO2":"gold",
        "NO3":"tan"
        }
    return colors

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
