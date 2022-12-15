from colorama import init, Fore, Back, Style

init(autoreset=True)

OK = Fore.GREEN + " OK"
FAIL = Fore.RED + " FAIL"

def main():

    print("\n-------PRESSURE ZONES-----\n")
  
    zone_1 = ["Zone 1",int(input("Zone 1: -"))]
    zone_2e = ["Zone 2e",int(input("Zone 2e: -"))]
    zone_2n = ["Zone 2n",int(input("Zone 2n: -"))]
    zone_2r = ["Zone 2r",int(input("Zone 2r: -"))]
    zone_3 = ["Zone 3",int(input("Zone 3: -"))]
    zone_3e = ["Zone 3e",int(input("Zone 3e: -"))]
    zone_3r = ["Zone 3r",int(input("Zone 3r: -"))]

    print("\n-----------REPORT---------\n")

    zones = [zone_1,zone_2r,zone_2e,zone_2n,zone_3,zone_3e,zone_3r] 
    amount_of_zones = len(zones)

    aerodynamic_multiplier = float(0.315)
    Mg = float(7.34)
    Mf = float(45.5)

    for zone in zones:
        if zone == 0:
            pass
        else:
            Mr = round((zone[1] * aerodynamic_multiplier) - Mg, 3)
            if Mr <= Mf:
                print(zone[0] + ":", Mr, "<=", Mf, OK)

            else:
                print(zone[0] + ":", Mr, "<=", Mf, FAIL)

main()
