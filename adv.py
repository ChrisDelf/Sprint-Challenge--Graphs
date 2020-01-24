from room import Room
from player import Player
from world import World
from util import Stack, Queue  # These may come in handy
import random
from ast import literal_eval
from random import shuffle

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
print(room_graph[0])

### helper
def get_directions(room_id):

    valid_directions={}
    if 'n' in room_graph[room_id][1].keys():
        valid_directions['n'] = '?'

    if 's' in room_graph[room_id][1].keys():
        valid_directions['s'] = '?'

    if 'e' in room_graph[room_id][1].keys():
        valid_directions['e'] = '?'

    if 'w' in room_graph[room_id][1].keys():
        valid_directions['w'] = '?'

    # shuffle(valid_directions)
    print(valid_directions)
    return valid_directions


### DFT
# def dft_adv(starting_room):
#     #Create an empty stack and push starting vertex Id
#     stack = Stack()
#     stack.push([starting_room])
#     # Create a Set to store visited vertices
#     visited = {}
#     # while stack.size() < len(room_graph):
#     #     path = stack.pop()
#     #     room_id = path[-1]
#     #     if room_id not in visited:
#     #
#     #         visited[room_id] = {}
#     #         print(visited)
#     #         for get_directions(room_id):
#     #             visited[room_id].add(direction)
#     #             # visited[room_id][] = '?'
#     #             print(visited[room_id])
#     #         print(visited[room_id][1].keys())

def dft_adv(starting_room):
    #Create an empty stack and push starting vertex Id
    stack = Stack()

    room_id = (starting_room)
    print("roomid", room_id)
    # Create a Set to store visited vertices
    visited = {}
    room_options = len(room_graph[0][1].keys())
    move = []
    track_rooms = []
    while room_options > 1:



        random_exit = random.randrange(0,4)
        print(random_exit)
        directions_list = [ 'n','s','e','w']
        player_room_directions = get_directions(room_id)
        movement = directions_list[random_exit]
        player.travel(directions_list[random_exit])
        move.append(movement)
        #getting new room id
        # path_copy = path.copy
        # path_copy.append(room_id)
        # track_rooms = path_copy
        room_id = player.current_room.id
        print("player", movement)
        print("player_room_directions", player_room_directions)
        print("player_room_id", room_id)
        print("movement array", move)
        room_options = len(player_room_directions)
        # room_id = path[-1]
        # if room_id not in visited:
        #
        #     visited[room_id] = {}
        #     print(visited)
        #     for direction in get_directions(room_id):
        #         visited[room_id].add(direction)
        #         # visited[room_id][] = '?'
        #         print(visited[room_id])
        #
    return move
move = dft_adv(player.current_room.id)

traversal_path = move
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
