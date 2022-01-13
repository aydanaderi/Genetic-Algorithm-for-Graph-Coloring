import random

def read_file(pth):
        with open(pth , 'r') as file:
            num_of_nodes = int( file.readline() )
            neighbours = []
            for index in range(1 , num_of_nodes + 1 ):
                file_line = file.readline()
                neighbours.append(file_line.split(' ')[:-1])        
        return neighbours

colors = ['RED' , 'BLUE' , 'WHITE' , 'YELLOW' , 'GREEN']
best_fitness = []
best_population = []
neighbours = read_file('graph.txt')
print('\nneighbours = ',neighbours)

connections = {}
for i in range(1,len(neighbours)+1):
    if(neighbours[i-1] == ['-1']) :
        connections[i] = []
    else :
        connections[i] = neighbours[i-1]
print('\nconnections = ',connections)

population = []
for i in range(0,5):
        Chromosome = []
        for i in range(0,len(neighbours)):
            Chromosome.append(colors[random.randint(0,4)])
        population.append(Chromosome)
print('\npopulation = ',population)

for r in range(0,50):
    different_color = []
    for i in range(0,5):
        row =[]
        for j in range(0,len(neighbours)):
            counter = 0
            for k in range(0,len(connections[j+1])):
                if(population[i][j] != population[i][int(connections[j+1][k]) - 1]):
                   counter = counter + 1
            row.append(counter)
        different_color.append(row)

    fitness = []
    sumation_fitness = 0
    best = 0
    x = -1
    for i in range(0,5):
        sumation = 0
        for j in range(0,len(neighbours)):
            sumation = sumation + different_color[i][j]
            sumation_fitness = sumation_fitness + different_color[i][j]
        fitness.append(sumation)
        if(sumation > best):
                best = sumation
                x = i
    best_fitness.append(best)
    best_population.append(population[x])

    prb = []
    for i in range(0,5):
        prb.append(fitness[i]/sumation_fitness)

    prb_cml = []
    sum_prb = 0
    for i in range(0,5):
        sum_prb = sum_prb + prb[i]
        prb_cml.append(sum_prb)

    parents = []
    count = 0
    while count < 2 :
            for i in range(0,5):
                rn = random.uniform(0,1)
                if(rn < prb_cml[i]):
                    parents.append(population[i])
                    count = count + 1
                if(count == 2):
                    break
                        

    rand_point = random.randint(1,len(neighbours) - 2)
    child1 = []
    child2 =[]
    for i in range(0,len(neighbours)):
        if( i < rand_point):
            child1.append(parents[0][i])
            child2.append(parents[1][i])
        else :
            child1.append(parents[1][i])
            child2.append(parents[0][i])


    population.remove(parents[0])
    population.remove(parents[1])  
    population.append(child1)
    population.append(child2)
    
    pm = 0.3
    pg = 0.3
    for i in range(0,len(population)):
        rand_pm = random.uniform(0,1)
        if(rand_pm < pm):
            for j in range(0,len(population[i])):
                rand_pg = random.uniform(0,1)
                if(rand_pg < pg):
                    new_colors = []
                    for k in range(0,len(colors)):
                        if(colors[k] != population[i][j]):
                            new_colors.append(colors[k])
                    color_rand = random.randint(0,len(new_colors) - 1)
                    population[i][j] = new_colors[color_rand]
    same_color = []
    result = []
    for i in range(0,5):
        row =[]
        for j in range(0,len(neighbours)):
            counter = 0
            for k in range(0,len(connections[j+1])):
                if(population[i][j] == population[i][int(connections[j+1][k]) - 1]):
                   counter = counter + 1
            row.append(counter)
        same_color.append(row)
    counter_end = 0
    for i in range(0,len(same_color)):
        sum_color = 0
        for j in range(0,len(same_color[i])):
             sum_color = sum_color + same_color[i][j]
        if(sum_color == 0):
             result = population[i]
             counter_end = counter_end + 1
             break
    if(counter_end != 0):
        print('\nright answer is = ',result)
        break
                
if(len(result) == 0):
        best = 0
        best_p = []
        for i in range(0,len(best_fitness)):
                if(best_fitness[i] > best):
                        best = best_fitness[i]
                        best_p = best_population[i]
        print('\nbest answer is = ',best_p)







