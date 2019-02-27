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

catch_sign_change_variable_1 = [1, 3, 4, 5]
catch_sign_change_variable_2 = [1, -3, -4, 0, -1, 5]
catch_sign_change_variable_3 = [15, -47, 84, -30, -11, -5, 74, 77]
catch_sign_change_variable_4 = []
catch_sign_change_variable_5 = [-47, 84, -30, -11, -5, 74, 77]

catch_sign_change_result_1 = 0
catch_sign_change_result_2 = 4
catch_sign_change_result_3 = 4
catch_sign_change_result_4 = 0
catch_sign_change_result_5 = 3

get_pin_variable_1 = "8"
get_pin_variable_2 = "11"
get_pin_variable_3 = "369"

get_pin_result_1 = ['5', '7', '8', '9', '0']
get_pin_result_2 = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
get_pin_result_3 = ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296",
                    "259", "368", "638", "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696",
                    "269", "358", "656", "698", "699", "298", "236", "239"]

sudoku1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [2, 3, 4, 5, 6, 7, 8, 9, 1],
           [3, 4, 5, 6, 7, 8, 9, 1, 2],
           [4, 5, 6, 7, 8, 9, 1, 2, 3],
           [5, 6, 7, 8, 9, 1, 2, 3, 4],
           [6, 7, 8, 9, 1, 2, 3, 4, 5],
           [7, 8, 9, 1, 2, 3, 4, 5, 6],
           [8, 9, 1, 2, 3, 4, 5, 6, 7],
           [9, 1, 2, 3, 4, 5, 6, 7, 8]]

sudoku2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 5, 3, 4, 8],
           [1, 9, 8, 3, 4, 2, 5, 6, 7],
           [8, 5, 9, 7, 6, 1, 4, 2, 3],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 6, 1, 5, 3, 7, 2, 8, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 4, 5, 2, 8, 6, 1, 7, 9]]

sudoku3 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 5, 3, 4, 8],
           [1, 0, 0, 3, 4, 2, 5, 6, 7],
           [8, 5, 9, 7, 6, 1, 4, 2, 3],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 6, 1, 5, 3, 7, 2, 8, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 4, 5, 2, 8, 6, 1, 7, 9]]

parentheses_three_1 = '{[()]}'
parentheses_three_2 = '{[(])}'
parentheses_three_3 = '{{[[(())]]}}'
parentheses_three_4 = '{{[[(())]]}})'

sock_merchant_variables = [9, [10, 20, 20, 10, 10, 30, 50, 10, 20]]
