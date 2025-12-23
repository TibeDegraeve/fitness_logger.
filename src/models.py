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