# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 10:31:56 2025

@author: Tibe
"""
import csv
from database import add_exercise, add_log, get_recent_logs, create_tables, get_all_logs

def toon_menu():
    print("\n" + "="*30)
    print("   FITNESS LOGGER MENU")
    print("="*30)
    print("1. Nieuwe oefening aanmaken")
    print("2. Training loggen")
    print("3. Bekijk logboek")
    print("4. Exporteer naar CSV")
    print("5. Stoppen")
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
            print("\n--- Laatste 10 Trainingen ---")
            logs = get_recent_logs()

            if not logs:
                print("Je hebt nog geen trainingen gelogd.")
            else:
                print(f"{'Datum':<12} | {'Oefening':<15} | {'Gewicht':<8} | {'Reps'}")
                print("-" * 50)

            for log in logs:
                print(f"{log['date']:<12} | {log['name']:<15} | {log['weight']:<8} | {log['reps']}")

            input("\nDruk op Enter om terug te gaan...")
            
        elif keuze == '4':
            print("\n--- Exporteren naar CSV ---")
            bestandsnaam = input("Bestandsnaam: ")
            if not bestandsnaam.endswith('.csv'):
                bestandsnaam += '.csv'
            
            logs = get_all_logs()
            
            try:
                with open(bestandsnaam, mode='w', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(['Datum', 'Oefening', 'Gewicht', 'Reps'])
                    for log in logs:
                        writer.writerow([log['date'], log['name'], log['weight'], log['reps']])
                
                print(f"Succes! Je data is opgeslagen in '{bestandsnaam}'.")
            except Exception as e:
                print(f"Er ging iets mis: {e}")
            
            input("\nDruk op Enter om terug te gaan...")

        elif keuze == '5':
            print("Programma afgesloten")
            break
        else:
            print("\nFout: Dat is geen optie. Probeer opnieuw.")

if __name__ == "__main__":
    create_tables()
    main()