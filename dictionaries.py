
#author : G.akhil venkat
#created : oct 2022

#                                                          DICTIONARIES in python

#initializing dictionary in general
dicti={1:'apple',2:'bat',3:'cat'}
print(dicti)
#initializing dictionary with multiple dictionary/types && accessing
dic={1:99.6,'name':'anits',6.7:['list','inside list'],'path':{'dictionary':'inside dictionary'},66.5:('tuple','inside tuple')}
print(dic[1])
print(dic['name'])
print(dic['name'][3]) # accessing 4th element in anits (string is also a sequence)
print(dic[6.7])
print(dic[1])
print(dic[66.5])
print(dic[66.5][1])
print(dic['path'])
print(dic['path']['dictionary'])
"""
output:
{1: 'apple', 2: 'bat', 3: 'cat'}
99.6
anits
t
['list', 'inside list']
99.6
('tuple', 'inside tuple')
inside tuple
{'dictionary': 'inside dictionary'}
inside dictionary
"""

#errors

""" dic={[1,2,3]:'anits'}
print(dic)
dic={{1,2,3}:'anits'}
print(dic)
#its an error unhashable list because key value cant be sequence(except string) """

#duplicate keys
dup={1:'anits',1:'college'}
print(dup[1])
  #college ->accessed last duplicated key

#creating dictionary using dic method
d={1:'apple',2:'bat',3:'cat'}
print(dict(d))
d1=[(1,'anits'),(2,'college')]
print(dict(d1))
"""
output:

{1: 'apple', 2: 'bat', 3: 'cat'}
{1: 'anits', 2: 'college'}

"""
                          #modification of elements

d3={1:'apple',2:'bat',3:'cat'}
d3[1]='amaze'
print(d3)
#{1: 'amaze', 2: 'bat', 3: 'cat'}
d3[4]='new element' #adding elements post initializing
print(d3)
#{1: 'amaze', 2: 'bat', 3: 'cat', 4: 'new element'}

d3={1:'apple',2:'bat',3:'cat'}
d4={4:'anits',5:'college'}
#print(d3+d4)
# unsupported operand type(s) for +: 'dict' and 'dict'
#print(d3*d4)
#unsupported operand type(s) for *: 'dict' and 'dict'


                       #methods & functions on dictionary


#SORTING

dic={1:99.6,'name':'anits',6.7:['list','inside list'],'path':{'dictionary':'inside dictionary'},66.5:('tuple','inside tuple')}
#print(sorted(dic.items()))
#not supported between instances of 'str' and 'int'

dic={5:'anits',5:'vizag',4:'college'}
print(sorted(dic.items()))
# [(4, 'college'), (5, 'vizag')] ->if duplicated it will only last element into consideration
dic={1:'zebra',2:'yok',3:'apple'}
print(sorted(dic.items()))
#[(1, 'zebra'), (2, 'yok'), (3, 'apple')]
dic={3:'zebra',2:'yok',1:'apple'}
print(sorted(dic.items()))
#[(1, 'apple'), (2, 'yok'), (3, 'zebra')]

dic={3:'anits',2:'college',1:'vizag'}
print(sorted(dic.keys()))
#[1, 2, 3]
dic={4:'anits',4:'college'}
print(sorted(dic.keys()))
#[4]  ->if duplicated it will only last element into consideration

#MIN & MAX

dic={3:'zebra',2:'yok',1:'apple'}
print(max(dic))
#3
print(min(dic))
#1

#clear
dic={3:'zebra',2:'yok',1:'apple'}
dic.clear();
print(dic)
#{}

#copy
d1=[(1,'anits'),(2,'college')]
d2=d1.copy()
print(d2)
#[(1, 'anits'), (2, 'college')]

#get
d3={1:'apple',2:'bat',3:'cat'}
print(d3.get(1))
#apple


#pop  
d3={1:'apple',2:'bat',3:'cat'}
print(d3.pop(3))
print(d3)
#cat
#{1: 'apple', 2: 'bat'}

#popitem
d3={1:'apple',2:'bat',3:'cat'}
d3.popitem()
print(d3)
d3.popitem()
print(d3)
d3.popitem()
print(d3)
"""
{1: 'apple', 2: 'bat'}
{1: 'apple'}
{}

"""
 
#update
d3={1:'apple',2:'bat',3:'cat'}
d4={4:'anits',5:'college'}
d5={**d3,**d4}
print(d5)
#{1: 'apple', 2: 'bat', 3: 'cat', 4: 'anits', 5: 'college'}
d3.update(d4)
print(d3)
#{1: 'apple', 2: 'bat', 3: 'cat', 4: 'anits', 5: 'college'}

#values
d3={1:'apple',2:'bat',3:'cat'}
print(d3.values())
#dict_values(['apple', 'bat', 'cat'])
