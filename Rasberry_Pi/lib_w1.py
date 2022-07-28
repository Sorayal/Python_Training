#!/usr/bin/python3
"""Bibliothek zur Verwaltung von DS18B20-Sensoren"""
W1_BASE = "/sys/bus/w1/devices"
Sensor_Namen = {"28-01143bf19baa":"Kaffee-Maschine"}

def Get_Number_Of_Sensors():
    """Ermittelt die Anzahl der Slave-Devices auf dem 1-Wire-Bus."""
    # Anmerkung: die "global" Deklaration ist nicht nötig, dient aber der
    # didaktischen Klarheit - die entsprechende Warnung von Thonny kann
    # daher ignoriert werden
    global W1_BASE
    try:
        with open(W1_BASE+"/w1_bus_master1/w1_master_slave_count", "r") as DATA:
            Anzahl = int(DATA.readline().strip())
    except FileNotFoundError:
        print("Get_Number_Of_Sensors() ist fehlgeschlagen. Ist der W1 aktiv?")
    return Anzahl
    
def Get_Number_Of_TempSensors():
    """Ermittelt die Anzahl der Temperatur-Sensoren auf dem 1-Wire-Bus."""
    global W1_BASE
    Anzahl = 0
    Geraete = []
    try:
        with open(W1_BASE+"/w1_bus_master1/w1_master_slaves", "r") as DATA:
            for Zeile in DATA:
                Geraete.append(Zeile.strip())
    except FileNotFoundError:
        print("Get_Number_Of_Sensors() ist fehlgeschlagen. Ist der W1 aktiv?")
    for i in range(len(Geraete)):
        if Geraete[i][:3] == "28-":
            Anzahl+=1
    return Anzahl
    

def Show_Sensor_Names():
    """\
Zeigt an, welche Sensoren auf dem Bus gefunden wurden. Sind bereits Namen definiert,
werden die Namen angezeigt, andernfalls wird die Sensor-ID ausgegeben."""
    global W1_BASE, Sensor_Namen
    Geraete = []
    with open(W1_BASE+"/w1_bus_master1/w1_master_slaves", "r") as DATA:
        for Zeile in DATA:
            Geraete.append(Zeile.strip())
    print("Die folgenden Geräte wurden gefunden:")
    for i in range(len(Geraete)):
        print(Geraete[i], "\t", Sensor_Namen.get(Geraete[i]))
    return

def Konfig_Sensor_Names():
    """\
Sucht nach Sensoren, denen noch kein Name zugeordnet ist und fragt den Anwender
nach einem aussagekräftigen Namen für das Gerät. Dieser Name wird in dem globalen
Dictionary der Geräte abgespeichert.
"""    
    global W1_BASE, Sensor_Namen
    Geraete = []
    with open(W1_BASE+"/w1_bus_master1/w1_master_slaves", "r") as DATA:
        for Zeile in DATA:
            Geraete.append(Zeile.strip())
    for i in range(len(Geraete)):
        if Sensor_Namen.get(Geraete[i]) == None:
            print("Es wurde ein neues Gerät mit der ID", Geraete[i], "gefunden.")
            Eingabe = input("Bitte einen Namen für das Gerät vergeben: ")
            if Eingabe != "":
                Sensor_Namen[Geraete[i]] = Eingabe
    return

def Write_Config():
    """Speichert die Konfiguration - i.w. die Gerätenamen - in einer Datei"""
    global Sensor_Namen
    with open("TempSensoren.conf", "w") as DATA:
        for g in Sensor_Namen:
            DATA.write(g + ":" + Sensor_Namen[g] + "\n")
    print("Konfiguration aktualisiert.")

def Read_Config():
    """Einlesen der Konfiguration - i.w. der Gerätenamen - aus der Konf.-Datei"""
    global Sensor_Namen
    Sensor_Namen = {}
    with open("TempSensoren.conf", "r") as DATA:
        for DataSet in DATA:
            print(DataSet, "  -  ", DataSet.split(":"))
            Key, Value = DataSet.split(":")
            Sensor_Namen[Key] = Value.strip()
    print("Konfiguration eingelesen.")
    
    
if __name__ == "__main__":
    print("Get_Number_Of_Sensors:", Get_Number_Of_Sensors())
    print("Get_Number_Of_TempSensors:", Get_Number_Of_TempSensors())
    Show_Sensor_Names()
    Konfig_Sensor_Names()
    Show_Sensor_Names()
    Write_Config()
    Sensor_Namen = {}
    Read_Config()
    Show_Sensor_Names()
    