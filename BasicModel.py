import numpy as np
import pandas as pd

import geopandas as gpd
from shapely.geometry import Polygon

import networkx as nx
import osmnx as ox

import random
from random import normalvariate

import requests

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

import datetime

class Delivery:
    def __init__(self):
        Kundengebiet = pd.read_csv(r'C:\Users\Juli\Desktop\Jochens Stuff\Uni\Master\WS 20-21\Masterarbeit\Masterarbeit\Bearbeitung\Modellierung\Erweiterung Kunden-Daten\Polygon_Datei_Riesig.csv', delimiter=";", encoding='utf-8')
        lat_point_list = [i for i in Kundengebiet.lat]
        lon_point_list = [i for i in Kundengebiet.lon]
        Kundengebiet_Polygon = Polygon(zip(lon_point_list, lat_point_list))
        crs = {'init': 'epsg:4326'}
        CRS_Kundengebiet_Polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[Kundengebiet_Polygon])
        Gebietsdaten = pd.read_csv(r'C:\Users\Juli\Desktop\Jochens Stuff\Uni\Master\WS 20-21\Masterarbeit\Masterarbeit\Bearbeitung\Datengrundlage\Kundenstamm_im_Einzugsgebiet.csv',
                                   delimiter=";", encoding='iso-8859-15')

        Ortschaften_Index = {Gebietsdaten["Ortschaft"][i]: (Gebietsdaten["Kategorie"][i], Gebietsdaten["OSM_ID"][i])
                             for i in range(len(Gebietsdaten))}

        tags = {'landuse':True}
        Landuse_Polygon = ox.geometries.geometries_from_polygon(Kundengebiet_Polygon, tags)

        self.Gebäude_Koordinaten_Wohngebiete = {}

        for Gebiet in Ortschaften_Index:
            Wohngebiet_Polygon = Landuse_Polygon.geometry[Ortschaften_Index[Gebiet]]

            tags = {'building':True}
            Building_Polygon = ox.geometries.geometries_from_polygon(Wohngebiet_Polygon, tags)

            Koordinaten_Gebäude = []

            for i, Building_ID in enumerate(Building_Polygon.index):

                Koordinaten_Gebäude_Mittelpunkt = [Building_Polygon.geometry[Building_ID].centroid.coords[0][1],
                                                   Building_Polygon.geometry[Building_ID].centroid.coords[0][0]]

                Koordinaten_Gebäude.append(Koordinaten_Gebäude_Mittelpunkt)

            self.Gebäude_Koordinaten_Wohngebiete[Gebiet] = Koordinaten_Gebäude

    self.Gebäude_Koordinaten_Wohngebiete
