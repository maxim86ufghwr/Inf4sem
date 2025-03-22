def r(forward_num):
    '''из обратной в польскую'''
    if len(forward_num) > 3:
        cut = 0
        last_operator = [forward_num[len(forward_num) - 1]]
        count_n = 0
        wh_uper_2 = []
        last_1 = 0
        for i in forward_num[:-1]:
            if i[0] in '0123456789':
                count_n += 1
            else:
                count_n -= 1
            wh_uper_2.append(count_n)
            if count_n==1:
                last_1 = len(wh_uper_2)
        return last_operator + r(forward_num[:last_1]) + r(forward_num[last_1:-1])
    elif len(forward_num) == 3:
        return [forward_num[2], forward_num[0], forward_num[1]]
    return forward_num
n = input()
t = True
nums = ['']
ops = ['077777']
last = 0
j = 0
main = 0
while j < len(n):
    if n[j] in '1234567890':
        if last == 1:
            print(f'Ошибка: введено два числа подряд')
            t = False
            break
        dop = ''
        while j < len(n) and n[j] in '1234567890':
            dop += n[j]
            j += 1
        j -= 1
        last = 1
        nums.append(dop)
    if n[j] == '(':
        main += 1000
    elif n[j] == ')':
        if main < 0:
            print('Ошибка: Закрывающая скобка не имеет пары')
            break
        main -= 1000
    elif n[j] in '*+-/':
        if last < 1:
            print('Ошибка: нет операнда перед оператором')
            t = False
            break
        if n[j] == '+':
            w = main + 1
        elif n[j] == '/':
            w = main + 2
        elif n[j] == '*':
            w = main + 3
        else:
            w = main
        if int(ops[len(ops)-1][1:]) < w:
            ops.append(n[j] + str(w))
        else:
            while len(ops) > 1 and int(ops[len(ops) - 1][1:]) > w:
                nums.append(ops[len(ops) - 1][0])
                ops.pop(len(ops)-1)
            ops.append(n[j] + str(w))
        last = -1
    j += 1
if main > 0 and t:
    print('Ошибка: Есть лишние открытые скобки')
elif last == -1:
    print('Ошибка: Есть лишний знак')
elif t:
    nums.pop(0)
    ops.pop(0)
    ops = ops[::-1]
    nums += ops
    ans = 'обратная польская: '
    for i in nums:
        if i != '' and i[0] in '0123456789':
            ans += i + ' '
        elif i[0] in '+-*/':
            ans += i[0] + ' '
        else:
            ans += i
    print(ans)
    ar = ans.split(' ')
    ar.pop(0)
    ar.pop(0)
    ar.remove('')
    print(ar)
    rrr = 'прямая польская запись: '
    j = r(ar)
    for i in j:
        rrr += i + ' '
    print(rrr, sep='\n')
