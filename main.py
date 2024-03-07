import modul

if __name__ == '__main__':
    while True:
     try:
        print("____KALKULATOR____")
        a = float(input("Podaj liczbę 1\n"))
        b = float(input("Podaj liczbę 2\n"))
        wybor = input("Co chcesz zrobić? \n 1=dodawanie \n 2=odejmowanie\n 3=mnozenie \n 4=dzielenie\n 5=potegowanie\n 6=zaokraglanie\n coś innego = wyjdź \n")
        match wybor:
            case "1":
                print(f"{a} + {b} = {modul.dodawanie(a,b)}")
                continue;
            case "2":
                print(f"{a} - {b} = {modul.odejmowanie(a,b)}")
                continue;
            case "3":
                print(f"{a} * {b} = {modul.mnozenie(a,b)}")
                continue;
            case "4":
                print(f"{a} / {b} = {modul.dzielenie(a,b)}")
                continue;
            case "5":
                print(f"{a} ** {b} = {modul.potegowanie(a, b)}")
            case "6":
                print(f"{a} zaokrąglone do {b} znaku = {modul.zaokroglanie(a, int(b))}")
            case _:
                print("\nWychodzenie...\n")
                quit()
     except KeyboardInterrupt:
            print("Wyłączanie...")
            quit()
     except Exception:
            print("Błąd... spróbuj ponownie")
            continue


