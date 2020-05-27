from fuzzy import FuzzySet


def main():
    # cuatro puntos que definen un conjunto difuso
    a = FuzzySet("Func1", 0, 10, 20, 30)
    b = FuzzySet("Func2", 15, 20, 35, 40)
    a.calculoMembresia(25)
    b.calculoMembresia(18)
    print(a)
    print(b)
    print("Resultados de operador OR")
    print(a | b)
    print("Resultados de operador AND")
    print(a & b)


if __name__ == "__main__":
    main()
