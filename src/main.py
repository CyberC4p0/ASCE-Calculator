from colorama import init, Fore, Back, Style

init(autoreset=True)

OK = Fore.GREEN + " OK"
FAIL = Fore.RED + " FAIL"

print("ASCE Calculator\n")

def main():
  
    zone_1 = int(71)
    zone_2r = int(91)
    zone_2e = int(91)
    zone_3 = int(111)

    zones = [zone_1,zone_2r,zone_2e,zone_3]
    amount_of_zones = len(zones)

    aerodynamic_multiplier = float(0.315)
    Mg = float(7.34)
    Mf = float(45.5)

    for zone in zones:
        Mr = round((zone * aerodynamic_multiplier) - Mg, 3)
        if Mr <= Mf:
            print(Mr, "<=", Mf, OK)

        else:
            print(Mr, "<=", Mf, FAIL)

main()