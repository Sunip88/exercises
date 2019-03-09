from code_wars_questions import *
from datetime import date, timedelta
from itertools import combinations, permutations, product, combinations_with_replacement
import numpy
from string import ascii_uppercase
from collections import Counter
from string import ascii_lowercase


def balance(book):
    '''
    Takes receipt (book) and returns it cleared and with total expense and average expense
    :param book: string
    :return: string
    '''
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
    '''
    Takes starting list (signature) and returns variation of fibonacci (three numbers are added not two)
     sequence from that list to the Nth number
    :param signature: list of integers
    :param n: integer
    :return: list of integers
    '''
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
    '''
    Catches sign changes in list
    :param lst: list of integers
    :return: integer
    '''
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
    '''
    Counts all friday 13 in given year
    :param year: integer
    :return: integer
    '''
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
    '''
    Gives fibonacci number
    :param n: integer
    :return: integer
    '''
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
    '''
    Gives all possible combinations of pin number with mistake possibilities (pin_numbers)
    :param observed: string
    :return: string
    '''
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
    '''
    Returns True or False if string with parentheses is valid (all parentheses are closed)
    :param string: string
    :return: boolean
    '''
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
    '''
    Counts letters with appears more than once in input
    :param text: string
    :return: integer
    '''
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
    '''
    Return True if sudoku is valid
    :param board: list of lists of integers
    :return: boolean
    '''
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
    '''
    Returns True or False if string with parentheses is valid (all parentheses are closed). Its working with 3 types of
    parentheses {[(
    :param string: string
    :return: boolean
    '''
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
    '''
    Returns number of pairs of numbers
    :param n: length of list (ar)
    :param ar: list of integers
    :return: integer
    '''
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


def students_second_worst(list):
    list.sort(key=lambda x: x[1])

    first = list[0]
    result = []
    for i in list:
        if i[1] != first[1]:
            if result:
                if result[0][1] == i[1]:
                    result.append(i)
            else:
                result.append(i)
    result.sort(key=lambda x: x[0])
    result_str = "\n".join(x[0] for x in result)
    return result_str


assert students_second_worst(students_second_worst_variables) == students_second_worst_result


def validate_uid(input_text):
    alphabet_upper = ascii_uppercase
    numbers = list(range(0, 10))
    test_upper = 0
    test_numbers = 0
    repeat_check = []
    for i in input_text:
        if i in alphabet_upper:
            test_upper += 1
        if i.isdigit():
            number = int(i)
            if number in numbers:
                test_numbers += 1
        if i not in repeat_check:
            repeat_check.append(i)
        else:
            return False
    if test_upper >= 2 and test_numbers >= 3:
        return True
    return False


assert validate_uid("B1CD102354") == False
assert validate_uid("B1CDEF2354") == True


def valid_card_number(input_text):
    only_digits = input_text.replace("-", "")
    if len(only_digits) != 16:
        return False
    first_number = input_text[0]
    correct_line = [4, 9, 14]
    correct_first = ['4', '5', '6']
    correct_signs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    count = 0

    if first_number not in correct_first:
        return False
    for nr, i in enumerate(input_text):
        if i not in correct_signs:
            return False
        if i == '-':
            if nr not in correct_line:
                return False
    for nr, i in enumerate(only_digits):
        if i == only_digits[nr - 1]:
            count += 1
            if count == 3:
                return False
        else:
            count = 0
    return True


assert valid_card_number('5122-2368-7954-3214') == True
assert valid_card_number('4253625879615786') == True
assert valid_card_number('4424424424442444') == True
assert valid_card_number('42536258796157867') == False
assert valid_card_number('4424444424442444') == False
assert valid_card_number('5122-2368-7954 - 3214') == False
assert valid_card_number('44244x4424442444') == False
assert valid_card_number('0525362587961578') == False


def max_value_x(fnc_details, *args):
    all_prod = list(set(product(*args)))
    max_sum = 0
    max_row = []
    for row in all_prod:
        temp_sum = 0
        for i in row:
            temp_sum += i*i
        temp_sum = temp_sum % fnc_details[1]
        if temp_sum > max_sum:
            max_sum = temp_sum
            max_row = row
    return max_sum


assert max_value_x([3, 1000], [2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]) == 206


def diagonalDifference(arr):
    length = len(arr[0])
    temp = []
    temp2 = []
    for i in range(length):
        temp.append(arr[i][i])
        temp2.append(arr[0 + i][(length-1) - i])
    return abs(sum(temp) - sum(temp2))


assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15


def countingValleys(n, s):
    in_vallie = False
    count_vallies = 0
    level = 0

    for i in s:
        if i == 'U':
            level += 1
        else:
            level -= 1

        if not in_vallie:
            if level < 0:
                in_vallie = True
        elif level == 0:
            in_vallie = False
            count_vallies += 1
    return count_vallies

assert countingValleys(12, 'DUDDDUUDUU') == 2


def jumpingOnClouds(c):
    position = 0
    count_moves = 0
    while position != len(c) - 1:
        possible_move_2 = position + 2
        possible_move_1 = position + 1
        if possible_move_2 > len(c) - 1:
            possible_move_2 = possible_move_1
        if c[possible_move_2] == 1:
            if c[possible_move_1] == 1:
                return False
            else:
                position = possible_move_1
                count_moves += 1
        else:
            position = possible_move_2
            count_moves += 1
    return count_moves


assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) == 4
assert jumpingOnClouds([0, 0, 0, 0, 1, 0]) == 3


def repeatedString(s, n):
    numbers_of_string = n // len(s)
    rest_from_string = n % len(s)
    a_letters = s.count("a") * numbers_of_string
    a_rest_letters = s[:rest_from_string].count("a")
    return a_letters + a_rest_letters


assert repeatedString(*repeatedString_variables) == repeatedString_result


def hourglassSum(arr):
    all_list = []
    np_board = numpy.array(arr)
    row_val_1 = 0
    col_val_1 = 3
    row_val_2 = 0
    col_val_2 = 3
    while row_val_2 < 7 and col_val_2 < 7:
        part_board = np_board[row_val_1:col_val_1, row_val_2:col_val_2]
        flat_list = []
        for row in part_board:
            for i in row:
                flat_list.append(i)
        flat_list[3] = 0
        flat_list[5] = 0
        all_list.append(flat_list)
        col_val_1 += 1
        row_val_1 += 1
        if col_val_1 > 6:
            row_val_1 = 0
            col_val_1 = 3
            col_val_2 += 1
            row_val_2 += 1
    return max(sum(i) for i in all_list)


assert hourglassSum(hourglassSum_variable) == 19


def rotLeft(a, d):
    rest_list = a[d:]
    before_list = a[:d]
    rest_list.extend(before_list)
    return rest_list


assert rotLeft([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]


def minimumBribes(Q):
    '''
    returns minimum moves needed from enumerate state to input (Q). Numbers can only move 2 places from enumerate state
    if this rule is broken function returns "Too chaotic"
    :param Q: list of integers
    :return: integer or string(Too chaotic)
    '''
    moves = 0
    for nr, i in enumerate(Q):
        if i - nr > 3:
            return "Too chaotic"
        for j in range(max(i-2, 0), nr):
            if Q[j] > i:
                moves += 1
    return moves


assert minimumBribes([2, 1, 5, 3, 4]) == 3


def arrayManipulation(n, queries):
    n_list = [0] * n
    for i in queries:
        for nr, j in enumerate(n_list[i[0]-1:i[1]]):
            n_list[nr+i[0]-1] += i[2]
    return max(n_list)


array_variable = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

assert  arrayManipulation(5, array_variable) == 200


def checkMagazine(magazine, note):
    '''
    Returns True if magazine have all words given in note
    :param magazine: string
    :param note: string
    :return: boolean
    '''
    splited_magazine = magazine.split()
    splited_note = note.split()
    splited_magazine_dictionary = {}

    for i in splited_magazine:
        if i in splited_magazine_dictionary:
            splited_magazine_dictionary[i] += 1
        else:
            splited_magazine_dictionary[i] = 1
    for i in splited_note:
        if i in splited_magazine_dictionary:
            splited_magazine_dictionary[i] -= 1
            if splited_magazine_dictionary[i] < 0:
                return False
        else:
            return False
    return True


assert checkMagazine(*checkMagazine_variables) == True


def twoStrings(s1, s2):
    for i in s2:
        if i in s1:
            return True
    return False


assert twoStrings('hello', 'world') == True
assert twoStrings('hi', 'world') == False


# def sherlockAndAnagrams(s):
#     list_of_words = []
#     result = 0
#     for i in range(1, len(s)):
#         list_of_words.extend(set(combinations(s, i)))
#     print(list_of_words)
#     for i in list_of_words:
#         temp = "".join(i)
#         if temp == temp[::-1]:
#             result += 1
#     return result


def plusMinus(arr):
    '''
    Returns percentage (in decimal) of positive, negative and zeros in list
    :param arr: list of integers
    :return: string
    '''
    length = len(arr)
    count_more = 0
    count_less = 0
    count_zero = 0
    for i in arr:
        if i > 0:
            count_more += 1
        elif i < 0:
            count_less += 1
        else:
            count_zero += 1
    more = count_more/length
    less = count_less/length
    zero = count_zero/length
    return "{:.6f}\n{:.6f}\n{:.6f}".format(more, less, zero)


# print(plusMinus([-4, 3, -9, 0, 4, 1]))


def staircase(n):
    '''
         #
        ##
       ###
      ####
     #####
    ######
    :param n: integer
    :return: string
    '''
    temp = []
    for i in range(1, n + 1):
        row_stairs = int(n-i) * " " + i * "#"
        temp.append(row_stairs)
    return "\n".join(temp)


# print(staircase(6))


def countTriplets2(arr, r):
    #not mine
    r2 = Counter()
    r3 = Counter()

    count = 0

    for v in arr:
        if v in r3:
            count += r3[v]

        if v in r2:
            r3[v * r] += r2[v]
        r2[v * r] += 1
    return count


assert countTriplets2([1, 2, 4, 8], 2) == 2


def freqQuery(queries):
    '''
    You are given q queries. Each query is of the form two integers described below:
    - (1, x) : Insert x in your data structure.
    - (2, y) : Delete one occurence of y from your data structure, if present.
    - (3, z) : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
    :param queries: list of sets
    :return: list of integers
    '''
    data_list = []
    r2 = Counter()
    result = []
    for i in queries:
        if i[0] == 1:
            data_list.append(i[1])
            r2[i[1]] += 1
        elif i[0] == 2:
            if i[1] in data_list:
                data_list.remove(i[1])
                r2[i[1]] -= 1
        elif i[0] == 3:
            if i[1] in r2.values():
                result.append(1)
            else:
                result.append(0)
    return result


assert freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]) == [0, 1]
assert freqQuery([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]) == [0, 1]
assert freqQuery([(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)]) == [0, 1, 1]
assert freqQuery([(3, 4), (2, 1003), (1, 16), (3, 1)]) == [0, 1]


def countSwaps(a):
    array_sorted = False
    count = 0
    while not array_sorted:
        array_sorted = True
        for nr, i in enumerate(a):
            if nr < len(a) - 1:
                if a[nr] > a[nr + 1]:
                    a[nr], a[nr + 1] = a[nr + 1], a[nr]
                    array_sorted = False
                    count += 1
    return [count, a[0], a[len(a) - 1]]


assert countSwaps([6, 4, 1]) == [3, 1, 6]


def maximumToys(prices, k):
    # prices = sorted(prices)
    array_sorted = False
    length = len(prices) - 1
    result = []
    while not array_sorted:
        array_sorted = True
        i = 0
        while i < length:
            if prices[i] > prices[i + 1]:
                prices[i], prices[i + 1] = prices[i + 1], prices[i]
                array_sorted = False
            i += 1
        length = length - 1
    for i in prices:
        if k - i >= 0:
            result.append(i)
            k = k - i
        else:
            break
    return len(result)


assert maximumToys([1, 12, 5, 111, 200, 1000, 10], 50) == 4


def makeAnagram(a, b):
    a_counter = Counter(a)
    b_counter = Counter(b)
    minus_1 = a_counter - b_counter
    minus_2 = b_counter - a_counter
    return sum(minus_1.values()) + sum(minus_2.values())


def number_needed(a, b):
    count = 0
    for letter in ascii_lowercase:
        ia = a.count(letter)
        ib = b.count(letter)
        count += abs(ia - ib)
    return count


assert makeAnagram('jxwtrhvujlmrpdoqbisbwhmgpmeoke', 'fcrxzwscanmligyxyvym') == 30


def alternatingCharacters(s):
    count = 0
    for nr, i in enumerate(s):
        if nr > 0:
            if s[nr] == s[nr - 1]:
                count += 1
    return count


assert alternatingCharacters('BBBBB') == 4


def isValid(s):
    '''
    Returns bool if string is valid. If frequencies are the same for all letters. Its possible to throw out one letter
    from string
    :param s: string
    :return: bool
    '''
    letters = Counter(s)
    values = Counter(letters.values())
    bugs = 0
    freq = values.most_common(1)[0][0]
    for i in letters:
        if letters[i] != freq:
            bugs += min(abs(letters[i] - freq), letters[i])
            if bugs > 1:
                return False
    return True


assert isValid("aaaaabbbbbcccccdd") == False
assert isValid("aaaaabbbbbcccccd") == True
assert isValid("aabbccddeefghi") == False


def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min = sum(sorted_arr[0:4])
    max = sum(sorted_arr[len(arr) - 4:len(arr)])
    return f"{min}, {max}"

assert miniMaxSum([1, 2, 3, 4, 5]) == "10, 14"


class LinkedList:

    def __init__(self):
        self._first = None
        self._last = None

    def add(self, value):
        new = Node(value)
        if self._first is None:
            self._first = new
        else:
            self._last.next = new
        self._last = new

    def first(self):
        return self._first.value

    def last(self):
        return self._last.value

    def get(self, index=0):
        current_index = 0
        current_node = self._first
        while current_index != index:
            if current_node.next is None:
                raise IndexError()
            current_node = current_node.next
            current_index += 1
        return current_node.value

    def remove(self, last=True):
        if self._first == self._last:
            self._last = self._first = None
        if not last:
            self._first = self._first.next
        else:
            current_node = self._first
            while current_node.next != self._last:
                current_node = current_node.next
            current_node.next = None
            self._last = current_node

    def __iter__(self):
        current_node = self._first
        while current_node:
            yield current_node.value
            current_node = current_node.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# l = LinkedList()
# l.add(1)
# l.add(2)
# l.add(3)
# print(l.first())  # 1
# print(l.get())  # 1
# print(l.get(1))  # 3
# print(l.last())  # 3
# l.remove()  # -> 1, 2
# l.remove(False)  # -> 2
# print(list(l))


def substrCount(n, input_string):
    result = []
    for nr_i in range(n):
        for nr_j in range(n - nr_i):
            part_string = input_string[nr_i:nr_j+nr_i+1]
            if part_string == part_string[::-1]:
                length_string = len(Counter(part_string))
                if length_string < 3:
                    result.append(part_string)
    return len(result)


assert substrCount(7, 'abcbaba') == 10


def dynamicArray(n, queries):
    lists = []
    result = []
    last_answer = 0
    for i in range(n):
        lists.append([])
    for action, sequence_number, value_element in queries:
        index = (sequence_number ^ last_answer) % n
        if action == 1:
            lists[index].append(value_element)
        elif action == 2:
            sequence = lists[index]
            value_place = value_element % len(sequence)
            last_answer = sequence[value_place]
            result.append(last_answer)
    return result


assert dynamicArray(2, [(1, 0, 5), (1, 1, 7), (1, 0, 3), (2, 1, 0), (2, 1, 1)]) == [7, 3]


def left_rotation(n, d, input_list):
    numbers_of = n // d
    rest_of = n % d
    if rest_of == 0:
        return input_list
    for i in range(rest_of):
        temp = input_list.pop()
        input_list.insert(0, temp)
    return input_list

assert left_rotation(5, 4, [1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]
