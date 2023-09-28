#Part A
import random 
weeks = 16
classes = 5
tuition = 6000
var = 5
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = ((classes / weeks))
cost_per_class = ((cost_per_week / classes_per_week))
print(cost_per_class, "is cost per class")
print(cost_per_class, type(cost_per_class), classes_per_week, type(classes_per_week), cost_per_week, type(cost_per_week))
var = [15, "Computer Science", 13.3, "Nice", 1500]
create = random.choice(var)
print(create)