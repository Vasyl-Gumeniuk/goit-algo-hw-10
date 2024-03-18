import pulp



# Ініціалізація моделі
model = pulp.LpProblem("Maximize-Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість продукту - Lemonade
fruit_juice = pulp.LpVariable('Fruit-Juice', lowBound=0, cat='Integer')  # Кількість продукту - Fruit juice


# Функція цілі (Максимізація виробництва)
model += lemonade + fruit_juice, "Production"

# Додавання обмежень
model += 2 * lemonade + 1 * fruit_juice <= 100  # Обмеження для води
model += 1 * lemonade <= 50  # Обмеження для цукру
model += 1 * lemonade <= 30  # Обмеження для лимонного соку
model += 2 * fruit_juice <= 40  # Обмеження для фруктового пюре



def main():
    # Розв'язання моделі
    model.solve()

    # Вивід результатів
    print(f"Виробляти продуктів Lemonade: {lemonade.varValue} одиниць")
    print(f"Виробляти продуктів Fruit juice: {fruit_juice.varValue} одиниць")
    print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue} одиниць")



if __name__ == "__main__":
    main()
