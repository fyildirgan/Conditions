# break& continue& while
# Döngülerle birlikte kullanılan bu yapılar program akışında akışı kesmeye ya da ilgili şart gözlemlendiğinde akışa o
# şartı atlayarak devam etmeye ya da bir koşul sağlandığı sürece çalışmayı sürdürmeyi yarayan ifadelerdir.

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    if salary == 3000:
        break
    print(salary)
#Out = 1000,2000: İlgili koşul sağlandığı program kendini durdurdu.

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)
#Out = 1000,2000,4000,5000: İlgili koşul geldiğinde çalışma devam et.

#while. dı sürece
number = 1
while number < 5:
    print(number)
    number += 1
