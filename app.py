# Create entries into the tables and print results

from models import db, Puppy, Owner, Toy

# Creating Puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add Puppies to DB
db.session.add_all([rufus, fido])
db.session.commit()

# Check by printing Puppy names
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

#Make an Owner
jose = Owner('Jose', rufus.id)

# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Frisbee', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Show updated on Rufus
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus.report_toys())

