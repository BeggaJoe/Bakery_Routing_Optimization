import numpy as np
import pandas as pd

class Delivery:
    def __init__(self):
        
        self.Gebietsdaten = pd.read_csv(r'C:\Users\Juli\Desktop\Jochens Stuff\Uni\Master\WS 20-21\Masterarbeit\Masterarbeit\Bearbeitung\Datengrundlage\Kundenstamm_im_Einzugsgebiet.csv',
                                        delimiter=";", encoding='iso-8859-15')

        self.Ortschaften_Index = {Gebietsdaten["Ortschaft"][i]: (Gebietsdaten["Kategorie"][i], Gebietsdaten["OSM_ID"][i])
                                  for i in range(len(Gebietsdaten))}
        
       

       
    
    

       
