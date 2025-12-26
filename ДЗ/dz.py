import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)

data = {
    "employee_id": range(1, 21),
    "age": np.random.randint(22, 60, size=20),
    "department": np.random.choice(
        ["IT", "HR", "Finance", "Marketing"], size=20
    ),
    "salary": np.random.randint(50000, 150000, size=20),
    "experience_years": np.random.randint(1, 20, size=20),
    "performance_score": np.round(
        np.random.uniform(2.5, 5.0, size=20), 2
    )
}

df = pd.DataFrame(data)



df.to_csv("employees_dataset.csv", index=False)



print("=== Первые строки ===")
print(df.head(), "\n")

print("=== Информация ===")
print(df.info(), "\n")

print("=== Описательная статистика ===")
print(df.describe(), "\n")

print("=== Средняя зарплата по отделам ===")
print(df.groupby("department")["salary"].mean(), "\n")

print("=== Корреляция зарплаты и стажа ===")
print(df["salary"].corr(df["experience_years"]), "\n")



plt.figure()
plt.scatter(df["experience_years"], df["salary"])
plt.xlabel("Стаж (лет)")
plt.ylabel("Зарплата")
plt.title("Зависимость зарплаты от стажа")
plt.show()
