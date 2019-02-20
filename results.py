
from questions import *
import itertools


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


def hamm(text_1, text_2):
    '''
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    '''
    result = 0
    for i in range(len(text_1)):
        if text_1[i] != text_2[i]:
            result += 1
    return result


assert hamm(*hamm_variables) == hamm_result


def perm(n):
    '''
    Given: A positive integer n≤7.
    Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
    '''
    start_list = list(range(1, n + 1))
    temp = list(itertools.permutations(start_list))
    result = str(len(temp)) + "\n"
    for i in temp:
        result += " ".join(map(str, i)) + "\n"

    return result

# print(perm(7))


def find_all(input_text, sub_string):
    result = []
    for i in range(len(input_text)):
        start = input_text.find(sub_string, i)
        if start == -1:
            break
        if start + 1 not in result:
            result.append(start + 1)
    result = " ".join(map(str, result))
    return result


assert find_all(*subs_variables) == subs_result


def gc_content(input_text):
    '''
    Taking string and checking G and C percentage
    :param input_text: string
    :return: float
    '''
    result = 0
    for i in input_text:
        if i == "C" or i == "G":
            result += 1
    if len(input_text) > 0:
        dna_text_len = len(input_text.replace("\n", ""))
        return result/dna_text_len * 100
    else:
        return 0

def gc_percent(input_text):
    '''
    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
    Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated
    '''
    start = 0
    result = {}
    biggest_gc = 0
    biggest_name = ""
    while True:
        start = input_text.find(">", start)
        if start == -1:
            break
        end = start + 14
        next_str = input_text.find(">", start + 1)
        if next_str == -1:
            next_str = len(input_text)
        dna_text = input_text[end + 1:next_str]
        dna_gc_content = gc_content(dna_text)
        result[input_text[start + 1:end]] = [dna_text, dna_gc_content]
        if biggest_gc < dna_gc_content:
            biggest_gc = dna_gc_content
            biggest_name = input_text[start + 1:end]
        start += len(dna_text)
    biggest_gc = '%.6f' % round(biggest_gc, 6)
    return f"{biggest_name}\n{biggest_gc}"


assert gc_percent(gc_variable) == gc_result


RNA_CODON_DATA = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y",
    "UAC": "Y", "UAA": "Stop", "UAG": "Stop", "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W", "CUU": "L",
    "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A",
    "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G",
    "GGA": "G", "GGG": "G",
}

def translation_to_protein(input_text):
    '''
    Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
    Return: The protein string encoded by s.
    '''
    start = 0
    result = ""
    while True:
        end = start + 3
        if end > len(input_text):
            break
        temp = input_text[start:end]
        if temp in RNA_CODON_DATA:
            if RNA_CODON_DATA[temp] == "Stop":
                break
            result += RNA_CODON_DATA[temp]
        else:
            break
        start += 3
    return result


assert translation_to_protein(prot_variable) == prot_result


MONOISOTOPIC_MASS_TABLE = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333,

}


def weight_protein(input_text):
    '''
    Given: A protein string input_text
    Return: The total weight of P.
    :param input_text: string
    :return: float
    '''
    result = 0
    for i in input_text:
        if i in MONOISOTOPIC_MASS_TABLE:
            result += MONOISOTOPIC_MASS_TABLE[i]
    return round(result, 3)


assert weight_protein(prtm_variable) == prtm_result


def fib_rabbit(n, k):
    '''
    Given: Positive integers n≤40 and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in
    each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)
    :param n: integer, number of months
    :param k: integer, produced litter
    :return: integer, number o pairs
    '''
    if n < 1:
        return 0
    elif n == 1:
        return 1

    return (fib_rabbit(n - 2, k) * k) + fib_rabbit(n - 1, k)


assert fib_rabbit(*fib_variables) == fib_result


def fib_rabbit_lived(n, m=1):
    # if n < 1:
    #     return 0
    # elif n == 1:
    #     return 1
    # if n <= m:
    #     return fib_rabbit_lived(n - 2, m) + fib_rabbit_lived(n - 1, m)
    # elif n == m + 1:
    #     return fib_rabbit_lived(n - 2, m) + fib_rabbit_lived(n - 1, m) - 1
    # return fib_rabbit_lived(n - 2, m) + fib_rabbit_lived(n - 1, m) - fib_rabbit_lived(n - (m + 1), m)

    #code above is usless, for high numbers its too slow

    #code below is not mine
    ages = [1] + [0]*(m-1)
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)


assert fib_rabbit_lived(*fibd_variables) == fibd_result
