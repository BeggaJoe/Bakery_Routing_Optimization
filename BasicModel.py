import numpy as np
import pandas as pd

class Delivery:
    def __init__(self):
        
        self.Gebietsdaten = pd.read_csv(r'C:\Users\Juli\Desktop\Jochens Stuff\Uni\Master\WS 20-21\Masterarbeit\Masterarbeit\Bearbeitung\Datengrundlage\Kundenstamm_im_Einzugsgebiet.csv',
                                        delimiter=";", encoding='iso-8859-15')

        self.Ortschaften_Index = {self.Gebietsdaten["Ortschaft"][i]: (self.Gebietsdaten["Kategorie"][i], self.Gebietsdaten["OSM_ID"][i])
                                  for i in range(len(self.Gebietsdaten))}
       
    def give(self, Zahl = 5):
        self.Gebietsdaten[0:Zahl]
    
       
