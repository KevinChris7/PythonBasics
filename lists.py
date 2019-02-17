
cricket = ["msdhoni", "rohit", "pieterson", "ponting", "kohli", ]

print(cricket)
cricket.sort()
print(cricket)
print(cricket[1])
print(cricket.index("msdhoni"))
cricket.append("pant")
print(cricket)
cricket.remove("rohit")
print(cricket)
cricket.insert(3, "abd")
print(cricket)

football = ["ronaldo", "beckham", "kaka", "messi", "ronaldo"]

print(football)
print(football[1:])
print(football[1:3])
print(football.count("ronaldo"))
football.sort()
print(football)
print(football.pop())


sports = cricket.copy()
print(sports)
sports.extend(football)
print(sports)
sports.clear()
