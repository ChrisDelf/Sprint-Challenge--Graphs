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
    # print(valid_directions)
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


    room_id = (starting_room)

    # Create a Set to store visited vertices
    visited = { 0 : get_directions(0)}
    opposites = { 'w': 'e', 's': 'n', 'n': 's', 'e': 'w'}
    room_options = len(room_graph[0][1].keys())
    move = []
    track_rooms = []
    while room_options > 1:



        random_exit = random.randrange(0,4)
        directions_list = [ 'n','s','e','w']
        player_room_directions = get_directions(room_id)
        movement = directions_list[random_exit]
        print("movement", movement)
        if player.travel(directions_list[random_exit]) is not None:
            #adding the found path to the current room
            next_room_id = player.current_room.id
            print("id", room_id, "movement", movement)
            visited[room_id][movement] = next_room_id
            #grabing the new room from the world
            new_room = get_directions(next_room_id)
            print("new Room", new_room)
            visited[next_room_id] = new_room
            visited[next_room_id][opposites[movement]] = room_id
            print("visited", visited)
            #gotta add the reverse

            move.append(movement)
            room_id = player.current_room.id
            room_options = len(player_room_directions)


    print("dead end time")
    print("roomid", visited)
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
