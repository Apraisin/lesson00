grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = sorted(students) #отсортировали

if len(grades) == len(students): #проверка, просто чтобы было =)
    students_GPA = {} #по другому словарь не создавался сам =\ (ну, можно было создать и до if, но зачем он нам нужен, если проверка не прошлась
    for i in range(0, len(grades)): #непридумал ничего умнее и быстрее =)
        students_GPA[students_sort[i]] = sum(grades[i]) / len(grades[i]) #забиваем в словарь имя из отсоритрованных множеств и добавляем к нему среднее значение оценок
    print(students_GPA)
else:
    print("Неверное соотношение имён и списка оценок") #гдето косяк в изночальных списках

#нет, я не проходил второй модуль но писал стенды на ардуинке =) Есть какието варианты сделать оптимальней?

