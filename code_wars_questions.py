balance_variable_1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""

balance_result_1 = """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""

balance_variable_2 = """1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""

balance_result_2 = """Original Balance: 1233.00\r
125 Hardware 24.80 Balance 1208.20\r
123 Flowers 93.50 Balance 1114.70\r
127 Meat 120.90 Balance 993.80\r
120 Picture 34.00 Balance 959.80\r
124 Gasoline 11.00 Balance 948.80\r
123 Photos 71.40 Balance 877.40\r
122 Picture 93.50 Balance 783.90\r
132 Tyres 19.00 Balance 764.90\r
129 Stamps 13.60 Balance 751.30\r
129 Fruits 17.60 Balance 733.70\r
129 Market 128.00 Balance 605.70\r
121 Gasoline 13.60 Balance 592.10\r
Total expense  640.90\r
Average expense  53.41"""

tribonacci_variables_1 = [[1, 1, 1], 10]
tribonacci_variables_2 = [[0, 0, 1], 10]
tribonacci_variables_3 = [[0, 1, 1], 10]
tribonacci_variables_4 = [[1, 0, 0], 10]
tribonacci_variables_5 = [[0, 0, 0], 10]
tribonacci_variables_6 = [[1, 2, 3], 10]
tribonacci_variables_7 = [[3, 2, 1], 10]
tribonacci_variables_8 = [[1, 1, 1], 1]
tribonacci_variables_9 = [[300, 200, 100], 0]

tribonacci_result_1 = [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
tribonacci_result_2 = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
tribonacci_result_3 = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
tribonacci_result_4 = [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
tribonacci_result_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tribonacci_result_6 = [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
tribonacci_result_7 = [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
tribonacci_result_8 = [1]
tribonacci_result_9 = []
