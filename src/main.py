# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 10:31:56 2025

@author: Tibe
"""
from database import add_exercise, add_log

def toon_menu():
    print("\n" + "="*30)
    print("   FITNESS LOGGER MENU")
    print("="*30)
    print("1. Nieuwe oefening aanmaken")
    print("2. Training loggen")
    print("3. Bekijk logboek")
    print("4. Stoppen")
    print("-" * 30)

def main():
    print("Welkom bij je Fitness logger!")
    
    while True:
        toon_menu()
        keuze = input("Maak een keuze: ").lower().strip()
        
        if keuze == '1':
            print("\n--- Nieuwe Oefening ---")
            naam = input("Naam van de oefening: ")
            spiergroep = input("Spiergroep: ")
            add_exercise(naam, spiergroep)
            input("\nDruk op Enter om terug te gaan.")
        elif keuze == '2':
            print("\n--- Training Loggen ---")
            naam = input("Welke oefening heb je gedaan?: ")
            try:
                gewicht = float(input("Gewicht (kg): "))
                reps = int(input("Aantal reps: "))
            except ValueError:
                print("Fout: Voer getallen in bij gewicht en reps!")
                continue
            
            datum_input = input("Datum (DD-MM-YYYY): ")
            
            datum = datum_input
            add_log(naam, gewicht, reps, datum)
            input("\nDruk op Enter om terug te gaan...")
        elif keuze == '3':
            print("\n>> Hier komt het overzicht.")
        elif keuze == '4':
            print("\nTot ziens! Goed getraind!")
            break
        else:
            print("\nFout: Dat is geen keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()