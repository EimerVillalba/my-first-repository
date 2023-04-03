
num_list = []

num = 1
num_count = int(input('cuantos números quiere comparar => '))

while num <= num_count:
    nums_input = int(input('ingresa un numero => '))
    num_list.append(nums_input)
    num += 1

print('el número mas grande es', max(num_list))
print('\n')
print('y el número mas pequeño es ', min(num_list))


#FUNCIÓN max = maximo
#FUNCIÓN min = mínimo