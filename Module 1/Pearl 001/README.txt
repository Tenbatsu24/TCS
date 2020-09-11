Names:
Puru Vaish		s2236141
Hyeon Kyeong Kim	s2112019

We have done the basic assignment, the bonus 1 and the bonus 2.

BasicAssignment: pearl.py
Bonus1: pearl_bonus1.py uses google_bonus1.py due to name change
Bonus2: pearl_bonus2.py uses google_bonus2.py due to name change

 In the zip file you will find a folder name pearltestingfile. This file has sample 3 txt files created by us which were read from the pearltesting.py to create a sample data set of pairs. Using the actual ones would create a print(pairs) which was too big for IDLE to process hence gave no info on errors. 

 In the pearltesting.py file we have created every variation of the assignment and implemented the code that we used in the actual result.

Concrete Test Cases:

Basic Assignment:

Search term: man
'man' occurs in ['brian.txt', 'chainltr.txt', 'grail.txt', 'menwomen.txt', 'pun.txt']

Search term: men
'men' occurs in ['catstory.txt', 'grail.txt', 'menwomen.txt', 'pun.txt']

Search term: woman
'woman' occurs in ['menwomen.txt', 'mothers.txt']

Search term: women
'women' occurs in ['brian.txt', 'grail.txt', 'menwomen.txt']

Bonus1:

Search term: man
'man' occurs in [['menwomen.txt', 22], ['brian.txt', 8], ['grail.txt', 6], ['pun.txt', 2], ['chainltr.txt', 1]]

Search term: woman
'woman' occurs in [['menwomen.txt', 15], ['mothers.txt', 2]]

Search term: men
'men' occurs in [['menwomen.txt', 5], ['grail.txt', 2], ['catstory.txt', 1], ['pun.txt', 1]]

Search term: women
'women' occurs in [['menwomen.txt', 4], ['brian.txt', 3], ['grail.txt', 1]]

Bonus2:

Search term: man
'man' occurs in [['menwomen.txt', 0.0117521], ['chainltr.txt', 0.0018018], ['pun.txt', 0.0011494], ['brian.txt', 0.0005785], ['grail.txt', 0.0004626]]

Search term: woman
'woman' occurs in [['menwomen.txt', 0.0080128], ['mothers.txt', 0.0054054]]

Search term: men
'men' occurs in [['menwomen.txt', 0.0026709], ['catstory.txt', 0.0025381], ['pun.txt', 0.0005747], ['grail.txt', 0.0001542]]

Search term: women
'women' occurs in [['menwomen.txt', 0.0021368], ['brian.txt', 0.000217], ['grail.txt', 7.71e-05]]