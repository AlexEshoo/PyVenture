import rooms

home = rooms.room('Home',[0,0])
home.message = 'Welcome to the pyventure homesquare'

field = rooms.room('Field',[1,0])
field.message = 'You stand in a large empty field'

factory = rooms.room('Factory',[2,0])
factory.message = 'You arrive in a large factory with broken windows vista'