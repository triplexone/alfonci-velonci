alfonci = 5000000
velonci = 9000000
alfonci_rast = 0.06
rat = 500000
godine = 0

while alfonci < velonci:
    godine += 1
    alfonci += int((alfonci * alfonci_rast))

    if godine % 4 == 0:
        velonci_rast = 0.05
        velonci += int((velonci * velonci_rast)-rat)
    else:
        velonci_rast = 0.02
        velonci += int((velonci * velonci_rast))

    print("Populacija " + str(godine) + ". godine: ")
    print("    Alfonaca ima: " + str(alfonci))
    print("    Velonaca ima: " + str(velonci))

print("Za " + str(godine) + " godina bit će više Alfonaca od Velonaca.")
