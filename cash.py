# -*- coding: utf-8 -*-

cash = 200
coins = [200,100,50,20,10, 5, 2, 1]

import time

def countChange(cash, coins):
    now = time.time()
    combos = []
    init_combo_list = [[i] for i in coins]
    ### Check one coin combo ###
    for i in init_combo_list:
        if i[0] == cash: combos.append(i)
    def inner(combo_list):
        incompletes = []
        for i in coins:
            for k in combo_list:
                #print(k)
                res = k+[i]
                res = sorted(res,reverse=True)
                if res in incompletes or res in combos:
                    continue
                else:
                    if sum(res)==cash:
                        combos.append(res)
                    elif sum(res)>cash:
                        continue
                    else:
                        incompletes.append(res)
        #return sorted(incompletes, reverse = True, key = sum)
        if incompletes:
            print("Time elapsed: %.2f" % float(time.time() - now), end = '  ')
            print("Max length: ", len(combos[-1]))
            inner(sorted(incompletes, reverse = True, key = sum))
        else: return
    inner(init_combo_list)

    return combos
    
    
combos = countChange(cash,coins)

#DP ALTERNATIVE 
#s = [1] + [0]*200
#for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
#    for i in range(len(s) - coin):
#        s[i+coin] += s[i]
#print(s[-1])
