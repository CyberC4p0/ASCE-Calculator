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
frame.pack(pady=15, padx=35, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, text="ASCE Section 1 Method 1", )
title.pack(pady=6, padx=5)

aerodynamic_multiplier_input = customtkinter.CTkEntry(master=frame, placeholder_text="Aerodynamic Multiplier")
aerodynamic_multiplier_input.pack(pady=6, padx=5)

Mg_input = customtkinter.CTkEntry(master=frame, placeholder_text="Mg")
Mg_input.pack(pady=6, padx=5)

Mf_input = customtkinter.CTkEntry(master=frame, placeholder_text="Mf")
Mf_input.pack(pady=6, padx=5)

zone_1 = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 1")
zone_1.pack(pady=6, padx=5)

zone_2e = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 2e")
zone_2e.pack(pady=6, padx=5)

zone_2n = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 2n")
zone_2n.pack(pady=6, padx=5)

zone_2r = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 2r")
zone_2r.pack(pady=6, padx=5)

zone_3 = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 3")
zone_3.pack(pady=6, padx=5)

zone_3e = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 3e")
zone_3e.pack(pady=6, padx=5)

zone_3r = customtkinter.CTkEntry(master=frame, placeholder_text="Zone 3r")
zone_3r.pack(pady=6, padx=5)

def main():

    print("\n--------TABLE VALUES------\n")

    aerodynamic_multiplier = float(aerodynamic_multiplier_input.get())
    Mg = float(Mg_input.get())
    Mf = float(Mf_input.get())

    print("Aerodynamic Multiplier:",aerodynamic_multiplier)
    print("Restoring Moments due to Gravity (Mg):",Mg)
    print("Attachment Resistance Expressed as a Moment (Mf):",Mf)

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

    for zone in zones:
        if zone[1] == 0:
            pass
        else:
            print(zone[0] + ": -" + str(zone[1]))

    print("\n-----------REPORT---------\n")
    
    amount_of_zones = len(zones)

    for zone in zones:
        if zone[1] == 0:
            pass
        else:
            Mr = round((zone[1] * aerodynamic_multiplier) - Mg, 3)
            if Mr <= Mf:
                print(zone[0] + ": ("+str(zone[1]),"x",str(aerodynamic_multiplier),"=",str(zone[1] * aerodynamic_multiplier)+") -",str(Mg),"=",str(Mr),"<=",Mf,OK)

            else:
                print(zone[0] + ":", Mr, "<=", Mf, FAIL)


generate_report = customtkinter.CTkButton(master=frame, text="Generate Report", command=main)
generate_report.pack(pady=6, padx=5)

exit_button = customtkinter.CTkButton(master=frame, text="Exit", command=exit)
exit_button.pack(pady=6, padx=5)

gui.mainloop()
main()
