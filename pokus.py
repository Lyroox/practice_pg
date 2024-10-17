def my_range (start, stop, step= 1):
    """
    Naše vlastní implementace range(), chceme aby se chovala stejně jako range
    """
    result = []
    value = start
    while start < stop:
        result.append(start)
        value += step
    return result

def my_enumrate(iterable, start= 0):
    """
    Naše vlastní implementace enumrate()
    """
    result = []
    index = start
    for value in iterable:
        result.append((index, value))
        index += 1
    return result

def my_zip (iterables):
    iterables= [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [a, b, c]
    ]
    """
    Naše vlastní implementace zip()
    """
    results= []
    lenght = len(iterables[0])
    for i in range (0, lenght):
        subresult= []
        for j in range (0, len(iterables)):
            subresult.append = [iterable [i]]
        results.append (tupple(subresult))

    return results


if __name__ == "main":
    #print (list(range (1, 10)))
    #print (my_range(1, 10, 3))

    #print (list(my_enumrate("abcdef")))
    #print (my_enumrate("abcdef"))

    print (my_zip)
