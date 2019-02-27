from code_wars_questions import *
from datetime import date, timedelta
from itertools import combinations, permutations, product, combinations_with_replacement
import numpy


def balance(book):
    list_text = book.split("\n")
    delete_signs = "!=:?;,{}"
    result = []
    temp = []
    count = 0
    for i in list_text:
        temp_result = ""
        for j in i:
            if j not in delete_signs:
                temp_result += j
        temp.append(temp_result)
    balance = float(temp[0])
    start_balance = balance
    result.append("Original Balance: {:.2f}\r".format(balance))
    for nr, i in enumerate(temp):
        part_result = ""
        if nr > 0:
            if i != "":
                temp = i.split(" ")
                price = float(temp[len(temp) - 1])
                strings = temp[0:len(temp) - 1]
                balance = balance - price
                balance_text = "Balance {:.2f}".format(round(balance, 2))
                part_result += "{} {:.2f} {}\r".format(' '.join(strings), price, balance_text)
                result.append(part_result)
                count += 1
    total_expense = round(abs(balance - start_balance), 2)
    result.append("Total expense  {:.2f}\r".format(total_expense))
    result.append("Average expense  {:.2f}".format(round(total_expense/count, 2)))
    result = "\n".join(result)
    return result


assert balance(balance_variable_1) == balance_result_1
assert balance(balance_variable_2) == balance_result_2


def tribonacci(signature, n):
    result = signature[::]
    for i in range(len(signature), n):
        new_number = result[i - 3] + result[i - 2] + result[i - 1]
        result.append(new_number)
    return result[0:n]


assert tribonacci(*tribonacci_variables_1) == tribonacci_result_1
assert tribonacci(*tribonacci_variables_2) == tribonacci_result_2
assert tribonacci(*tribonacci_variables_3) == tribonacci_result_3
assert tribonacci(*tribonacci_variables_4) == tribonacci_result_4
assert tribonacci(*tribonacci_variables_5) == tribonacci_result_5
assert tribonacci(*tribonacci_variables_6) == tribonacci_result_6
assert tribonacci(*tribonacci_variables_7) == tribonacci_result_7
assert tribonacci(*tribonacci_variables_8) == tribonacci_result_8
assert tribonacci(*tribonacci_variables_9) == tribonacci_result_9


def catch_sign_change(lst):
    #for some reason "0" is positive number
    count = 0
    temp = []
    for i in range(len(lst)):
        if lst[i] >= 0:
            temp.append("+")
        elif lst[i] < 0:
            temp.append("-")
    for nr, i in enumerate(temp):
        if nr > 0:
            if i == "+" and temp[nr - 1] == "-":
                count += 1
            elif i == "-" and temp[nr - 1] == "+":
                count += 1
    return count


assert catch_sign_change(catch_sign_change_variable_1) == catch_sign_change_result_1
assert catch_sign_change(catch_sign_change_variable_2) == catch_sign_change_result_2
assert catch_sign_change(catch_sign_change_variable_3) == catch_sign_change_result_3
assert catch_sign_change(catch_sign_change_variable_4) == catch_sign_change_result_4
assert catch_sign_change(catch_sign_change_variable_5) == catch_sign_change_result_5


def unlucky_days(year):
    count = 0
    days = (date(year, 12, 31) - date(year, 1, 1)).days + 1
    for i in range(days):
        today = date(year, 1, 1) + timedelta(days=i)
        if today.weekday() == 4 and today.day == 13:
            count += 1
    return count


assert unlucky_days(2015) == 3
assert unlucky_days(1986) == 1


#fiboacci with memo
memo = {}


def fibonacci(n):
    if n in memo:
        return memo[n]
    if n in [0, 1]:
        return n
    res = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = res
    return res


assert fibonacci(70) == 190392490709135


# trailing zeros of N!
def zeros(n):
    i = 1
    result = []
    while 5 ** i < n:
        result.append(n // 5 ** i)
        i += 1
    return sum(result)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(1000) == 249
assert zeros(4617) == 1151


def get_pins(observed):
    pin_numbers = {
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": ["3", "5", "6", "9"],
        "7": ["4", "7", "8"],
        "8": ["5", "7", "8", "9", "0"],
        "9": ["8", "6", "9"],
        "0": ["0", "8"],
    }
    result = []
    samples = []
    for i in observed:
        samples.append(pin_numbers[i])
    temp = list(product(*samples))
    for i in temp:
        result.append("".join(i))
    return result


assert sorted(get_pins(get_pin_variable_1)) == sorted(get_pin_result_1)
assert sorted(get_pins(get_pin_variable_2)) == sorted(get_pin_result_2)
assert sorted(get_pins(get_pin_variable_3)) == sorted(get_pin_result_3)


def valid_parentheses(string):
    temp = []
    for i in string:
        if i == "(":
            temp.append(i)
        elif i == ")":
            if len(temp) > 0:
                temp.pop()
            else:
                return False
    if len(temp) == 0:
        return True
    return False


assert valid_parentheses("hi())(") == False
assert valid_parentheses("  (") == False
assert valid_parentheses("") == True
assert valid_parentheses("hi(hi)()") == True


def unpack(l):
    # not mine
    res = []
    for i in l:
        if type(i) is list:
            res += unpack(i)
        elif type(i) is tuple:
            res += unpack(list(i))
        elif type(i) is dict:
            res += unpack(list(i.keys()))
            res += unpack(list(i.values()))
        elif type(i) is set:
            res += unpack(list(i))
        else:
            res += [i]
    return res


def duplicate_count(text):
    text_lower = text.lower()
    temp = []
    result = []
    count = 0
    for i in text_lower:
        cont_res = i in result
        cont_temp = i in temp
        if not cont_res and not cont_temp:
            temp.append(i)
        elif not cont_res and cont_temp:
            count += 1
            result.append(i)
    return count


assert duplicate_count("indivisibility") == 1


def points(games):
    count = 0
    for i in games:
        x = i[0]
        y = i[2]
        if x > y:
            count += 3
        elif x == y:
            count += 1
    return count


def validSolution(board):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # checking rows
    for row in board:
        if sorted(row) != check:
            return False
    # checking columns
    n = 0
    while n < 9:
        column = []
        for i in range(9):
            column.append(board[i][n])
        if sorted(column) != check:
            return False
        n += 1

    # checking 3x3
    np_board = numpy.array(board)
    row_val_1 = 0
    col_val_1 = 3
    row_val_2 = 0
    col_val_2 = 3
    while row_val_2 < 10 and col_val_2 < 10:
        part_board = np_board[row_val_1:col_val_1, row_val_2:col_val_2]
        flat_list = []
        for row in part_board:
            for i in row:
                flat_list.append(i)
        if sorted(flat_list) != check:
            return False
        col_val_1 += 3
        row_val_1 += 3
        if col_val_1 > 9:
            row_val_1 = 0
            col_val_1 = 3
            col_val_2 += 3
            row_val_2 += 3
    return True


assert validSolution(sudoku1) == False
assert validSolution(sudoku2) == True
assert validSolution(sudoku3) == False


def valid_parentheses_three(string):
    data = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    temp = []
    for i in string:
        if i in data.keys():
            temp.append(data[i])
        else:
            if len(temp) == 0:
                return False
            if i == temp[-1]:
                temp.pop()
            else:
                return False
    if len(temp) == 0:
        return True
    return False


assert valid_parentheses_three(parentheses_three_1) == True
assert valid_parentheses_three(parentheses_three_2) == False
assert valid_parentheses_three(parentheses_three_3) == True
assert valid_parentheses_three(parentheses_three_4) == False


def sockMerchant(n, ar):
    done = []
    result = 0
    for i in ar:
        if i not in done:
            temp = [x for x in ar if x == i]
            done.append(i)
            length = len(temp) // 2
            result += length
    return result


assert sockMerchant(*sock_merchant_variables) == 3
