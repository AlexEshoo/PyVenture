import players
import rooms
import map_file
import inspect

player1 = players.player()

#commands = {'move':players.move()} # Not used. Looking for good implementation of commands

user_in = None
room_dict = {}
coord_dict = {}

for name, obj in inspect.getmembers(map_file):
	if isinstance(obj,rooms.room):
		room_dict[obj.title] = obj
		coord_dict[str(obj.coords)] = obj #lists do not work as keywords so convert to str

print room_dict


### Main loop ###

while user_in != 'quit':
 	current_room = coord_dict[str(player1.location)] #Call the key coords as a string
 	current_room.set_stage() #should probably only be done if the room changes to avoid too much text

 	user_in = raw_input('Enter a command: ')

 	if user_in == 'move':
 		old_location = player1.location
		direction = raw_input('Which way? ')
 		player1.move(direction)
 		try:
 			coord_dict[str(player1.location)]
 		except:
 			player1.warp(old_location)
 			print '\nYou cant go that way!\n'







