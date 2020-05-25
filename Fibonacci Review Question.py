# Fibonacci review question with examples of why you want to use a generator instead of a list(list takes up a lot more resources)


def fib(fib_range,fib_index_0,fib_index_1):
    for i in range(fib_range):
        yield fib_index_0
        temp = fib_index_0
        fib_index_0 = fib_index_1
        fib_index_1 = temp + fib_index_1
  
for x in fib(10000,0,1):
    print(x)



def fib_list(fib_range,fib_index_0,fib_index_1 ):
    fib_listed = []
    for i in range(fib_range):
        fib_listed.append(fib_index_0)
        temp = fib_index_0
        fib_index_0 = fib_index_1
        fib_index_1 = temp + fib_index_1
    return fib_listed

print(fib_list(10000,0,1))
