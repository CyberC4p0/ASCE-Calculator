# Importing Required Modules
import customtkinter
from colorama import init, Fore, Back, Style
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

gui = customtkinter.CTk()
gui.geometry("600x600")

init(autoreset=True)

OK = Fore.GREEN + " OK"
FAIL = Fore.RED + " FAIL"

frame = customtkinter.CTkFrame(master=gui)
frame.pack(pady=30, padx=70, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, text="ASCE Section 1 Method 1", )
title.pack(pady=12, padx=10)

zone_1 = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 1")
zone_1.pack(pady=12, padx=10)

zone_2e = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 2e")
zone_2e.pack(pady=12, padx=10)

zone_2n = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 2n")
zone_2n.pack(pady=12, padx=10)

zone_2r = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 2r")
zone_2r.pack(pady=12, padx=10)

zone_3 = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 3")
zone_3.pack(pady=12, padx=10)

zone_3e = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 3e")
zone_3e.pack(pady=12, padx=10)

zone_3r = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 3r")
zone_3r.pack(pady=12, padx=10)

def main():

    print("\n-------PRESSURE ZONES-----\n")

    zones = [
            ["Zone 1",int(zone_1.get())],
            ["Zone 2e",int(zone_2e.get())],
            ["Zone 2n",int(zone_2n.get())],
            ["Zone 2r",int(zone_2r.get())],
            ["Zone 3",int(zone_3.get())],
            ["Zone 3e",int(zone_3e.get())],
            ["Zone 3r",int(zone_3r.get())]
            ]

    print("\n-----------REPORT---------\n")
    
    amount_of_zones = len(zones)

    aerodynamic_multiplier = float(0.315)
    Mg = float(7.34)
    Mf = float(45.5)

    for zone in zones:
        if zone[1] == 0:
            pass
        else:
            Mr = round((zone[1] * aerodynamic_multiplier) - Mg, 3)
            if Mr <= Mf:
                print(zone[0] + ":", Mr, "<=", Mf, OK)

            else:
                print(zone[0] + ":", Mr, "<=", Mf, FAIL)


generate_report = customtkinter.CTkButton(master=frame, text="Generate Report", command=main)
generate_report.pack(pady=12, padx=10)

exit_button = customtkinter.CTkButton(master=frame, text="Exit", command=exit)
exit_button.pack(pady=12, padx=10)

gui.mainloop()
main()
