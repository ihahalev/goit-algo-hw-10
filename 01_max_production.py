import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
L = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
F = pulp.LpVariable('Fruit Juice', lowBound=0, upBound=10, cat='Integer')

# Функція цілі (Максимізація прибутку)
model += L + F, "Production"

model += 2*L + F <=100, "Water"
model += L <=50, "Sugar"
model += L <=30, "Lemon Juice"
model += 2*F <=40, "Fruit Puree"

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print("Виробляти Лимонаду:", L.varValue)
print("Виробляти Фруктового соку:", F.varValue)
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")
