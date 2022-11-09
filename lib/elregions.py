import h5py
import matplotlib.pyplot as plt
import geopandas as gpd
from pandas import concat


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

def create_elregDF():
    GAMSregions =  get_GAMSregions()  # Get dict of regions
    path    = "../data/NUTS_RG_01M_2021_4326_LEVL_2.json"
    gdf     = gpd.read_file(path)
    elregDF = None    # Start with empty variable
    for key, item in GAMSregions.items():

        for nutsID in item:
            gdf_reg = gdf[gdf.NUTS_ID == nutsID]
            gdf_reg = gdf_reg.assign(gamsID=key)
            
            try:
                elregDF = concat([elregDF,gdf_reg])
            except AttributeError:
                
                elregDF = gdf_reg
    return elregDF

path    = "../data/NUTS_RG_01M_2021_4326_LEVL_2.json"
elregDF = create_elregDF()

# Set current projection and project to Mercator
elregDF = elregDF.set_crs("EPSG:4326")
elregDF = elregDF.set_crs(epsg=4326)
elregDF.to_crs("EPSG:3395")

fig, ax = plt.subplots(1, 1, figsize=(6,4))
ax=elregDF.plot(column='gamsID', ax=ax)
ax=elregDF.boundary.plot(color="black",linewidth = 0.1, ax=ax)
ax.set_axis_off()
plt.title = ("Model regions")
plt.savefig('GAMSregions.png')
plt.show()
