import numpy as np
import pandas as pd

class Delivery:
    def __init__():
        
        Gebietsdaten = pd.read_csv(r'https://raw.githubusercontent.com/BeggaJoe/Bakery_Routing_Optimization/main/Kundenstamm_im_Einzugsgebiet.csv',
                                        delimiter=";", encoding='iso-8859-15')

        Ortschaften_Index = {Gebietsdaten["Ortschaft"][i]: (Gebietsdaten["Kategorie"][i], Gebietsdaten["OSM_ID"][i]) for i in range(len(Gebietsdaten))}
       
    def give(Zahl = 5):
        Gebietsdaten[0:Zahl]
    
       
