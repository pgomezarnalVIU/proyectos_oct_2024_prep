#numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
#print(sorted(numbers))

#El diccionario
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
sorted_people = dict(sorted(people.items()))
print(sorted_people)

#Ordenar por elemento
sorted_alph_people = dict(sorted(people.items(),key=lambda item:item[1]))
print(sorted_alph_people)

#Ordenar por elemento + asc/desc
sorted_alph_people_reverse = dict(sorted(people.items(),key=lambda item:item[1],reverse=True))
print(sorted_alph_people_reverse)

