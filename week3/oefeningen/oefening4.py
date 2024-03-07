import sys

try:
    sval = input("Geef een getal: ")
    try:
        ival = int(sval)
        ival_double = ival * 2
        print(f"Het dubbele is: {ival_double}")
    except ValueError:
        print("Getal klopt niet")
    except:
        print("Er is IETS misgegaan")
    finally:
        print("Dit komt altijd in beeld")
except KeyboardInterrupt: # Ctrl-C (Windows)
    print("Gebruiker wil stoppen")
    sys.exit(1)
