from Flask_SQL import db,Puppy

#creates all the tables model --> database table
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

#none
#none
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

#or we can add objects seperately by
#db.session.add(sam)
#db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
