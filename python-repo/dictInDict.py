allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def tolBroght(guests,item):
    count=0
    for k,v in guests.items():
        count=count+v.get(item,0)
    
    return count

print("the total fruit count is")
print("no.of apples brought by all",tolBroght(allGuests,'apples'))
print("no.of apple pies brought by all",tolBroght(allGuests['Bob'],"apple pies"))
print("no.of apple pies brought by all",tolBroght(allGuests['Carol'],"apple pies"))

