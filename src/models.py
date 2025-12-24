# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 20:26:55 2025

@author: Tibe
"""

class Trainingset:
    def __init__(self, oefening, gewicht, reps, datum):
        self.oefening = oefening
        self.gewicht = gewicht
        self.reps = reps
        self.datum = datum

    def bereken_volume(self):
        return self.gewicht * self.reps

    def __str__(self):
        totaal = self.bereken_volume()
        return f"{self.datum} | {self.oefening}: {self.reps}x {self.gewicht}kg (Totaal: {totaal}kg)"
    
if __name__ == "__main__":
    
    # 1. Maak een test set
    test_set = Trainingset("Test Oefening", 100, 5, "2024-01-01")
    
    # 2. Controleer de berekening
    print(f"Oefening: {test_set.oefening}")
    print(f"Volume:   {test_set.bereken_volume()} (Verwacht: 500)")
    
    # 3. Controleer de tekstweergave
    print(f"Weergave: {test_set}")