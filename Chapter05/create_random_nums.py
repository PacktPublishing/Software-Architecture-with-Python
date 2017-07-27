import random

my_range = range(1, 100000)

def random_nums(num):
    for i in range(num):
        nums = random.sample(my_range, 100)
        open('numbers_%d.txt' % i,'w').writelines(map(lambda x: str(x)+'\n',
                                                      nums))
random_nums(1000000)
