#INT2
int2_variables = [979, 927]
int2_result = 1817770

#INT3
int3_variables = ['KThelodermaP4wckekWPqBagJ1SphAARElFs3nqN0XpDmu9G0X4e3u4PBE6ZIaMh9yCoXwDEBP8kW8fOfqrkoGBXp7Adt5Rz3avicularia6RBgvxepl8ZE6oEjLrZpLTJC4rKOwCj7Li1Qmkf0AGKLOLdqK3FSPfn4.',
                  1, 10, 97, 106]
int3_result = 'Theloderma avicularia'

#INT4
int4_variables = [4850, 9104]
int4_result = 14840079

#INT5
int5_result = """Some things in life are bad, they can really make you mad
Other things just make you swear and curse
When you're chewing on life's gristle, don't grumble give a whistle
This will help things turn out for the best
Always look on the bright side of life
Always look on the right side of life
If life seems jolly rotten, there's something you've forgotten
And that's to laugh and smile and dance and sing
When you're feeling in the dumps, don't be silly, chumps
Just purse your lips and whistle, that's the thing
So, always look on the bright side of death
Just before you draw your terminal breath
Life's a counterfeit and when you look at it
Life's a laugh and death's the joke, it's true
You see, it's all a show, keep them laughing as you go
Just remember the last laugh is on you
Always look on the bright side of life
And always look on the right side of life
Always look on the bright side of life
And always look on the right side of life"""

#INT6
int6_variable = """When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"""
int6_result = {'When': 1, 'I': 2, 'find': 1, 'myself': 1, 'in': 4, 'times': 1, 'of': 11, 'trouble': 1, 'Mother': 2,
               'Mary': 2, 'comes': 2, 'to': 3, 'me': 4, 'Speaking': 3, 'words': 7, 'wisdom': 7, 'let': 30, 'it': 36,
               'be': 41, 'And': 3, 'my': 1, 'hour': 1, 'darkness': 1, 'she': 1, 'is': 4, 'standing': 1, 'right': 1,
               'front': 1, 'Let': 6, 'Whisper': 4, 'when': 2, 'the': 4, 'broken': 1, 'hearted': 1, 'people': 1,
               'living': 1, 'world': 1, 'agree': 1, 'There': 4, 'will': 5, 'an': 4, 'answer': 4, 'For': 1, 'though': 1,
               'they': 2, 'may': 1, 'parted': 1, 'there': 2, 'still': 2, 'a': 2, 'chance': 1, 'that': 2, 'see': 1,
               'night': 1, 'cloudy': 1, 'light': 1, 'shines': 1, 'on': 1, 'Shine': 1, 'until': 1, 'tomorrow': 1,
               'wake': 1, 'up': 1, 'sound': 1, 'music': 1, 'yeah': 2}

#DNA
dna_variable = "GGCCTAAACCCGCCCAGATACAATTCACCGACTGCCCGGCAGGAAAGGTTATTCAAGAGGTGTTGACGGTCAATGCCCGAGTCTTGGAGTGGTTCCCACTTCTAGAGGGGCCCAGCGAGGAACCGAAGCTTATCTGGGGACATGGAGTAGCTGAGAGCGGGTCAAATGCCGAGATGACTTTGCGTGTTAGCACGGTTACTGGGACTAGCAGGATCGTTTGGTGTTACATCGAGCGTGCAAGCGGTGGCGTGGCATAGCATCCGAGTGAGCCTAGCATCGACCGGGGAGGCAAAACCACAGTCACAGAAGGACTTGCCCTACGGTCCATGCAGGCCGTTGATGAAGAGTGAGCCTTTGATAATGGGGCCGGATCTTAGTTCTCGGAATGCATGTCCCTGGGGAAAATCTCGGGTGGGCGCACTAGCGAATACCGTTCCGGGTGCATTGGATCATACACACCGTTCATAATAGATATACCCGCACCAGGTAACTTCGGTCAGGAACAAGAGTTCGCGGATGAAAGTTTCAGACAAGGCCTTCTGGAAAACTTGTAGGAAGGTTGCAACCATGAAGGAGACATGGTGTATCTTCTGTGTGGCAAGACATAGAAGCTATCAATTATCTTTTATTCGCTGAACATAACTCCACGACTTCGAACTATAACGCGCCTCTCGTATCTGCGTGGGGTCGCCACTGGCATTTCCTCGAGGTGGCCACAGTTGGGTTGGGGCGAAACAGCCCTCAGCGGGACTCGTCCACAAAGATCGTGAATCCTGGGAAGCACGTCATCGTAGTCCTGAGGCCTCGTCGAAGCCTCTAAGGGATGTCGTCTTTATTAGTAGATAAGACTTTAGTAAAAGGTGGGCCAGGCATGACTGGTG"
dna_result = "218 204 259 200"

#RNA
rna_variable = "ACCTATAACGAATGAGACATGGAGAAGATTCTAACCAACAAATTATCCGTCTATACTCAGTCTAACGTTACCCATCAGGGGCAGACAGCGCAAACCGATTGAGGGCAAATTCCGTTACAATGAACTGTGGTTACCCCCCGCTTTGGCCCTTCTGTGGGCGTAAACAGTTAAAAAATGTGTTTACGGCACGCCCGTGGCCGCTGTTTAAGTTTTGTGCGATTTTTGGGGAACCTAGATACGACCGCATGAAAGGCCAAAAGACAGGCGACATGCTTTTTTGGTGACAGTATGAATTAGACCCTTGCAGTTTTACAGAAAACCCCGGGGCAAGCGTTAACGTAGCTCGCCGTTTATTCGAGGGTACGCTTGCAAGTCAGGGCCACATGAGCGTGCCTGATGCCTCTGCATTTAGCAGAGCCAGGGGAATTGAGCACCGTTCGGTACACTGTGTTACGCCCTGCCATGACTTTCTTTCCAAGTGCTTGACATTTATTTAGATAAGCGTGCAAAATAATGTCTCATTGGGTGTTATTCCAGCAAAAGAAGTGGGGCACGTTTAATAGAAAGCACAGAGGTCGGAGGTTCCGCGTCGTCACGCAGACAGAGCCCATATAGTTCCACTAGGTCCTCGAGGGAGTTAATAGTATGACACATATCTAGCAACGACGCAGGGCACATATCGGGCAATAGCGAAGGCGTCCCGCAACAAAGACATATGGATTCCGGTGATCGACGAGCTAGGTCTTTTATCTCTAATCCCTAGGTTCAGATCGGAAAATATGGGACGGATGTGGGTTGGTTTGCATTCTCTTCTCGTACCAGAAAGACCCACAGGCCAGGATCCGGCGATTCTTGCCGTTCACAATTCCACCGCTCCATCGTCGCTGCTCTTTCACTGCGATTTAGTGCCCGGAGAGGATTTCAGCTCGTGTAGTAATTGACCCCCAGTCGA"
rna_result = "ACCUAUAACGAAUGAGACAUGGAGAAGAUUCUAACCAACAAAUUAUCCGUCUAUACUCAGUCUAACGUUACCCAUCAGGGGCAGACAGCGCAAACCGAUUGAGGGCAAAUUCCGUUACAAUGAACUGUGGUUACCCCCCGCUUUGGCCCUUCUGUGGGCGUAAACAGUUAAAAAAUGUGUUUACGGCACGCCCGUGGCCGCUGUUUAAGUUUUGUGCGAUUUUUGGGGAACCUAGAUACGACCGCAUGAAAGGCCAAAAGACAGGCGACAUGCUUUUUUGGUGACAGUAUGAAUUAGACCCUUGCAGUUUUACAGAAAACCCCGGGGCAAGCGUUAACGUAGCUCGCCGUUUAUUCGAGGGUACGCUUGCAAGUCAGGGCCACAUGAGCGUGCCUGAUGCCUCUGCAUUUAGCAGAGCCAGGGGAAUUGAGCACCGUUCGGUACACUGUGUUACGCCCUGCCAUGACUUUCUUUCCAAGUGCUUGACAUUUAUUUAGAUAAGCGUGCAAAAUAAUGUCUCAUUGGGUGUUAUUCCAGCAAAAGAAGUGGGGCACGUUUAAUAGAAAGCACAGAGGUCGGAGGUUCCGCGUCGUCACGCAGACAGAGCCCAUAUAGUUCCACUAGGUCCUCGAGGGAGUUAAUAGUAUGACACAUAUCUAGCAACGACGCAGGGCACAUAUCGGGCAAUAGCGAAGGCGUCCCGCAACAAAGACAUAUGGAUUCCGGUGAUCGACGAGCUAGGUCUUUUAUCUCUAAUCCCUAGGUUCAGAUCGGAAAAUAUGGGACGGAUGUGGGUUGGUUUGCAUUCUCUUCUCGUACCAGAAAGACCCACAGGCCAGGAUCCGGCGAUUCUUGCCGUUCACAAUUCCACCGCUCCAUCGUCGCUGCUCUUUCACUGCGAUUUAGUGCCCGGAGAGGAUUUCAGCUCGUGUAGUAAUUGACCCCCAGUCGA"

#REVC
revc_variable = "TTACTAGTACGATATTTGCTCTATCCGGGCAAGACCTTGTGATCTGGTCTTGCCGCGTCCCTGGGCTTGCCAGCTACCCACATGCTTTTAGTCAGGGGAACATGAAGGCTAAATCGCGGCGGGTCGTACTTGGTATATTTGCACTCCCGCTGAGACTCCATTTCAAGGCCGCGGTTATACGACCGAAATTGCGCTCGTGAAATCGCCATGTTTGTCATTCATACTTGGTCTGGTTTCGCTCGGGAACACTTGTACACGTGCGCAATGCGTCCTCCTTGAAACGTCTGGTTGTATCCGAACCCCTTTCCCGCCTCTTTTCAGGTCCACCAGATGCCGGAATAGAACTTAGGACAGCTAGCCGGCCATCCTGCTTTCGTTCTCACTAACCCCTGTAAACGATACCCGCATGTGAAGCACGTCGCGTTGTCTAATTCTGCCGATTCCACCTACCCTCGCGTGTGTACTGATGACGCAGCGCCAAGCAGTAAATGAGATCAAACAATCCCCCGTCAAACGTAGGTATCGAGGCCTTATGACGAATACAACTCAAACTCGGAAATGTGTCCGCGGTAGGACGAGGAAAATGGTGGTCCTTAGGAAATATCTTCTCACGACGTCCTTTACGCAAGCGTTCGCTCCACTATGTAAAGCTTCATAGGGTGTTTGACTCATAATTTTTTCTGTCACAACGATTGCCAACAGCAATCGAACGAAGGTGTATAATTTGTACTTGTCGCCTTAAAGTTGACCCGCCTTGAGGTCGCACGGTAGATAGGTGTGCTGAGTGGAGAGTAGCGCGGCGCACACGCCTCAACTCCAGGGGTGGCTAGCCATATAGTTTAGAGCTTACCAATAGCGGTTTCGCTTTCGGGCTTAGCTTCAGCGATGGTCAGTGCAGCCGTCTTCTTACTAAGCCTTCAGAATCCTAACACCGA"
revc_result = "TCGGTGTTAGGATTCTGAAGGCTTAGTAAGAAGACGGCTGCACTGACCATCGCTGAAGCTAAGCCCGAAAGCGAAACCGCTATTGGTAAGCTCTAAACTATATGGCTAGCCACCCCTGGAGTTGAGGCGTGTGCGCCGCGCTACTCTCCACTCAGCACACCTATCTACCGTGCGACCTCAAGGCGGGTCAACTTTAAGGCGACAAGTACAAATTATACACCTTCGTTCGATTGCTGTTGGCAATCGTTGTGACAGAAAAAATTATGAGTCAAACACCCTATGAAGCTTTACATAGTGGAGCGAACGCTTGCGTAAAGGACGTCGTGAGAAGATATTTCCTAAGGACCACCATTTTCCTCGTCCTACCGCGGACACATTTCCGAGTTTGAGTTGTATTCGTCATAAGGCCTCGATACCTACGTTTGACGGGGGATTGTTTGATCTCATTTACTGCTTGGCGCTGCGTCATCAGTACACACGCGAGGGTAGGTGGAATCGGCAGAATTAGACAACGCGACGTGCTTCACATGCGGGTATCGTTTACAGGGGTTAGTGAGAACGAAAGCAGGATGGCCGGCTAGCTGTCCTAAGTTCTATTCCGGCATCTGGTGGACCTGAAAAGAGGCGGGAAAGGGGTTCGGATACAACCAGACGTTTCAAGGAGGACGCATTGCGCACGTGTACAAGTGTTCCCGAGCGAAACCAGACCAAGTATGAATGACAAACATGGCGATTTCACGAGCGCAATTTCGGTCGTATAACCGCGGCCTTGAAATGGAGTCTCAGCGGGAGTGCAAATATACCAAGTACGACCCGCCGCGATTTAGCCTTCATGTTCCCCTGACTAAAAGCATGTGGGTAGCTGGCAAGCCCAGGGACGCGGCAAGACCAGATCACAAGGTCTTGCCCGGATAGAGCAAATATCGTACTAGTAA"

#HAMM
hamm_variables = ['ATGCCTGATTCGTTCTAGGAGTGCGCTCTCCAACAAACGGCGGATCATGTAATTCCACCGTAGGGTAATCGGCCGTTATTGCCGATTCCTGAGGAGTTTTACGTCTACGTAGACGACGACGGTATTAGATGGTTCAGTGCGGTAAAGCCCGACCCTGGAAGTGTGGTGTGATGCATGCGTAAATCTCATTTGTGTTGTCGTAACTGCCAATGTCGACCTATGGAGTATATTTGACGACCGCGGGTACTAATACAGGTCTCCTTGCCACCCTGGACCCGCGCCGGGTAATCATACGGTCACTATTATTTCAACCGAGTTCCTCTCGGATCTGGGTGAGGTGGGATTTATGCTGCCGATGAGTCGGGGAGGCCACTCCCCATCGGCAGGCTGCGTCATATGCTCATCGAATCGGGCTCCTCGTGGTGATCTATGTGGATGCGTTTGATACCCTAGAACGTGAGTTACTCGTCATAAGGCTATAGCGCAACCAGATCTTGAGGAAGAGTTCCAGCGTCGGTCTCTGCTAGAACACATCGTGGCCGTTCCAGACTCCTGAGCCCCCGCTAAAATAACAGCTCCAGTGCTGTCATTCCACGCACAGTGGGAGAACAAAGAATCCAGTCTAGTGTTTTTCGGCGCGCCGAGTAAAGTCTACTTGGGCGGAAGATCGGCGAGTTCTCTGCGGTGCTAGAGAGCAGGGCTAGTTATCCTCAGTAGAAGTCCGATATAACCTGCCAGTGATATAATTCTTCATTATGAGCGGCGATTCGATTTCATTGACAGTCACAGAAGGCAGGTAGGTATCGTTCAACACTGTACGTTCACGAGTCAGACTATTGAACAAAGAGTAATAAATCACCTTGCTTGGACTATGACTAGGTTATTGCCTAATACCAATGGGCCAGTACCGAGCGGGTGTATGTCGAATCATTACACCATCGTTATGTA',
                  'GTGCCTCAGATGTAGTCCGAGCGCCCTGTGCAATAGAGACAGGCTTTATGGGTTTCACCCTACTGATACCCGGGGGTGTCGTAACTACTCGCGAAGTTTTTGCGCTAGCACGATGTGGGCCGCATCAGAAGGTGCATAAAGGGAACACGCGTCAGGGCAATGGGGCTAGAATGTACGATTACTTCATCCTATAGTTACCCTAGTTCCATACGACGACATTCGGAATAGAGTGTCCAACCTCATGGGGCAACGCTCCTATACTTGCCGTGTTGGATAAGCGCTGAGTATTCATAAGATGTCGGGTACTCCTAGATCGTTCCTATAGACTCTTGGATAGGTGCGATATAATGTGCCGCTGGCTCAGTCAAGCAGGTCCTCACTGGACGGCTGCATCTTAAGACTCACGACTTCGGCCTCCTGTGGTACTCTATATAATCCAATGTCATACTCTAGAGATTAGACTGAAACCCGTAATATTATAGCGAAGCGCCATCTAAACCAAGATTCTCCATGTTATTCCCTGCAAGACATAATTGCGAAACTGGCCATCTACCGCGCCCTGAGGTTCATAATACCTGCCGCTCTGTGAATCCCAGCAACAGGGCCACATAGCAATCTGGGTGTCGTTCCCATCTGTCCCCCAATTAAAGCTCCATTCGTCGGTCGAAGCGCGTGGTCCACGTTGTAATGCAAGTCAGAGCATGCTATAATTAATACAAGTCGGTATCAGCGTCTAGATGTATAAATTGTCCAAGATGACCGTGGATACGAGTTAGTCTAGTCAAGTTGAGGGCCTTCTGTTCCCGTGGCACACGGAACTTGCACGACACCGCCTGCATTGCTTTATAATAGAAAGGATCAGGTTTGGACACACAATCGCCCTTTGCTGGCAACCAATGGTCTGCTACCTATCGGCTGTGTGCCTTGACAGTTCAGAAACGGCATCTA']
hamm_result = 464

#SUBS
subs_variables = ['GCGCCTGGGTGTGAGGTGTGATGGTGTGAGGGTGTGACCGGTGTGAACTAGAGGTGTGAGGGTGTGAATGCGAGGTGTGAGGTGTGACAAGTGGTGTGAGGTGTGAGAACGGTGTGAGGTGTGAGGTGTGACGGGTGTGAGGGTGTGAAATGGTGTGACAGGTGTGATAGGTGTGACGGTGTGATGGGTGTGATCCCGGGGTGTGAGGTGTGAGGTGTGATGGGGGTGTGATGGTGTGACGGTGTGACATTCATCGGTGTGAGGTGTGATACCGGAGTCCAAGGTGTGAAGGTGTGATGCAGGTGTGAGGGGGTGTGAGTGGGTGTGAGGTGTGATGGTGTGAGGTGTGAGGTGTGATGTTTAGGTGTGAGGTGTGAATTTGGGTGTGATCACATGAGGTGTGAGGTGTGAGGTGTGAGGTTACCTCGGGTGTGAGGTGTGAGGTGTGATACTATTGTGATGGTGTGAGTGTCATCGGGGTGTGAGTTGGTGTGAAGGTGTGAGGTGTGAGGTGTGAGGTGTGACACGGGTGTGACGGTGTGATTTCGGGTGTGATGACGGTGTGAGGTGTGAGGTGTGAATTCGGATCACGGTGTGATAGGTGTGAGGTGTGAGGGGTGTGAGGTGTGAGTCTGGTGTGAAGAGGGTGTGACATGGTGTGAGTGGGGGTGTGACCTCGGTGTGAGGGTGTGAAAACGGTGTGAACGGGTGTGAAGGTGTGACGGTGTGAAAACGGTGTGAGGGTGTGAGTTGGTGTGAGGTGTGAGGGGTGTGAAGGTGGTGTGATGGTGTGACAGGTGTGAC',
                  'GGTGTGAGG']
subs_result = "8 23 53 74 93 111 118 134 200 207 256 302 322 337 344 364 398 405 412 429 436 497 504 511 560 567 601 608 617 679 735 753 760"

#GC
gc_variable = '''>Rosalind_2643
TGGCGAACTTGCGTATCTGTCTAGCAACCGGCGTATCACCGAGTTCGGAGCTTCCTGTGA
TACATTGGGCCAAAATGTTAGATTCGCTTCTTACATAGTGTGAACATCGGATCAGGAACA
CTAACTAATGGCAAATGTGATTGTCTGCTTTAAGGTACCATTACCTGTAATGTTGTCTTC
AGACCGAATCCTCCACCGATCGCTTCCTCACTCCGCATGACGCGATTGGAATCATCGAAA
ATTGCACCGCATGAGTTTCCCTGAGAAAGGCTTATCCGTGGTCTCCTCGCGCCCGTCTGC
AATGAACACTTTAACACAGGATGCGTAAAACTACACGACGACCGTCACACCATGGTCTAG
CGTCCGGTGAAAGCTTAAAGGCCGATCCCAGAACATAACCGCTGGCCACAACAAATCGCA
TCCGGAAGCCATCCGACCCTCTGCGTAAGCCAACAAACCAATCGTAGACATGTGTGGCGG
TTCAATTGTGAAGAGTCGGACGAGCTTGCATCTTGAGACTCCAGGCGACCCCACCTTTCG
CTTGTGCCCGACTTCTCAAGCTGGAAACGGCTGTACCTGACCGGGAAGCAGACGGAATCT
TCCTCATAACTGTTAAGCCGAGTTATAACAACAGCCGGATGTGTCCATTACCGGATACGC
GTCTATCATGTATGCGCTGGGTTCTCGTTTACAGTCAGCTTACGACAGACACGCTTGACA
ATTCGGCTTTGATCCGTCGTAGCCCATGTGCAAAGTTCCAGTCAATACTAGTTCAGATCA
ACTGAGAACCTCACTGCCGGTGTACGAGAGGAGTGATACAGTGGCGACCGTCACATTAGA
AACATAACTA
>Rosalind_7503
AGAGTCCGCTCTAGCTGCGAACGTCTCTCGCCATCCAGTAGTTGGCGTATTCGATGTTGC
CCGGATCTCGTGGCAGTCTAGAACTGCTAACCGTGCTTTTGATATATCCGTGCTAAGGGT
TCAGCGCAGCAGTTGTGAAATACATGCTTAGCCTTGACCTTAATCCTAAGTGAAGCTAGA
AGGATGTGGAGCCAATAATGCGTGAAGCAGGGTCTCTCCGTTCGCTGCTAGTCAAACGGG
TCCGCCCTCGAACCGGGGGAGACGCAGAATCTATTTTCTCTTTGAACAACGATCTCATGT
ACACTCTCGTTCGCTTGTCCCCGATTCGATGATGCGTTTTGCCCATGCTTGCGGTTGGGG
CCTGAAGGTATATCAAGCGATGAAGAGCCTCGCATTACGCGCATCCCGCCCTGAGACGAC
CCTGGGGTAAGGCCAATCCGCACAAGATGCAATGATGTAGGGCTTTTTTGAGGGTTACGT
GAAACTATCACTCGAGGGTGATCACATCGATAACGTTAAGCAGGCGTGGTGTCTGCAGTG
AGGGAGAAACCGGTCCCTGCCTCGACTAAACGGGGGAATGTTGTCCTGCGACGCGTTACG
TAGACCGATACGGCATCGGATGGTCATATAAGTTCAAAGCGACATAGGATACAGGACGGA
CACGGGACTCTGGGCGCTGAGAGCTAATTAGCCAGGTATCGCTCGGCGAGTTTTCTCGAT
GGGATATCGCGTTAATGACAAAGAGTACCAAGAATATGGTTCAAATGCTCCCTATCTCCA
GCTATCCTTGGGATAAATCTGACAGGCCTCAGCTTACAATCTCTCACGCCCACGCCCGTC
CCCCACTACATACTTCAGTGGTAC
>Rosalind_1205
GTGTCGTAACCGTAACGTCGCTGTCAGGTGACTCGAAGACATTATGAAACGGCACTGAGG
TTGATGCTGCTCTCTACGCCGACGTGAACCGCTAGCACATTACCCCCGCTTAAGTTGTAC
CGCGTGCTTTCGGTCTAAACTCTTACTACCCGTACCAGCCGTGCGTTCACCAACAAGTTG
CGGCTGGCTGAATTCAGAAAGCTGAAAGCTAGAGGGTGGTTCCTTATGCGCGTAGTGACA
GTGTCGTACGCCGTCACAGCTTCCATCCAGCCAATTGTGATAAGCGTTAGAGTGCAGCCA
TCTTTTAATTAATATAATACTTCCCGATTATAACAATACCCTATGTCGGAAGCGCTCCGT
TTTCAACGATCTGGGTTGTATGCATTCAACTGGTCGGCAATGACAAATCCGTACTACGCT
CCACGTGATAAATGCGGCGTGGTCTCATGTGACACGATGTCCTGACCGAGTTAGCTTTCT
ACTAACGCTTGAACTTGACAATATGAAGAATTTGGGTGGCTGACAGAGATTCGCGCACTA
AATCAATCCCCAAGGGTGGAAGTCGTGAGGGGGGGGCTAGCGATCTCTTAAGAATGCCCT
ACGAACAAGACAATCATGATTTCGAAGCGCAGTAAGTGAAGACGTTGGCATCCTCGCCGT
AACGACAGCCTTGAGGATAACCCTAACCAATAAGCTCTATCCACAGTGCGCTGGGATCTA
GCTCACGCCCGATCGACGGGCGTTCACTTCGTAACCTGGAGTAGGCAGGTTTAGCTGAAT
ATTCCTTCACCCCGGGGTTTTAAACGCCATTGGGGATGTACAGACTCCTACTGATCGCAA
CAA
>Rosalind_9478
GAAATGCGGGCTGAGCATTAGTGACTAATACATTCTGATGGTCATAATAGGTGGGCGAAA
ATTAACCGGTGATATTAAACTTCGCCGATGGATGCTAATTCTTATGTGAACTAAGACGAG
AGTTAGCACACAAATGCCACTTCCAGTGGCGGGCCACGGGGAAGTACAGACAACATACAG
TAGACTTCTGTGCTTTGTTTGGGCAAGCATGCCATTTGCACCGCCACACTCACAATAGTG
GGCTGATGGATCCGAGTATTGCTAGCTTAAGACGTCAACGTCCACTTTCGCCTGGCAAAG
GTTAATCCAGGCTGACAGTTGTGCGTCCCGGCCTGCAATTTTGTCTCCCACATCCAAGCT
TTCGTAGCTCTCTACAACCATTCAGCGGTAACCAGTCCATCTATGTGGTACTCGACGAGA
CACCTTAGAGCAGCACGGAAGACCCTCCGGGTAGACATTAACTCTGGCCTCTTAAGCGAA
GGGTCATCCATGCTCAGACGCCGTCACTGTTACGTAAGAAAGTGAGTAGCTATACCGTGA
GTGCTCATCACTCCACCTTCATCGGACCTCGTCCGGTAAAGGGACGCGCATCTGACTGCC
CCTTACATATCTTCAGATCTGTACGGCAGATACCATACGGTGTCACGCGTAGGCTATATT
TGGTTTACTAGCAACCAACGGAGATTCAGGAGTCTCCTACATTATACGGGTGAACAGACC
AATGCACCCAGCCTGCCACGACAAAACGAACCCCGACAGAACCTCAGGATCTTCCTTATG
ATTTTACGCCTAGTGCGTAATCTGCGAGCGCAGCAATTGAAGCCGAATTTCCTCTACG
>Rosalind_9812
TCGACATCAAGCCAGGGGAAGGCACTTCCGCTAGTAGACATAGCACGGCGCCTTAGGCAT
TTTGACTTACGGCTTCTCGCAGGTGACCCCGGATCTGGATGTGGTCAGTTCATCCATGAC
TTTCGTAATTACTAGCGGAAAGAATTAAGTGGCCTTGTAGACCATGTTTTTGTCGCCCAG
TCGTGTAGTACAAGACCGAGTCATTAAGTAGCACCCCTCCTCGTGTTTCTAAGCCTCATC
GTCAGGGGATAGTGCTGCCAAATGATTTATTCCGTACACCATGGTCCGCAACTTGCGGCG
GTGCTTGGACGTGGGTATACTCGATGCGATGTGTAAAACCTTTGAGTCTAACTCTACGGA
AAGCACGTGAAGTCGCTCGAAGACATGCCATATATTACCTTCGCACAAATGTGTACTCGA
CCTCCAAGCGTCTGTGGGTTAGGTGCTAGCTGAACAGACGATCTATCGCCTTCTCGGTGG
GTGACTCAATGTCTCCGTTTGGGGACTTACTCCCGAAGCAAGTGAGTCCTCAGTGAAACT
TGAATTCCCGCTCCTCCACTGAGATTTCAGCAGCATCAATACTGTCATATATAGTCCTTA
GACAAATAGAATTACGTAAGGCACCCGGCCGACAAACAAGAAGCTCTGCACACACGAAAC
AGTCATTACCGAGGAGTTACGGATACCTGCGCATTGGATAGCATACCAATGGAACGGGAA
ACACACCACGTGCTAGTCACTCACTAATCGTATTAGATGACGGACTATATGGGGCCCACG
ACCTTCTGGGAAGCTTCACTCCAGTGAACCTTATGTCAAATAGGATGTCGGAAAGGCGCG
TGGGGCAACGTCACCGCTAACAACTGACCCATGCCTCCAGAAACGTCGCGCCCCAAGACA
CCATTTGCGCTATTGCTCCAATTT
>Rosalind_6850
ACTAATATGGGCCAATTTCTTTCACCATGTGATGAACGTCCGCACCTCGGGGACGCAGCT
CAGTTCGATCGGGCTCAGAAGAGTGCGTCGACGCACCGGGGGTTTCGTGTAGACGCACGA
GATATAGGCACGCTGGCGCGACGACTATACGCACGTAACCACCAAAGATTGGATTACGTC
ACTTGACGCTTCAGACATCCGGTCCCCCTAGCTTCCCGTGTTACCTGGAAGCGATAACGG
GTGTTCTATTAAAGACGGAAGCCAAATTCAGACGCCGTTACGGGTTATAGTTTGGCATAC
GGGCTCAGCGCACTTGTCTCGGTCACGACAGTTTATATTAGTTGCTACTCATGCCTATCC
TCGCATACAGCATGACCGAGGGTGACAATCTTGTCTTTGATATTCAGTCGAATTATGTAG
TGCTGTACGCGCCACCGTGTTCGTACTAAGGTTGATGGTGGTGACCAAACTCCCGTAGAC
TGAAGTGGACGGATCACCAATTTCGGGTCAATTATTGCCGTGCCTCTGACCAGCCCAGAC
ACTCAGGTAGGAATTCTGTCATGTCACACCGATCGTGCGGTATAGCAGAAGGGGTCCACC
AGACGCCAGCACATACTCCTGAAGGGATGTCAGCTCTTGCATGGACCGTAGCGGGCCGAG
AGCAAGCCTCTTGTGACGGGGAATAAGACTTATATTAGTTGATTGGCTTGAAGCTACACG
CAACCACATGGAGTTCATACTGCGTCATCCCACTATGGGCATATTTTGCCAGTCTACTGC
GGGTAAACGTCAATACAATAAATCGTGAGTGTCCAGAACTGCGAAAGATTTCTTGGTCTC
GAGGTGACTGAATCGCCTCTCGCCCACCTGCTAGTGA
>Rosalind_1597
TCACTGCCGAATGAAGGTGTAGAGGGCACGCTGCGTACAGTACTTAGATGCGTGCTTTTC
TGCCAGCCGGGATTGGCCAGTAGTAGGGCCAACACAACACGTCACTTTCCCTTACAAATA
ACGACGATTATCGGTCCTCTCTCCAATTCATCCGTTTTTATGATTTATAGCCAGATGGAG
TCCTGTTATCTCACTAATTGACGGAACTATTGGGCGGTCTTTGCCCTCGAACTGAATCTA
GTGTACCTGTCCTGGTAATGAGATATGCCCACTGGCAATCCGGGAGCGCTGACGAGCATT
ATGTCGTCTGCTTCATACCACGTGGGTTGCCCGCACGTTGATTGCCACTTCAAAGCGCGA
CGACTAATTGGTATGTGTGGCGTTAAGACCATCAGTCAGTTGCCTAGGCGCGCAGCAAAC
AGTACCATTTAATAAAGGGGACAGGTCTGCTGGAATTGCAGGCTAAATGGATAAGAGAGC
GCTTATGGAGGAGGCGTGTATGACGGTAGTCATTAACTTAATCATCTTCCTGTCCCCGTT
AGCGACAAGCGGAGCCTTAACTTACTTGTACTCTTGAGGTGGGGGTACACCCCCGAAGTT
GATAGTCATCTAATGCTCATCAGTTATCGTCCTTCTGCCGGGGACCAGTTTCGACAATGC
GTGGCAGTTATTATCACCATAGACCACTTTACGATTATGGCCAAAGGAACTCAATTGCTG
AAATATCCTTCTTTCAAGAGGGATGGCTCGATTGCGCCAGTCCCTAGTACATGTCGCGTG
ACCCAGGGCTCCACTCGATGGCCTCGAAGCTTGTCGTGGAATGCACGACGTCATTAAACT
CAAAGTCCAGCTATGGCAATAGGCGAGTGCTGTGGGATGTCTGGTCGCTCTGCTGACATC
ACAATTACATAGTCTGTCCCGGCGGCCCGTGGTA
>Rosalind_0008
CCCTGTCCACGGGAACGGGTTGCTACGTTCTTCATTGCCGCGCTGAGCAGACTCATTGTT
ATCTAACGCACAACGCGATGCGTTGAGCAGCCTTGGCACGGAGGTCCGTTATCGTGGGGT
TGTTCGGCAGGTGAGGTAAATTCCTGCTTGGCGCAGCGATCGGCCTCATTTGTGTTGTGT
AGGGCCTCAGCTCGGGTCGGTAGTAATGACATTAAAACTGTAGTGACTGGCAATGCTAAG
TGTACTGAGAAGGCCATGTAGGCTTGATCCCTTTCATAGTTAAAGGAGAATGGCTACATG
GAGCTTAGTACGACTGCCCCCCTGCTTGGAGTTTCTGTAACTGGTCAAGTCTGGTGCCCC
CGGGCCCCTCGGCGGTTCCGGGGCCCAATGATCACATTGAGGGCGGATGTTCATTGCAGG
CCCCTGAGGTGGGGGGGTCGGACGTAGAGCATACTGTTCCAGGCCGTAGGTCGTATTATA
CTGTCCGTCATACGGCATAGAAGGCCGTTCGCAGCCACGTACATCGGTGTCCAACGGATC
TCGTCTGGCTACGGTGGATCTTCGTTGCTGCAGCCGAATCCTTGGTTAATCCTGCCGCAT
ATACTGACAATGATTACATGTAACAGAACACCCGAGGTGCCGCACCGGGGTTGTGCAGAG
CTGACGCTCCGAGCTAGGTACGCTCCTAGGCTAGGGCGTACCCGGGCAGATCATCTCCCC
AGTTAGTTGTTCGTCCCGCATATCGCGGGCACCCAGGGCTATTAAATACCTTCGATCACC
CCTTCAGTACGTGGTAATCTAAACCCATCGGCGATTGTAAATTCATTGTCGGGAGTAGGC
TTATGGACTATACGA
>Rosalind_2504
GCAATAGTCCCCATATCGGCGTCATGTGAATGTCTCTCTTCATGAATGATACCAGGTGGA
ATACTTTTGCAGTGCATGTGGGCCTACCATTTGGCAGACACGTGGTATCAACTACGGTCG
AGACTGGAACCGATAGACCGTACCCGCTTCCATTATAATGCGGTCCGTTACCCGAGCAAG
ACTCCCCAGCGAGCTATGCTAACATGCGTAACGCGAGGTACAAGCGTGGACCTTTGCTCA
GGAGTGGCCCGCAGCCGTGACCGGAGGGAAACTGCCGCGAGGTAGGTTTATCTATGAATA
AAGACCCCCGACCCTACTCACTGAAGGGCGAACCCTGAATGAGAGAGGCTGGTCATTTGG
TGCCGTTGCGCGTCTACGGCGGTTTAAAGCCTGGCCATAGTGTGCACGACTAGAGAGCTG
TCGTCACAAGGCAGTAGGGGAACTCCTCGCCTAGGACTCCCGCACTCGTATGTACACTTA
CGGTCCCAACGTGAAGACGTATGATAGACGAAACGTATGTCGCCCCCACGGCGCGTCAAC
TTGGACCAAAATTCCGCACTGTAGATGCTTGACATATGTTCCGGTGCGCTTGACACTGTG
ATATAAGTTTTTAAATCTACACTAAGTGCGAATCCCAGTGGTCCCAACGACCAGTGTGCT
GTCATCATACTTTGCGTCGAGTGGTAACTCACTCCTCTCTGCATCCGCATCGGAAAATGA
GACCTCCACTGACACTGATGGATATTGTAACCAGCAGATTACTCTGGTCTTTTATTACGT
TACCTTAGTCTCGGCAGTCAATAGCTCTCTCTATGAGCAAGTACCGGCTGCAGGCTCATG
TCCCCACGAGGCCCGTTAGATATTGTTCTGGATTACCGTAAATTCCATTATTCTTCTCGG
ACGACTACATT'''
gc_result = '''Rosalind_0008
54.502924'''

#prot
prot_variable = """AUGCUUUCUCCCUUUAUUCCAGGCCAUUCCGGGCAGUCCACUGUCGAAAGCAUUUGGAAGUACCAAGAAGUUACUACGCUUUGCGCGAAGCCGGUAUCAUCCCAUAGAAGCCGGUUCAUCUGUUCUCGAGCUCUCUUCUGCUGUUCACAUCUUAACAGGUCCCGUAUAAGACCGGCCUGCCCCAUGCGCGCAACCACUUGGCGAACUACUCAAAUUCUAAUGGUUUCCAAUUGUCCGAUGCUAAAGAUCUAUGCACGCAUUUCAAACUCGGAUCUCGAUCUCCGGGGUAUCGUAGAUAAUCUAAGAGGGACAACGAGCUUAUUCUAUGCAGGCAUACAUUUAUGGGGCGACGUUGAUACGGUGCUCUUCGCCAUAGGCAGUACGGGCGCGUCCAGGGAACUAGCUCAGUUCGUCGUUCAAGCGCAUUUGUGGCUGGGGAUACAGCAGUUCGAUGAGCCGCUGCUCGUGUGGUCUGCGUCGGGGCACACAGCCUUGGCCCGGGACAAGGAUCGGUUGUGCGGGCCGAACCCCUCAUCCAGCAUUUUGUUAAUCACAAAGAACCAGCAUAUUCAGGUCAUUGACGACCCUGUUUCUCCAUCAACCUUAAAUUGCACGCCGUCAGAUACCUCGCCUCCCUGGUCACUGGACGCCGCGAACAUCAGUAAAUUACUAUCGUUGGUCUUAAUCCCUAACGAAUCUAGCCACCAGUCCACGCCUAGUCCAGUAGGCCCCGCUCACACUACGCUUCGGUCCAACGUCCGCAAAUAUGCAUACGCGAUGGUAGCCCUCCUGGCGACGCAGCGACAACGAGUUGGGGCCAUAUACCAAAAGUACCCGAUUGUCGAUCGGACGAAAAACCAUGCUCUGGAAUCGCUUGUACGACAUGGAGGCUCCCGUCCCAAGUGGAAAUCUCGUGGCGCCAGUCAAAUUCCCGCUGGUCUCACGGUGUUAUGGACCUAUAAUGGGAUUCGUAGUAGCGGCGGUCAGCUUAUACCUUUAAAGCGGCUGUCCAAUAAAGUGAGGCACCAGAACAAAUACGGUCCCGGUCCGAUUGGGCACGCUAACCUGAGACGAACAGGUCCCCAACCGGAAAGUCACCGGAGCGGGCUUGCACCUCAAUCGGUCACCAAUACAGAGACAACUUGCUGCCCCAGAAGCCCCCACGUGGCGACAGAACGAUUCGAUAUGAUAACGAUCCGCCGUGGUCUGUUGCAGGCCACUCUAGGUGUCGUAAUUCGGGCCACCUGUGCGCGCGAGUUAGAGUUACGCCCGUCAGAAGGUUAUCUCCGAGUGGCAGUUCACUUCCCGACGUGCCCACAGGCUUUCCUUCAGACUAGCGUUGGAUCAAGCGAUCAAGAAGAUAAACGCUGUAGGCCCCAUGGAUGCCAUAUCAAUUCCGCGGUCAGACUCGAACCCACUAUCGCCCCCCCCCACCUGUACCCGUGGGAAUUGUCAUACAUGGGGAGGGGGAGCUCCGAGUCGAUUGUAUGCGGGCCUACCCCAGUCUCGAAGAAGCGAUCUUUAUUUCACAAGGUGGACGUAAUGCUCGUGCCCACGUAUUCGGGUUGGGUGAUCCCACUGUUAGUACCUCUUGCCGACCCACAUCCUACGAAUUUAGUCCCAGUGCUGGGGGUCAGUAGUCUCGCGGCGAAUGGAACGGUUCCUUGCGGCGAACCCAGGACUUACGUAGUUCAAAUGAGUAAUAAGACCUCAAACGGUUCCCAGUGGCCUGCCUUACCCAUAAAGCGCUCCCACCCCUGUCCGGCGGUUAGUCAUGUUAAUGGCUCGAUUUACCGAUUGGCGAGCCCACCCGUGCAAGCGUGCAAAGCCAAUUGCACGAGUAUAGAUGCAGGCGGGAUGGUAGCGGGAAUCUUAUGUACCACCGAACGGAGGUUGGUCACAUGCAUCCCUCCUCCUGCUAACGAUCAUUCGGCGUGUAAGUCGCUUGGGUUUACAGCAUUGGUGGUAGUUGAGAGGCAAUGGAGUCCUUGUGUAUCUGCCCGCCCUCAAAUCGACGUAGGGGGGGAAGAUGAUGAGUCGGCAGCGAGUCCCCGAGAGCACCAUACAACGCUCCCCUUCGAGCGAUGCGAGUCCGAAAGCAUGUGUGCCGUUUGCAGGGACGGUGUCCUCGGUGAGCCGUCUACGCUGUACGAACCCCAAUCAUGUCCCCGGAUUCAGACCAUGGCCGCUCCAAAUAGGGUAAUACCUCAAUUGAUGCAGGGUCCAAUAGCAAUCAUAGGCCGUGCUGCUCCAGUGGAUCCAUACGUAACGUCAUGUGGUUCGUCUGACCAUACGAGAUUGGAGCUAUUCCCGAAAGUCCAGGACGGAUGUUUCUACCCACUGCGUGAGUCCGUGGAUGCGCCAAUCAUCGGCCCCCAGGCACGGGUCUUGAUUUUCUUACAUAUCAUUGUCUUCGUUUUUGAGCGAGGGACCGUGUCGGAGAUUCGCUGCCUAUUGCAUGUGUUCAAUAGGCGUUUAAGUCGGCCGGGGCUCAGUCUAGGUAACUCUUUAUGCGCAAGACAUGAGGAGGCUCCUUCGACCACCUGCAACAGACGUUCGUGCGAGUUCUGCCGAUGCAAAGCGCGGCGUCGGAGUCACACCAGGCCCACGGACGAUGAGGAGGGAGGACCUAGGGGCACGCGUCCUGUGUCUGCGGGCACCCUCCUUUUUACAAUCCAUCCUACGCAAUUUCACUUACCGCAUCGUGCGCUUCCUCUUUGGGGGUCAAGCAAUCCAGUGAAAUUGUGUGCGAUUCUAAGUCAUGACCCCCAUUUCUAUACCAUACCGUUGACGCGUCCCAUUGACGGUGCCAUUGUUAGAAGGUCACACAGGGCCCACGUAAAUGCUGCGUGCAAGAGACCAGGGUCAUGCGUAAUAGGCGCCCAUUACUUUUGCUCAAAGCAGUCCUGCGGCCCGUGCCGAGGACUCAUAUUCCAUCGAGGGAAUUGGCGCGUAGGUAGCUCGGCCAGGCACAUAACUCGGGAGUCACGGUUGCCUGACGAUUGUCGGAUAAAAAAGAUUCGGGAGUCAUUUCUUUGGCGAACGCACUUCAACUCUCGCCACGUGGGGAGUUGGGGGGAAAGGAGCACGGAUAGCCUCUGCGGGCAUACUACCCGGGAGCGUAAGUGCUAUAACUUAGUGACAAUGCUACCCACCGCUAUCACGGGGUGCAACGUCUGUUUGCAGGACUCGGCUACACAUUGCAUGGAAGGAAAGGCCUGUAAGUGGAUGGAAGUGUGCGGAUCUCCAGCAGUAGAUCCGCCGGGAGGUGUCAGAUUCCUAAUGACUUCGCCAAUUGUGCUAGGCAGUUUCUGGCGUAUUGGGCCGGCUCUUCCCAGUCGAUUAUCGUGGUCAGUACCCCGAGACCUGUAUAUGAGCAGGUCCGUCUACUUUAUAUAUGAGACUUGUUCUAUAAUGGUUGGCGUUGGCGGAUACCAGAUUAGCUACUGGCUAAUUAUAGUCUGGAAGUCGCUGCUAGCAACUUCCGCAGAUGUUAUAUUAAUGUUGAUAGACGGUACCGAGGUUGUAUACACGAUUGAAGUUCUACUGACUACCCAAAUCGUCCCCACGAUACAGCGGAUUGGUUGGAGACCUCAAGGGUUGAAGUGCAGACUAUUGCGCCAUGAAUACAGGGUAGAUUGCGGCAAUGUCAAAACCCAGGUGGGCCGGGAUGGACAGAAUCGUGGACAGGCUCGAGGGAGCGAUUCUCUUACAUUUCGACCCCCACCGCCCCUUCCGGGCAGGCGUACAAUCGCGGCCCCAUGUGCAUCACGUGUAGCAGAGUUUACGGGGACCGCUACGUGCGCGCCUGAUACGUAUAUAGGUAUCACUGAAGUCCUAAACCGAAUACACCGAGUAGUUGCCUAUCCCAACGUACGCAUCGGACAUCAGGCAGCUAUCACGUCAAACGGAAGAGGAACUAAAUGGGCGACAACCCCGACAUACCGGUGUAUGUGCGUUGCCCCUGAACAUCGAAAACGGCAAUGCAUUACGACUCGUGCCCGCUUUCUGAAUCAGAGCACUAAGUUACUACUUUUGGUGACCGGAAAAGGUAUGUAUGCGCAGUUUCAGUGCGGGAAACACUCCUCCCAGCGUGAUUCCUGUUCGCUGUAUUAUUUCAUUAAAAAAACGUUACCAGUGGUAUGGAGGCCUUUAUGCGGGCACUGGCCGACCGGGGCGCGCUAUCUGACCAAUCUGCGGCUUUUCUACUCCCGGACGACCCGAUCACUCUACCUUCUCUCCGAACUAAUAGCAGCAUGCGGGCUGGCGGACUCGUCUGUCGCUUGGCGAAAAGCCCAGCAUGACUCCUACAAUGAACCUCAUUUUACCCCCAAAAUAAAUGUAUCAUGCGGAUUGAUUGCAGGGUGGUUUACCCGCGAUUUCCACAUGUCGCGUACAGUGGAAAGAGCGAGUGGCCGCUGUGUAUACGAGACGUUUCGAAUUCAACACAAAUACGCGUGUCCGUCUUGCCGGGGAACAAACUUAGGCACCUCGACUAGCGUACCAUCGCGGCCUGAGCGGGAUUCAUCCCGAUGCAGAUCUUCGCUCGCAAUGGACGCGCCUGUCGAUUGCGGUCCCUGGGCUACUGGCGCUGAAGCUGACGGUUGCCCUGUGAUUGUCGUUCAGUCAUCAUUGUUAGGCUGCGGAAGCGGAUGCACUCAGAUGAGAAACGUACAUUCUCGUAACGAACACCACGGCCCUGUGGUGAGCGUUAAAACCUGUAGGCCGCGCGGCAAGUGGGCAGAAGGACUUAUCACGCGCCGGCUGUAUGGGUUUUGGUGGCCAGUAGUGGGAUCAACCUGGAGCAUGGUCGGGACUCCUACCAAGCGACCGGGGUUGGUGACUAAGCCAAAAACAGAUUCACUUCCGGUCGCAAGGCUCCCUUCCGAGCGUGGCUGGCGAUAUCGAGAGCGGAUUAUGCUUGCGAGAUAUCGUGCUCUUAAAUCUGAUUUUUCUAUCGACGGAGCGCUUCACACCGUUCACUUCGUCACUCAACGUUUAGGAGUACAGCCAGAUGUGAUUGGGCUAUUAGAGCCCCUGUACCGAAACCCGGUGCUUAGCCGGCUGGUGUGGGGCAGUACCAUGACCCUCUCUGUAUCGAUAUCCGUGAAUUACUUCGAUGGCUUAGGUGUGUUAUUCAAGUCAUGGGCACCGGCUCAAUCCGCUCUGUGGGGUCUUUCUGAAAAGUCUGUGCAGUCCUUAUAUCCUUAUCGCCAACCUAGUUUGCGUGAUAAUAACGGACGUAUCAUCGUGGAAAAACUAAAGACGUAUCUCGGUUCAACUGAAAGCGAUGGGGACGCUCUGUCGCUUCACGUACUCGAAGGCACCCGCGUAUACUCCGCCACAUGGGUGACUCCAUGCCACACGCUGCUGGCUCUCCAUGGGGUUAUUCGUUCGACCGCGGCUAGUAGAUAUUACGGGAAUCGAUUAGCGCUAUCAGUGGACUCCAGUUCCACAGAUGAAGAACAUCGGCCCUCUCUGUGCCCCCUGGCGGGGGACACUGAUGAUCCUAUCCCGAGUUUAGGAAAAGAUAUAGGUCUGUGCCUUCACAGUUAUGCUGAUCACAGUGGAUACACAGGUAACAACUCCAGUAAGGGGCAACUUUUCUACUACGAUGCAAUACAUGUGUCCCGUGACUUAGUACUAACCGGGACCCCGGCAUCCUUCCAGCUUUCACGAAGAGCCCCCUCCCCACUUAGGGUGGAUAUGCAACGGCAGAAGCACCUAGCGGCAGCGCUCCAACGCAUGAAUAAAAACAGCCUGCCCAUGAGUCCUCACACUCGACACUGGCAGCAAGCCACGCGCCUAUCACCAGCGAGCACGCUAAAUUACGUAGGGCUCCAGACGAAUAUCCCUUCACCAAGCCAAAAGCCAAAUACAUCGGAAUCUGCGGAACCGACUCCGUUAGUUGAUCAUCCUAUGAUGUAUCUACGACCUGCGUUCGUAAGAAUCCGUGGCCCAUGCACUGUAUCAUUGCGAUCCAGGCUGGGCCGCAAGUCCAGAGUCCACCAUGUGCUCUUGUUAUGUUGUCUCUGUGGACCAGUCAGUGCGUUUCCCCCCCUCAAGUCGGCUCAAGCAUGGACCUCUCAAGCGAUAGCACGACGCAGGGUGCUGACCGAUCCAAUCGUAACGAGGUCCAUAAGGAAUCUGUCGAACAGCUGCCUAACACUCGUGGCCCUAUAUGAAAAGACACCCCACUCCUGGAGUCGGCUUCGACGCCACAUUCGAGCCAGGCUUAACACAUGUGGCGUAAGCGAGCAUUUUCGCCCUCUCCAGUCUCGCAUCGCAAUGGUAUCUACGGCCUCGUGGUCGUCAGAUAUGAAACAAGGCCCAUGCAAGGCGGUUGUAUAUUCUAUGUCUUUCUUGCUAAUUAGUUCUGGGGGACCAGCUGAUUAUUGCUCUGGUGGCGGGGGGACGCCGGCAGUCUGUUGUAUAUUUGGGGCUAGAGGACGCGAUUCAGGCAUGGCAUCGCCCGAGCCAUUCUGGAUAAUUUCAGAAUGUAGUAGUUGCGAAUUUGGGUCGAUCGAUUCUAAGACAGUGAGGCUCCUCGCAAUUGUGUACUUAAAGGGGAUGCUGGUACCGUCUCUCCGUUCUGGAGUAUACACAAUUUUGAAUAUCAAAGAUCGCGCCCCUUCCAUGAGUUUAAUAACCAAAGCACUUAGUAUAUUCGACGUUACAAGAUCUCCGCAUUCUCAUCGAAGUGCCGCAUUAUCUAUGAGUGCCGUUACUACCCGCCUAGACCUGCGAGCCGUCGUGCACUUUUUCCGUGCCGGAAGUUCAUAUUCUGGUAGCUGCGAGACCCCGCCCUGCGGAGUCCCCAGCUACAGUAUCAAACCUAGCCGAAUAGUGGGCCCUUCGGAGUACGUCUUCUGCGUCAGUCUUGAUAACUAUUUAUCGAGUUCUUUCGGUUGCAGGGUAUUCUCUCAUUCACGCAGCCGUGAUGCAAAGGUUGAUGUGCUAUUGUAUCGGUCACGCGACUACAAUUCACCCGUAAAGUGCGGAGUUCUGCAGAAAAACUUCCACACGGGACAGGGCCUCAUAUUAAGGUUAGACAGACAGCAUAGACCAGCUUAUAUGUAUUCCGGCUUCGGAUGCGCUGGAUAUACUUGUUUGAACCAACAAGUCGUAAAUGAAACCUGGUGCAGAAUUGAGAGUGCUAGGGAUCGGUGUACGCAUUCCUCCGAUUACAGAAUCACAACUAUGCUGGCUAAGCCAAGAAAUAUUUACACGCAGACGGGUCUCCUGGCAUUGGCGUCGCAAGACGUGAAAGUGAUGCCUGGGACAGGCAGGGGGUGCGUGAACGAGUGUGCCUCACAGCGCCACUGUAUAUCUGGUGCGUACUCCGAAAAUAUCGUUAGGUAUGGAAUUGCCUCCGUCUAUGGUUGUUCGCCCCCUAUAUUGGAACUUGGGAAGACCUUCUCAGUGCGUAGAUUCGAAACGCGUGGAAUGUUCGACAAAGAUGUUUAUAGUGGGGGUUCAUACUUCCAGCCUCAUGAUAUCCUCCGCAUUCUGUGGACAGGCGGAUCGCAAGCUAGAGGCUUGCACGACAGGGAUGACCGCUUUUUUUUAGCGAGGUUUCCAGGGCGGCGAUCAUCGUUGAUUUAUCUCAAUCCGUUCGUACUUAGAACAUGGGAUAACAGGAGGGAACGGAUCUCGUUUUUUAGGCGAAUCUAUGGACAGGAUCGUAGCGUAUCCGGUCUGACGUUAGUAUCCGGGGGGCGGAAUGCGAUCCCCCAGGCCCCCUCUGAACUAAUCAAAAACCGGAACGAAGCAUAUGGCAGUUUCCAACUUAGUAUUGCAUUUCCCAAAGUUUUACGCUCAUGGCGUCGGGUAAUGGAUAGUGUACACAAGAGUUCCCGAGGGCAGCUCCCUACGUUCGUCAUAUGUAGUCAGGAGUUUUCGGCGCCAGCACCAGGAAGAGGGACCGGACAGGAGGUGGCCCCGCCAUGCGAGCCCACCGCUUUAGAAAAAAUAUUUCGAACCACCCCACACUUCCUGCUCCAACUCGCUUGGGUUAAUAGCUGGAAGUCCGAGUCGGAGAGGAGCUCGCACCUGAAUCACCCGUUGACCGGAUUCUUGUUGCCUCAAGACCGAGUAAAGGUUCACCGGAUUGUCCCACGUCUUGGGUCGGGAUUGGGAUCGCCCGCGGAUCUCGCCGCCAGUCCGUCGGGUGGCGGGGAGGCACUUAGGGUCCCCCUGACUAUCGAUCGCUCCAGAUCAUUCAUUGAUGCUGCCCUACCGCGGAAUGUUGGUCGUGAAUAUGGGGUUGCGCUUAACUUUCUAAUAAGACUCCUCCGGUGCAUGAUUACCCGAGGCACUGACACAGGAGAAGCCAACCAUCCAACCCCCGCUUGUCAGGAAUUCCUUAGUUGUGCCGAGAGCUUACAUAACGAAGGUCGUGUAACUGACGUAUCCCCCAAAUCGAGAACAGCAAAUGAAACAUCUCAUAAUACGCUGCAAGUAGGGCUCCAACUGAAGAUUCACCGGCUGAAUAGCAAAUAUUUCCGAAUCUUUUCAUAUACAUGGUCCCUACGUUCUUCCUUACUACUAGCACAUCAUAUCCCUGGGUACAUUUUCGCGGUUACUUGGGGAAGAACACGAUUAAGUGACACGCGCCGAUAUGAUUCUCGCGCUAUGUUUGAACUACUGAUUCCGCCUAGCCCACUCUGGUCGUUCACAUACGACGAUGUGAAGUCUGACCAAUCUUACUGUCGGCCCGGCUAUCUGAUUAAAUUUCUACUGCAGGCCGUAUCUUGUCAUGUUGGAUUACGUAGCAUGGAUCGUUCUCGGACUCGUAGGAUGGGGUCGCCGGAAGCCGAGAGUCAUCACAAACCGCUCCGUCCGUGGUGCUGCACAGUUGUAUCUCAAAAAGUUCGCUGGGAGACUGGGACUCUUGCUCUCCCCAGGGUUGAUGCUAACUUAAAAUCACCAGCAGUAUAUGACCGCAUGAGUCUGUUGGGAUUAAUCACUAGUGCGGUAUCGAUCCCCCAUCAGGCAAAUCAGAAGACCUGUCUGUUAGUGACAGCUUCACCCCUUGAAAUAUGGCGCCAGCGGUGA"""
prot_result = """MLSPFIPGHSGQSTVESIWKYQEVTTLCAKPVSSHRSRFICSRALFCCSHLNRSRIRPACPMRATTWRTTQILMVSNCPMLKIYARISNSDLDLRGIVDNLRGTTSLFYAGIHLWGDVDTVLFAIGSTGASRELAQFVVQAHLWLGIQQFDEPLLVWSASGHTALARDKDRLCGPNPSSSILLITKNQHIQVIDDPVSPSTLNCTPSDTSPPWSLDAANISKLLSLVLIPNESSHQSTPSPVGPAHTTLRSNVRKYAYAMVALLATQRQRVGAIYQKYPIVDRTKNHALESLVRHGGSRPKWKSRGASQIPAGLTVLWTYNGIRSSGGQLIPLKRLSNKVRHQNKYGPGPIGHANLRRTGPQPESHRSGLAPQSVTNTETTCCPRSPHVATERFDMITIRRGLLQATLGVVIRATCARELELRPSEGYLRVAVHFPTCPQAFLQTSVGSSDQEDKRCRPHGCHINSAVRLEPTIAPPHLYPWELSYMGRGSSESIVCGPTPVSKKRSLFHKVDVMLVPTYSGWVIPLLVPLADPHPTNLVPVLGVSSLAANGTVPCGEPRTYVVQMSNKTSNGSQWPALPIKRSHPCPAVSHVNGSIYRLASPPVQACKANCTSIDAGGMVAGILCTTERRLVTCIPPPANDHSACKSLGFTALVVVERQWSPCVSARPQIDVGGEDDESAASPREHHTTLPFERCESESMCAVCRDGVLGEPSTLYEPQSCPRIQTMAAPNRVIPQLMQGPIAIIGRAAPVDPYVTSCGSSDHTRLELFPKVQDGCFYPLRESVDAPIIGPQARVLIFLHIIVFVFERGTVSEIRCLLHVFNRRLSRPGLSLGNSLCARHEEAPSTTCNRRSCEFCRCKARRRSHTRPTDDEEGGPRGTRPVSAGTLLFTIHPTQFHLPHRALPLWGSSNPVKLCAILSHDPHFYTIPLTRPIDGAIVRRSHRAHVNAACKRPGSCVIGAHYFCSKQSCGPCRGLIFHRGNWRVGSSARHITRESRLPDDCRIKKIRESFLWRTHFNSRHVGSWGERSTDSLCGHTTRERKCYNLVTMLPTAITGCNVCLQDSATHCMEGKACKWMEVCGSPAVDPPGGVRFLMTSPIVLGSFWRIGPALPSRLSWSVPRDLYMSRSVYFIYETCSIMVGVGGYQISYWLIIVWKSLLATSADVILMLIDGTEVVYTIEVLLTTQIVPTIQRIGWRPQGLKCRLLRHEYRVDCGNVKTQVGRDGQNRGQARGSDSLTFRPPPPLPGRRTIAAPCASRVAEFTGTATCAPDTYIGITEVLNRIHRVVAYPNVRIGHQAAITSNGRGTKWATTPTYRCMCVAPEHRKRQCITTRARFLNQSTKLLLLVTGKGMYAQFQCGKHSSQRDSCSLYYFIKKTLPVVWRPLCGHWPTGARYLTNLRLFYSRTTRSLYLLSELIAACGLADSSVAWRKAQHDSYNEPHFTPKINVSCGLIAGWFTRDFHMSRTVERASGRCVYETFRIQHKYACPSCRGTNLGTSTSVPSRPERDSSRCRSSLAMDAPVDCGPWATGAEADGCPVIVVQSSLLGCGSGCTQMRNVHSRNEHHGPVVSVKTCRPRGKWAEGLITRRLYGFWWPVVGSTWSMVGTPTKRPGLVTKPKTDSLPVARLPSERGWRYRERIMLARYRALKSDFSIDGALHTVHFVTQRLGVQPDVIGLLEPLYRNPVLSRLVWGSTMTLSVSISVNYFDGLGVLFKSWAPAQSALWGLSEKSVQSLYPYRQPSLRDNNGRIIVEKLKTYLGSTESDGDALSLHVLEGTRVYSATWVTPCHTLLALHGVIRSTAASRYYGNRLALSVDSSSTDEEHRPSLCPLAGDTDDPIPSLGKDIGLCLHSYADHSGYTGNNSSKGQLFYYDAIHVSRDLVLTGTPASFQLSRRAPSPLRVDMQRQKHLAAALQRMNKNSLPMSPHTRHWQQATRLSPASTLNYVGLQTNIPSPSQKPNTSESAEPTPLVDHPMMYLRPAFVRIRGPCTVSLRSRLGRKSRVHHVLLLCCLCGPVSAFPPLKSAQAWTSQAIARRRVLTDPIVTRSIRNLSNSCLTLVALYEKTPHSWSRLRRHIRARLNTCGVSEHFRPLQSRIAMVSTASWSSDMKQGPCKAVVYSMSFLLISSGGPADYCSGGGGTPAVCCIFGARGRDSGMASPEPFWIISECSSCEFGSIDSKTVRLLAIVYLKGMLVPSLRSGVYTILNIKDRAPSMSLITKALSIFDVTRSPHSHRSAALSMSAVTTRLDLRAVVHFFRAGSSYSGSCETPPCGVPSYSIKPSRIVGPSEYVFCVSLDNYLSSSFGCRVFSHSRSRDAKVDVLLYRSRDYNSPVKCGVLQKNFHTGQGLILRLDRQHRPAYMYSGFGCAGYTCLNQQVVNETWCRIESARDRCTHSSDYRITTMLAKPRNIYTQTGLLALASQDVKVMPGTGRGCVNECASQRHCISGAYSENIVRYGIASVYGCSPPILELGKTFSVRRFETRGMFDKDVYSGGSYFQPHDILRILWTGGSQARGLHDRDDRFFLARFPGRRSSLIYLNPFVLRTWDNRRERISFFRRIYGQDRSVSGLTLVSGGRNAIPQAPSELIKNRNEAYGSFQLSIAFPKVLRSWRRVMDSVHKSSRGQLPTFVICSQEFSAPAPGRGTGQEVAPPCEPTALEKIFRTTPHFLLQLAWVNSWKSESERSSHLNHPLTGFLLPQDRVKVHRIVPRLGSGLGSPADLAASPSGGGEALRVPLTIDRSRSFIDAALPRNVGREYGVALNFLIRLLRCMITRGTDTGEANHPTPACQEFLSCAESLHNEGRVTDVSPKSRTANETSHNTLQVGLQLKIHRLNSKYFRIFSYTWSLRSSLLLAHHIPGYIFAVTWGRTRLSDTRRYDSRAMFELLIPPSPLWSFTYDDVKSDQSYCRPGYLIKFLLQAVSCHVGLRSMDRSRTRRMGSPEAESHHKPLRPWCCTVVSQKVRWETGTLALPRVDANLKSPAVYDRMSLLGLITSAVSIPHQANQKTCLLVTASPLEIWRQR"""

#prtm
prtm_variable = """RNPCQYDWQSNNPVKQPQGIRRCSGHAVRFHWPETHLMRYLLFSWQGLVLFIMHKTSQLFEHIEQQDFAVYWYVMNIYQCVVRAEAQDVPLFKARSHMGGREFMWTVCHQQRCDRMDVRADVDQSFEFICGWKAVRKTPEQELCRLHQTAQLADNHSCEENAGIHLVYHMRCQKNRITCVAWKSSCFNTWPGTYMQNCVMVYGTLHQQQCKESMGKHQIMFGKEMHGRRFPPQNRGMVAKQWVKTWDNLPGMPFYHTLGHHEFGGYWKNTWVYQEHQTFGYFKEWEPWNVNCTATMAAHCNPYEGITRFTHWKYPVRHWQDHAVMTGKMSASSASDSTRSCCYTNTQMKCPFEHKPSETMIRTFCPYPEQKSLMTMEHLRFNTIFPNGQTEMKGDSTEYCEPIMRWVSYKVQYEVGMKRNERSCSKYYDGNASMYPKQCWTKVDSDYHWQVIFHANYQDAHSIYYDKLFELWKSNMHMENGLSFQAINFSADVMIFIHQTTRNIDDCNAPYTREFPVPYNEIWHIEEGHWDQENWWMWSSSVTDKPYFHFPSERIFISPMQVNSPQAPNCQVDGDRVTYMWVLFSWHSCVTKNCRSAVPYRPDGHNRVQGARRITQEPTVGMHLMLMGVDKLCQVTLFIQHEYAKVRYMPWAPNNHCKNFLSFLKQLSRNSHMHEVLEWSPIVDAPWSYRPFWCKEEIGEYYNACMCFVKVAALFCRYNDFVVWDLSKFWKWRYAHMINDGLWAHIVIKKFSWWVPAFVKYSTQPGGLVAWCSRRIAQGPDNERGVILQDTAHCMREINPIYMDDYEDPIGWCHWWCKVHNMCFPCGASEGRGADVHYIQNFWYGSYNRVEHGFNLSYRCVLWAIYFWHWRIDFGEWRFIYNIDDIKFETCMAKYVSASYKVGYIQTEECASSMMSEGMRHNCVMYLGCNVCNVAIIHMFPERKFLRMQLQYNNRSYCINYEHSQRQGPAGANPQF"""
prtm_result = 116251.472

#fib
fib_variables = [8, 3]
fib_result = 217

#fibd
fibd_variables = [86, 16]
fibd_result = 414110157126129233
