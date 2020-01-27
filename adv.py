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
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# print( "Room 8", room_graph[8][1].keys())
# print( "Room 9", room_graph[9][1].keys())  #interesting mystery on why 8 is not connected to 9 but 9 is connected to 8
# print( "Graph", room_graph)
### helper
# def pretty(d, indent=0):
#    for key, value in d.items():
#       print('\t' * indent + str(key))
#       if isinstance(value, dict):
#           print(value)
#       else:
#          print('\t' * (indent+1) + str(value))

def get_directions(room_id):
    # print("I'm running", room_graph[room_id][1].keys())
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
    # if room_id == 9:
    #     print("HELLO", valid_directions)
    return valid_directions
def check_next_room_exits(next_id, next_direction, prev_id):
    # print("I'm running", next_id)

    opposites = { 'w': 'e', 's': 'n', 'n': 's', 'e': 'w'}
    next_array = []
    pre_array = []
    for d in room_graph[next_id][1].keys():
        if d == 'n':
            next_array.append('s')
        if d == 's':
            next_array.append('n')
        if d == 'e':
            next_array.append('w')
        if d == 'w':
            next_array.append('e')
    for i in room_graph[next_id][1].keys():
        pre_array.append(opposites[i])
    if next_direction in next_array:
        # print("we are good")
        return True
    else:
        # print("warning!")
        # print(next_direction)
        return False






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

def big_loop(starting_room):
    #Create an empty stack and push starting vertex Id


    room_id = (starting_room)

    # Create a Set to store visited vertices
    visited = { starting_room : get_directions(starting_room)}
    opposites = { 'w': 'e', 's': 'n', 'n': 's', 'e': 'w'}
    room_options = len(room_graph[starting_room][1].keys())
    moves = []
    tracked_rooms = set()
    current_room = starting_room

    while len(visited) < 500:
        print("STuck here? dft")

        while '?' in visited[current_room].values():


            # random_exit = random.randrange(0,4)
            # directions_list = [ 'n','s','e','w']
            player_room_directions = visited[current_room]
            array_possible_exits = []
            index = 0
            # print("-------------------------->", visited[0])
            # input(")))))))))))))))))))")
            for e in list(player_room_directions.values()):
                if e == '?':

                    array_possible_exits.append(list(player_room_directions.keys())[index])
                    # print("ARRAY OF P", array_possible_exits)
                index += 1
            if len(array_possible_exits) == 0:
                print("dead end")
                break
            # print("-------------------------->", visited[0])
            next_direction = array_possible_exits[random.randrange(len(array_possible_exits))]
            # print("Next directions", next_direction)
            # print("dir array", array_possible_exits)
            next_room = room_graph[current_room][1][next_direction]
            # print("prev room", current_room)
            # print("next room!!!!",next_room, room_graph[next_room][1].keys())
            next_room_check = check_next_room_exits(next_room, next_direction, current_room)

            # print("next_room", next_room)
            # print("next_room_check", next_room_check)

            moves.append(next_direction)
            if next_room_check == True:
                # visited[next_room] = get_directions(next_room)
                print(next_direction)
                visited[current_room][next_direction] = next_room
                if next_room not in visited:
                    visited[next_room] = get_directions(next_room)
                    print("here!!!!", visited[next_room])
                    visited[next_room][opposites[next_direction]] = current_room
                else:
                    visited[next_room][opposites[next_direction]] = current_room
            if next_room_check == False:
                if next_room not in visited:
                    # breakpoint()
                    print("danger zone")
                    visited[current_room][next_direction] = next_room
                    visited[next_room] = get_directions(next_room)

                # print(visited[next_room])
                print("danger zone2")
                # visited[current_room][next_direction] = next_room

                # current_room = next_room
            # print("room_check", next_room_check)
            # print("current_room", current_room)
            # print("next_room", next_room)
            current_room = next_room


                # visited[next_room] = get_directions(next_room)

                # print(next_room)
                # print(visited[next_room], "wrewrwrewrwerew")
                # print(visited)


                # print("false room", visited[next_room][next_direction].values())
                # if 'f' in visited[next_room][next_direction].values():
                #     break
                #     print("false room", visited[next_room])
                #


            # world.print_rooms()
            # print("visited", visited)
            # input("-----------------------------")


            # world.print_rooms()
            # pretty(visited)

            # current_room = next_room
            # print("Current Room", current_room)
            # input("--------------------------------------------")

       # Create an empty queue and enqueue a PATH TO the starting vertex ID
            # Create a Set to store visited vertices
            # While the queue is not empty...
                     #Dequeue the first PATH
                #Grab the last vertex from the PATH
                #If that vertex has not been visited...
                    #CHECK IF IT'S THE TARGET
                        #IF SO, RETURN PATH
                    #Mark it as visited..
                    #Then add a PATH TO its neighbors to the back of the queue
                        #COPY THE PATH
                        #APPEND THE NEIGHBOR TO THE BACK
        # print("dead end time")
        # print("Current Room@#$@$@#$@#$@#$23", current_room)
        # print("roomid", visited)
        # print("dfs", moves)
        while len(visited) < 500 and '?' not in visited[current_room].values():
            print("STuck here?")
            queue = Queue()
            player_room_directions = visited[current_room]
            v = set()
            for key, value in player_room_directions.items():
                queue.enqueue([value,[key]])
            while queue.size() > 0:
                # print("stuck queue?")
                this_one = queue.dequeue()
                room = this_one[0]
                if room not in v:
                    # print(len(moves))
                    # print("visited_rooms", visited[room].values())
                    if '?' in visited[room].values():
                        # breakpoint()
                        current_room = room
                        moves += this_one[1]
                        break
                v.add(room)

                player_room_directions = visited[room]
                for key, value in player_room_directions.items():
                    path_copy = this_one[1].copy()
                    path_copy.append(key)
                    queue.enqueue([value, path_copy])
                    # print(queue.queue)

    #         print("bfs", moves)
    #         print("bfs", current_room)
    #         print("--------------------------------")
    #         # breakpoint()
    # print("visited", v)
        print(len(visited))

    return moves

moves_1 = big_loop(player.current_room.id)

# print("move array", move)
traversal_path = moves_1
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
    print(len(moves_1))
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
