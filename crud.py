from Flask_SQL import db,Puppy

##create

my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

## Read
all_puppies = Puppy.query.all() # List of puppies objects in the tables
print(all_puppies)

#Select by # ID:
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#Filters, produce sql code
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
#["Frankie is 3 years old"]

############### Update

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


############## Delete

second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
