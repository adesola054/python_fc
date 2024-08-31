# data structures

# 1. list
car_brands = ['bmw','toyota','hyundai',"toyota"]
car_brands.append("skoda")
print(car_brands)
print(type(car_brands))

# 2. tuple
car_brands_tup = ('bmw','toyota','hyundai',"bmw")
print(car_brands_tup.count("toyota"))
print(car_brands_tup.count("toyota"))
print(car_brands_tup.count("hyundai"))
print(car_brands_tup) 
print(type(car_brands_tup))

# 3. set
car_brands_set = {'bmw','toyota','hyundai',"hyundai"}

print(car_brands_set)
print(type(car_brands_set))

# 4. dictionary
student_dict = {'student_name':'najaf','student_rollno':2443, 'student_marks':578}
print(student_dict)
print(type(student_dict))
student_dict.update({'student_name':'kamal'})
print(student_dict)
student_dict.update({'student_marks':654})
print(student_dict)

