from code_wars_questions import *


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
