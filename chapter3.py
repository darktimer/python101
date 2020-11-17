bicycle = ['trek','cannondale','redline','specialized']
message = "My first bicycle was a " + bicycle[0].title()
print(message)

#3-1 to 3-3
names = ['harry','ron','hermione']
print(names[0])
print(names[1])
print(names[2])

message = "Hello! " + names[0].title() + ", nice to see u."
print(message)
message = "Hello! " + names[1].title() + ", nice to see u."
print(message)
message = "Hello! " + names[2].title() + ", nice to see u."
print(message)

tracks = ["moto",'bike','car']
message = 'I would like to own a ' + tracks[0].title() + ' to work.'
print(message)
message = 'I would like to own a ' + tracks[1].title() + ' to work.'
print(message)
message = 'I would like to own a ' + tracks[2].title() + ' to work.'
print(message)
#end

names = ['harry','ron']
names.append('hermione')
print(names)

names = ['harry','ron']
names.insert(0,'hermione')
print(names)

names = ['hermione', 'harry', 'ron']
del names[0]
print(names)

names = ['harry', 'ron','hermione']
popped_names = names.pop()
print(names)
print(popped_names)

names = ['harry', 'ron','hermione']
first_owned = names.pop(1)
print(names)
print(first_owned.title())

names = ['ron','harry','hermione']
names.remove('harry')
print(names)

names = ['ron','harry','hermione']
temp = 'harry'
names.remove(temp)
print(names)
print(temp.title())

#3-4 to 3-7
names = ['ron','harry','hermione','jean','navl','sirius','fred']
message = "Would u like to dinner with me? " + names[-2].title()
print(message)
message = "Would u like to dinner with me? " + names[1].title()
print(message)
message = "Would u like to dinner with me? " + names[2].title()
print(message)
message = "Would u like to dinner with me? " + names[0].title()
print(message)

print(names[3].title() + " can't come join us, so sad.")
names[3] = 'lord voldemort'
print("So we invite " + names[3].title() + " to join us, welcome!")

message = 'Would u like to dinner with me? ' + names[0].title()
print(message)
message = 'Would u like to dinner with me? ' + names[1].title()
print(message)
message = 'Would u like to dinner with me? ' + names[2].title()
print(message)
message = 'Would u like to dinner with me? ' + names[3].title()
print(message)
message = 'Would u like to dinner with me? ' + names[4].title()
print(message)
message = 'Would u like to dinner with me? ' + names[5].title()
print(message)
message = 'Would u like to dinner with me? ' + names[6].title()
print(message)

print('Oh sweet God! Guess what? I found a bigger table! Come here!')
names.insert(0,'dumbledore')
names.insert(3,'mcGonagall')
names.append('lupin')
message = 'Would u like to dinner with me? ' + names[0].title()
print(message)
message = 'Would u like to dinner with me? ' + names[3].title()
print(message)
message = 'Would u like to dinner with me? ' + names[-1].title()
print(message)

print("Sorry we can only serve two guests! Rest of u'll can go home.")
print(names)
names.pop()
names.pop()
names.pop()
names.pop()
names.pop()
names.pop()
names.pop()
names.pop()
print(names)
print("Sorry guys!")
print(names[0].title() + ", u r still on table.")
print(names[1].title() + ", u r still on table too.")

del names[1]
del names[0]
print(names)
#end

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('This is original list:')
print(cars)
print('This is sorted list:')
# print(sorted(cars, reverse = True))
print(sorted(cars))
print('This is original list again:')
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#3-8 to 3-10
places = ['Peking', 'Hangchow', 'LA', 'DC', 'NY']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

names = ['ron', 'harry', 'hermione', 'jean', 'navl', 'sirius', 'fred']
print("I invited " + str(len(names)) + " guests to dinner!")
