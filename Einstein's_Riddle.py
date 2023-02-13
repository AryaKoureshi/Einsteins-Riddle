# Hints
# 1. مرد انگلیسی در خانه قرمز زندگی میکند.
# 2. مرد سوئدی سگ دارد.
# 3. نوشیدنی مورد علاقه مرد دانمارکی چای است.
# 4. خانه سبز رنگ سمت چپ خانه سفید رنگ است.
# 5. صاحب خانه سبز رنگ قهوه مینوشد.
# 6. مردی که سیگار پالمال میکشد پرنده نگهداری میکند
# 7. صاحب خانه زرد رنگ سیگار دانهیل میکشد.
# 8. مردی که در خانه وسطی زندگی میکند نوشیدنی مورد علاقه اش شیر است.
# 9. مرد نروژی در اولین خانه زندگی میکند.
# 10. مردی که سیگار بلندز میکشد همسایه مردی است که گربه دارد.
# 11. مردی که اسب دارد همسایه مردی است که سیگار دانهیل میکشد.
# 12. مردی که سیگار بلومستر میکشد آبجو مینوشد.
# 13. مرد آلمانی سیگار پرنس میکشد.
# 14. مرد نروژی در همسایگی کسی است که خانه اش آبی رنگ است.
# 15. مردی که سیگار بلندز میکشد همسایه ای دارد که نوشیدنی مورد علاقه اش آب است.

from constraint import *

def showSolution(solution):
    for i in range(1,6):
        print("House {}".format(i))
        print("--------")
        print("Nationality: {}".format(solution["nationality{}".format(i)]))
        print("Color: {}".format(solution["color%d" % i]))
        print("Smoke: {}".format(solution["smoke%d" % i]))
        print("Drink: {}".format(solution["drink%d" % i]))
        print("Pet: {}".format(solution["pet%d" % i]))
        print("\n")
            
problem = Problem()
for i in range(1,6):
    problem.addVariable("color%d" % i, ["قرمز", "سفید", "سبز", "زرد", "آبی"])
    problem.addVariable("nationality%d" % i, ["انگلیسی", "سوئدی", "دانمارکی", "نروژی", "آلمانی"])
    problem.addVariable("smoke%d" % i, ["پالمان", "دانهیل", "بلندز","بلومستر", "پرنس"])
    problem.addVariable("drink%d" % i, ["چای", "قهوه", "شیر", "آبجو", "آب"])
    problem.addVariable("pet%d" % i, ["سگ", "پرنده", "گربه", "اسب", "ماهی"])

problem.addConstraint(AllDifferentConstraint(), ["color%d" % i for i in range(1,6)])
problem.addConstraint(AllDifferentConstraint(), ["nationality%d" % i for i in range(1,6)])
problem.addConstraint(AllDifferentConstraint(), ["drink%d" % i for i in range(1,6)])
problem.addConstraint(AllDifferentConstraint(), ["smoke%d" % i for i in range(1,6)])
problem.addConstraint(AllDifferentConstraint(), ["pet%d" % i for i in range(1,6)])

for i in range(1,6):

    # Hint 1
    problem.addConstraint(lambda nationality, color:
                          nationality != "انگلیسی" or color == "قرمز",
                          ("nationality%d" % i, "color%d" % i))
    # Hint 2
    problem.addConstraint(lambda nationality, pet:
                          nationality != "سوئدی" or pet == "سگ",
                          ("nationality%d" % i, "pet%d" % i))
    # Hint 3
    problem.addConstraint(lambda nationality, drink:
                          nationality != "دانمارکی" or drink == "چای",
                          ("nationality%d" % i, "drink%d" % i))

    # Hint 4
    if i < 5:
        problem.addConstraint(lambda colora, colorb:
                              colora != "سبز" or colorb == "سفید",
                              ("color%d" % i, "color%d" % (i+1)))
    else:
        problem.addConstraint(lambda color: color != "green",
                              ("color%d" % i,))
    # Hint 5
    problem.addConstraint(lambda color, drink:
                          color != "سبز" or drink == "قهوه",
                          ("color%d" % i, "drink%d" % i))
    # Hint 6
    problem.addConstraint(lambda smoke, pet:
                          smoke != "پالمان" or pet == "پرنده",
                          ("smoke%d" % i, "pet%d" % i))
    # Hint 7
    problem.addConstraint(lambda color, smoke:
                          color != "زرد" or smoke == "دانهیل",
                          ("color%d" % i, "smoke%d" % i))
    # Hint 8
    if i == 3:
        problem.addConstraint(lambda drink: drink == "شیر",
                              ("drink%d" % i,))
    # Hint 9
    if i == 1:
        problem.addConstraint(lambda nationality:
                              nationality == "نروژی",
                              ("nationality%d" % i,))
    # Hint 10
    if 1 < i < 5:
        problem.addConstraint(lambda smoke, peta, petb:
                              smoke != "بلندز" or peta == "گربه" or
                              petb == "گربه",
                              ("smoke%d" % i, "pet%d" % (i-1),
                               "pet%d" % (i+1)))
    else:
        problem.addConstraint(lambda smoke, pet:
                              smoke != "بلندز" or pet == "گربه",
                              ("smoke%d" % i,
                               "pet%d" % (i == 1 and 2 or 4)))
    # Hint 11
    if 1 < i < 5:
        problem.addConstraint(lambda pet, smokea, smokeb:
                              pet != "اسب" or smokea == "دانهیل" or
                              smokeb == "دانهیل",
                              ("pet%d" % i, "smoke%d" % (i-1),
                               "smoke%d" % (i+1)))
    else:
        problem.addConstraint(lambda pet, smoke:
                              pet != "اسب" or smoke == "دانهیل",
                              ("pet%d" % i,
                               "smoke%d" % (i == 1 and 2 or 4)))
    # Hint 12
    problem.addConstraint(lambda smoke, drink:
                          smoke != "بلومستر" or drink == "آبجو",
                          ("smoke%d" % i, "drink%d" % i))
    # Hint 13
    problem.addConstraint(lambda nationality, smoke:
                          nationality != "آلمانی" or smoke == "پرنس",
                          ("nationality%d" % i, "smoke%d" % i))
    # Hint 14
    if 1 < i < 5:
        problem.addConstraint(lambda nationality, colora, colorb:
                              nationality != "نروژی" or
                              colora == "آبی" or colorb == "آبی",
                              ("nationality%d" % i, "color%d" % (i-1),
                               "color%d" % (i+1)))
    else:
        problem.addConstraint(lambda nationality, color:
                              nationality != "نروژی" or
                              color == "آبی",
                              ("nationality%d" % i,
                               "color%d" % (i == 1 and 2 or 4)))
    # Hint 15
    if 1 < i < 5:
        problem.addConstraint(lambda smoke, drinka, drinkb:
                              smoke != "بلندز" or
                              drinka == "آب" or drinkb == "آب",
                              ("smoke%d" % i, "drink%d" % (i-1),
                               "drink%d" % (i+1)))
    else:
        problem.addConstraint(lambda smoke, drink:
                              smoke != "بلندز" or drink == "آب",
                              ("smoke%d" % i,
                               "drink%d" % (i == 1 and 2 or 4)))
solutions = problem.getSolutions()
print("Found {} solution(s)!".format(len(solutions)))
for solution in solutions:
      print(showSolution(solution))