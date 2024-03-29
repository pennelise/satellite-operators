import yaml
from interpolation import VerticalGrid
import parser

with open("config.yml", "r", encoding="utf8") as f:
    config = yaml.safe_load(f)


def colocate_pixels(sat_lat, sat_lon, gc_lat, gc_lon):
    pass
    # get gridcells which are coincident with each satellite observation
    # assumes model pixel size >> satellite pixel size


def regrid_gc_to_sat_pixels(sat_lat, sat_lon, gc_lat, gc_lon):
    pass
    # calculate pixels which overlap each satellite observation
    # this is what the IMI does
    # assumes model pixel size is close to satellite pixel size


def get_closest_time(gc_time, sat_time):
    pass
    # get closest times in model to satellite times
    # can potentially use this structure for fast time-matching:
    # sron_v19_df_means["lat"] = np.round(sron_v19_df_means["lat"] / 0.25) * 0.25
    # sron_v19_df_means["lon"] = np.round(sron_v19_df_means["lon"] / 0.3125) * 0.3125


def get_model_columns(
    gc_df,
    satellite_levels,
    centers_or_edges,
    averaging_kernel,
    pressure_weight,
    satellite_lat,
    satellite_lon,
):
    """
    generic function to apply an operator to a satellite
    takes:
        - GEOS-Chem dataframe (not a problem b/c this is standard)
        - all required satellite inputs as np arrays
    """
    # for nobs observations at one time:
    # get closest model time
    # get overlapping pixels
    # get model column on satellite grid
    # apply averaging kernel and pressure weight
    # return model_columns


def apply_operator_to_files(satellite_name, gc_filepath, satellite_filepath):
    """apply one of the default operators to a satellite"""
    # basically a wrapper for get_model_columns which reads in files:
    # read satellite file
    # read model file
    # apply operator
    # return model_columns
    # units & choice of vertical levels in satellite data
    # may make this difficult to do generically
