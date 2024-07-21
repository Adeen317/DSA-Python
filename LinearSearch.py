#Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number b turning over as few cards as possible. Write a function to help Bob locate the card.

#Linear Search
#Brute Force
def locate(cards, query):
    if len(cards)==0:
        return 0
    else:
        for i in range(len(cards)):
            if cards[i] == query:
                return i
            i+=1
            if i==len(cards):
                return -1

cards=[13, 11, 10, 7, 4, 3, 1, 0]
query=7
#output=3

tests=[]

#=======================================================================================================================================

#Test-Cases

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
        },
    'output':3
    })

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
        },
    'output':0
    })

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
        },
    'output':3
    })

tests.append({
    'input': {
        'cards': [13],
        'query': 13
        },
    'output':0
    })

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 5
        },
    'output':-1
    })

tests.append({
    'input': {
        'cards': [],
        'query': 7
        },
    'output':-1
    })

tests.append({
    'input': {
        'cards': [13, 13, 11, 10, 10, 7, 4, 3, 1, 0],
        'query': 7
        },
    'output':5
    })

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 7, 7, 4, 3, 1, 0],
        'query': 7
        },
    'output':3
    })

print(tests)
#======================================================================================================================================================================================================================







#a=locate(**test['input']) == test['output']
#print(a)
result = locate(cards, query)
#result = locate(tests['input']['cards'], tests['input']['query'])
print(result)
