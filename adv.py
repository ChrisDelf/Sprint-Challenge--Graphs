from room import Room
from player import Player
from world import World
from util import Stack, Queue  # These may come in handy
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


### helper
def get_directions(room_id):

    valid_directions=[]
    if 'n' in room_id[1].keys():
        valid_directions.append('n')

    if 's' in room_id[1].keys():
        valid_directions.append('s')

    if 'e' in room_id[1].keys():
        valid_directions.append('e')

    if 'w' in room_id[1].keys():
        valid_directions.append('w')

    shuffle(valid_directions)

    return valid_directions


### DFT
def dft_adv(starting_room):
    #Create an empty stack and push starting vertex Id
    stack = Stack()
    stack.push([starting_room])
    # Create a Set to store visited vertices
    visited = {}
    while stack.size() < len(room_graph):
        path = stack.pop()
        room_id = path[-1]
        if room_id not in visited:

            visited[room_id] = set(path)
            print(visited)
            for direction in get_directions(room_id):
                visited[room_id].add(direction)
                print(visited)

dft_adv(player.current_room.id)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
