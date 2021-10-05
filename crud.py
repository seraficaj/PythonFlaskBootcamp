from app import db, Puppy

## Create
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

##  Read
all_puppies = Puppy.query.all()
print(all_puppies)

# SELECT BY ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filter 
puppy_frank = Puppy.query.filter_by(name='Frank')
print(puppy_frank.all())

## Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
print(first_puppy)

## Delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

#
all_puppies = Puppy.query.all()
print(all_puppies)

