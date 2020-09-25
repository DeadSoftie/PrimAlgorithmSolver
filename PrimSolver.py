import re

largestpt = -1
graph = []
file = open('file_name.file_type', 'r') #Specify the file name and type from your present working directory to open

for i in file:
    if not re.match('//', i):   #Removing any comments in file using regular expressions
        data_val = i.split(' ') #Removing spaces in the values using the split function
        json_blob = {data_val[0] + '&' +data_val[1]: data_val[2].replace('\n', '')}    #Generating JSON and removing the new line at the end
        if int(data_val[0]) > largestpt:
            largestpt = int(data_val[0])    #Finding the largest node available in the file
        if int(data_val[1]) > largestpt:
            largestpt = int(data_val[1])            
        graph.append(json_blob)    #Appending the JSON to the currently empty graph

verts_qty = largestpt + 1
prim_result = []   #Final result for display
minimum_dist = {}   #Generating JSON for minimum distance
added_vertices = []  #Vertices that are added
added_vertices.append(int(list(graph[0].keys())[0].split('&')[0]))  # Add the first vertex to the added list

i = 0

while i < verts_qty:
    for vertex in range(len(graph)):
            v = list(graph[vertex].keys())[0].split('&')
            if (int(v[0]) in added_vertices or int(v[1]) in added_vertices) and (int(v[0]) not in added_vertices or int(v[1]) not in added_vertices):
                #To remove any other chances of data inclusion
                #These two parameters for the two vertices should be the only options
                if len(minimum_dist) == 0:
                    minimum_dist = graph[vertex]
                elif int(list(graph[vertex].values())[0]) < int(list(minimum_dist.values())[0]):
                        minimum_dist = graph[vertex]

    if (minimum_dist):
        prim_result.append(minimum_dist)
        if int(list(minimum_dist.keys())[0].split('&')[0]) not in added_vertices:
            added_vertices.append(int(list(minimum_dist.keys())[0].split('&')[0]))  #Appending the values to the added vertices list
        
        if int(list(minimum_dist.keys())[0].split('&')[1]) not in added_vertices:   #Appending the values to the added vertices list
            added_vertices.append(int(list(minimum_dist.keys())[0].split('&')[1]))
    minimum_dist = {}   #Resetting JSON and iteration variable
    i = i + 1

def print_all():    #Function to print the vertices and the cost
    print('The vertices of the Minimum Spanning Tree:\n')
    print(prim_result)
    cost = 0
    for i in prim_result:
            cost = cost + int(list(i.values())[0])
    print('\n\nThe cost of connecting the vertices through the Prism Algorithm: ', cost, '\n')

print_all()