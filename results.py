from questions import *


#INI2
def f_add(a, b):
    '''
    Given: Two positive integers a and b, each less than 1000.
    Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
    '''
    return a**2 + b**2


assert f_add(*int2_variables) == int2_result


#INI3
def f_str(s, a, b, c, d):
    '''
    Given: A string s of length at most 200 letters and four integers a, b, c and d.
    Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
    In other words, we should include elements s[b] and s[d] in our slice
    '''
    first_word = s[a:b+1]
    secopnd_word = s[c:d+1]
    return f"{first_word} {secopnd_word}"


assert f_str(*int3_variables) == int3_result


#INT4
def f_sum_ods(num_min, num_max):
    '''
    Given: Two positive integers a and b (a<b<10000).
    Return: The sum of all odd integers from a through b, inclusively.
    '''
    temp = 0
    for i in range(num_min, num_max + 1):
        if i % 2 != 0:
            temp += i
    return temp


assert f_sum_ods(*int4_variables) == int4_result


#INT5
def f_ods_lines(input):
    '''
    Given: A file containing at most 1000 lines.
    Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
    '''
    f = open(input, 'r')
    text_lines = f.readlines()
    result = """"""
    for i in range(1, len(text_lines) + 1):
        if i % 2 != 0:
            result += text_lines[i]
    return result


assert f_ods_lines('int5_text.txt') == int5_result


def f_word_apperances(input_text):
    '''
    Given: A string s of length at most 10000 letters.
    Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive,
    and the lines in the output can be in any order.
    '''
    text = input_text.split(' ')
    temp = {}
    result = ""
    for i in text:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1
    for key, val in temp.items():
        result += f"{key} {val}\n"
    return result, temp


assert f_word_apperances(int6_variable)[1] == int6_result


def dna_problem(input_text):
    '''
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times
    that the symbols 'A', 'C', 'G', and 'T' occur in s.
    '''
    temp = {}
    for i in input_text:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1
    return f"{temp['A']} {temp['C']} {temp['G']} {temp['T']}"


assert dna_problem(dna_variable) == dna_result


def dna_rna(input_text):
    '''
    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    '''
    result = ""
    for i in input_text:
        if i == "T":
            result += "U"
        else:
            result += i
    return result


assert dna_rna(rna_variable) == rna_result


def revc(input_text):
    '''
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement s^c of s.
    '''
    text = input_text[::-1]
    result = ""
    for i in text:
        if i == "A":
            result += "T"
        elif i == "T":
            result += "A"
        elif i == "C":
            result += "G"
        elif i == "G":
            result += "C"
    return result


assert revc(revc_variable) == revc_result
