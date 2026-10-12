def kalkulator():
    print("--- PREPROSTI KALKULATOR ---")
    a = float(input("Vnesite prvo število: "))
    operacija = input("Izberite operacijo (+, -, *, /): ")
    b = float(input("Vnesite drugo število: "))

    if operacija == '+':
        rezultat = a + b
    elif operacija == '-':
        rezultat = a - b
    elif operacija == '*':
        rezultat = a * b
    elif operacija == '/':
        rezultat = a / b if b != 0 else "Napaka: Deljenje z 0!"
    else:
        rezultat = "Napačna operacija!"

    print(f"Rezultat: {rezultat}")

if __name__ == "__main__":
    kalkulator()
# Avtor: Trajche
