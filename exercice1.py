import random

def gen_list_random_int(int_nbr=10,int_binf=0,int_bsup=10):
    
        l=[]
        for i in range(int_nbr):
            l.append(random.randint(int_binf,int_bsup-1))
        return l


print(gen_list_random_int())