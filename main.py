# 1
'''
def all_divisors(number_):
    list_ = []

    for i in range(1, number_+1):
        if number_ % i == 0:
            list_.append(i)

    return list_

print(all_divisors(int(input('Введите число: '))))
'''

# 2
'''
def three_args(var1 = None, var2 = None, var3 = None):
    str_var1 = ''
    str_var2 = ''
    str_var3 = ''

    if var1 != None:
        str_var1 = 'var1 = ' + str(var1)
    if var2 != None:
        str_var2 = ', var2 = ' + str(var2)
    if var3 != None:
        str_var3 = ', var3 = ' + str(var3)

    return '< Переданы аргументы: ' + str_var1 + str_var2 + str_var3 + ' >'


print(three_args(0,None,3))
'''

# 3
'''
def pall(st_):
    st_ = st_.lower()
    
    st_reverse = st_[::-1]
    if st_ == st_reverse:
        return 'Эта строка является палиндромом'
    else:
        return 'Эта строка не является палиндромом'

st = input('Введите строку: ')

print(pall(st))
'''

'''
# 4
def words_frequently_repeat_and_long(string_):
    word_ = string.split()

    words_count = {}

    for i in word_:
        if i in words_count:
            words_count[i] += 1
        else:
            words_count[i] = 1

        word_frequent = max(words_count, key = words_count.get)

        word_long = max(word_, key = len)

        return 'Часто повторяющееся слово: '+word_frequent + '. ' + 'Самое длинное слово: ' + word_long

string = 'My name is Kirill, My favorite coffee is creamy chocolate'

print(words_frequently_repeat_and_long(string))
'''

# 5

#Сложное, не получается у меня.
'''
def matrix_spiral(n_, m_):
    matrix = [[0] * m_ for _ in range(n_)]

    iter = 1

    #while iter <= n_ * m_:
        #for i in range


    return matrix

#n = int(input("Введите количество строк: "))
#m = int(input("Введите количество столбцов: "))

spiral_matrix = matrix_spiral(3, 3)

for row in spiral_matrix:
    print(row)
'''


