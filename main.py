import modul

if __name__ == '__main__':
    while True:
        print("____KALKULATOR____")
        a = int(input("Podaj liczbę 1\n"))
        b = int(input("Podaj liczbę 2\n"))
        wybor = input("Co chcesz zrobić? \n 1=dodawanie \n 2=odejmowanie\n 3=mnozenie \n 4=dzielenie\n coś innego = wyjdź \n")
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
            case _:
                print("\nWychodzenie...\n")
                quit()


