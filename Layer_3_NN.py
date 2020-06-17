X = [1.1, 1.2, 1.3, 1.4] #INPUT

W_1 = [2.1, 2.2, 2.3, 2.4] #WEIGHT1
W_2 = [3.1, 3.2, -3.3, 3.4] #WEIGHT2
W_3 = [4.1, -40.2, 04.3, 4.4] #WEIGHT3


B_1 = 1.6             #BIAS
B_2 = 2
B_3 = 3
#FORMULA = INPUT(n)*WEIGHT(n)+BIAS
Output = [ X[0]*W_1[0] + X[1]*W_1[1] + X[2]*W_1[2] + B_1,
           X[0]*W_2[0] + X[1]*W_2[1] + X[2]*W_3[2] + B_2,
           X[0]*W_3[0] + X[1]*W_3[1] + X[2]*W_3[2] + B_3 ]
print(Output)
