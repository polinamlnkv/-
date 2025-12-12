import sys
import math

class BekvadratRoots:
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.roots = []

    def get_coef(self, index, prompt):
        while True:
            try:
                if len(sys.argv) > index:
                    coef_str = sys.argv[index]
                else:
                    coef_str = input(prompt + " ")
                coef = float(coef_str.replace(",", "."))
                return coef
            except ValueError:
                print("Ошибка: введите число заново.")
    def get_coefs(self):
        self.A = self.get_coef(1, "Введите коэффициент A:")
        self.B = self.get_coef(2, "Введите коэффициент B:")
        self.C = self.get_coef(3, "Введите коэффициент C:")


    def solve(self):

        a, b, c = self.A, self.B, self.C


        D = b*b - 4*a*c

        if D < 0:
            return

        elif D == 0:
            y = -b / (2*a)
            self.add_roots_from_y(y)

        else:
            sqrt_D = math.sqrt(D)
            y1 = (-b + sqrt_D) / (2*a)
            y2 = (-b - sqrt_D) / (2*a)
            self.add_roots_from_y(y1)
            self.add_roots_from_y(y2)

    def add_roots_from_y(self, y):
        if y < 0:
            return
        elif y == 0:
            self.roots.append(0.0)
        else:
            sqrt_y = math.sqrt(y)
            self.roots.append(sqrt_y)
            self.roots.append(-sqrt_y)

    def print_roots(self):
        if not self.roots:
            print("Нет действительных корней")
        elif len(self.roots) == 1:
            print(f"Один корень: {self.roots[0]}")
        else:
            print("Корни уравнения: " + ", ".join(str(r) for r in self.roots))

def main():
    solver = BekvadratRoots()
    solver.get_coefs()
    solver.solve()
    solver.print_roots()


if __name__ == "__main__":
    main()
