countries = ['wa', 'nt', 'q', 'nsw', 'v', 'sa']
possvalues = []
colours =['orange', 'green', 'blue']
peers = {'wa': ['nt', 'sa'], 'nt':['wa', 'sa', 'q'], 'sa': ['wa', 'nt', 'q'], 'q': ['nt', 'sa', 'nsw', 'v'], 'nsw': ['q', 'sa', 'v'], 'v' : ['nsw', 'sa', 'q']}

# create dict with box and poss values obg
def createposs():
    for x in countries:
        possvalues.append('ogb')
    print(possvalues)
    possvalues[0] = 'g'
 
    grid = dict(zip(countries, possvalues))
    return grid

def eliminate (grid):
    solvedvalues =[]
    for x in grid:
        if len(grid[x]) == 1 :
            solvedvalues.append(x)

    for x in solvedvalues :
        for i in peers[x]:
            for a in grid[i] :
                if a == grid[x] :
                    grid[i] = grid[i].replace(a, '')

    return grid


def search(grid1):

    grid2 = eliminate(grid1)
    #check if solved return false if not

    if all(len(grid2[s]) == 1 for s in grid2):

        print ('its solved')
        return grid2

    elif len([i for i in grid2 if len(grid2[i]) == 0]) >0  :

        print ('it failed')
        return False

    else:
        print(grid2)
        for i in grid2.keys():
            print (i)
        #find box with least values to guess
        s, n = min((len(grid2[i]), i) for i in grid2.keys() if len(grid2[i]) >1)


        #take guess using found box with min options
        for i in grid2[n]:
            propgrid = grid2.copy()
            propgrid[n] = i
            attempt = search(propgrid)
            if attempt:
                print(attempt)
                return attempt
