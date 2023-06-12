# Dictionary & Its Functions Explained
d1 = {}
print(type(d1))

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti'}
print(d1['rohan'])
print(d1['harry'])
print(d1['skillf'])

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
print(d1['subham'])

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
d1['anik'] = 'junk food'
d1[420] = 'kcbabs'
print(d1)

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
print(d1['subham'])
print(d1.copy())

# copy with delete
d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
print(d1['subham'])
d2 = d1
del d2['harry']
print(d2)

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
print(d1['subham'])
print(d1.get('harry'))

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B' : 'magic', 'L' : 'roti', 'D' : 'chiken'}}
d2.update({'leena' : 'toffee'})
print(d2)

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
print(d1.keys())

d1 = {'harry' : 'burger',
      'rohan' : 'fish',
      'skillf' : 'roti',
      'subham' : {'B':'magic',          'L':'roti','D':'chiken'}}
print(d1.items())