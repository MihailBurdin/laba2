#Задание №4
#x = int(input())

#if x < -20 :
    #print(0,'#Холодно')
#elif -20 < x < 0:
    #print(1,'#Прохладно')
#elif 0 < x < 15:
    #print(2,'#Зябко')
#elif 15 < x < 25:
    #print(3,'#Тепло')
#else  :
    #print(4,'#Жарко')

# Задание №3
def lim_max(nums, limit):
    x = 0
    e = list(nums)
    for i in range(len(e)):
        if e[i] < limit and e[i] > x:
            g = e[i]
    if x == 0:
        return -1
    else:
        return x
z = (10, 20, 30, 40, 50, 60, 70, 80, 100)
print(lim_max(z, 50))

#задание №2
 a = list(set(listt))
    i = 0
    g = 0
    x = 0
    while True:
        if a[i] > a[i + 1]:
            g = a[i]
            a[i] = a[i + 1]
            a[i + 1] = g 
        if a[i] < a[i + 1]:
            x += 1
        else:
            x = 0
        if x == len(a):
            break
    return a 
print(del_rep([19, 2, 1, 2, 17, 1, 5, 3, 4]))

