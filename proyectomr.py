import heapq

 

# Define el tamaño de las cuadras y la posicion de Javier y Andreina

grid_size = (6, 6)

javier_start = (4, 4)

andreina_start = (2, 3)

 

# define la posicion de los establecimientos

establishments = {

    "The Darkness": (0, 4),

    "La Pasión": (4, 1),

    "Mi Rolita": (0, 2)

}

 

# Define la caminata dependiendo del tipo de acera

normal_time_javier = 4

normal_time_andreina = 6

bad_sidewalk_time_javier = 6

bad_sidewalk_time_andreina = 8

commercial_time_javier = 8

commercial_time_andreina = 10

 

# Define las cuadras con aceras es mal estado

bad_sidewalks = [(2, i) for i in range(6)] + [(3, i) for i in range(6)] + [(4, i) for i in range(6)]

commercial_blocks = [(i, 1) for i in range(6)]

 

# Funcion que calcula el tiempo de caminata

def walking_time(block, person):

    if block in bad_sidewalks:

        return bad_sidewalk_time_javier if person == "Javier" else bad_sidewalk_time_andreina

    elif block in commercial_blocks:

        return commercial_time_javier if person == "Javier" else commercial_time_andreina

    else:

        return normal_time_javier if person == "Javier" else normal_time_andreina

 

#Funcion que busca la ruta mas corta por el algoritmo de djikstra

def shortest_path(start, end, person):

    pq = [(0, start)]

    distances = {start: 0}

    previous = {start: None}

 

    while pq:

        current_distance, current_block = heapq.heappop(pq)

 

        if current_block == end:

            break

 

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            neighbor = (current_block[0] + dx, current_block[1] + dy)

            if 0 <= neighbor[0] < grid_size[0] and 0 <= neighbor[1] < grid_size[1]:

                distance = current_distance + walking_time(neighbor, person)

                if neighbor not in distances or distance < distances[neighbor]:

                    distances[neighbor] = distance

                    previous[neighbor] = current_block

                    heapq.heappush(pq, (distance, neighbor))

 

    path = []

    while end:

        path.append(end)

        end = previous[end]

 

    return path[::-1], distances[path[0]]

 

# Funcion que calcula tiempo y trayectoria de las rutas

def calculate_trajectories(destination):

    javier_path, javier_time = shortest_path(javier_start, establishments[destination], "Javier")

    andreina_path, andreina_time = shortest_path(andreina_start, establishments[destination], "Andreína")

 

    if javier_time > andreina_time:

        return javier_path, andreina_path, "Andreína", javier_time - andreina_time

    elif andreina_time > javier_time:

        return javier_path, andreina_path, "Javier", andreina_time - javier_time

    else:

        return javier_path, andreina_path, None, 0

 

# Ejemplo de uso

destination = "The Darkness"

javier_path, andreina_path, early_person, early_time = calculate_trajectories(destination)

 

print(f"Ruta de Javier: {javier_path}")

print(f"Ruta de Andreina: {andreina_path}")

if early_person:

    print(f"{early_person} Debe salir {early_time} minutos antes.")

else:

    print("ambos deben salir al mismo tiempo.")