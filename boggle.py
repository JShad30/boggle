from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """Creates a grid that will hold all the tiles for a boggle game"""
    
    #The choice method returns a random item form a list, tuple or string.
    
    return {(row, column): choice(ascii_uppercase) 
        for row in range(height)
        for column in range(width)
    }
    
    #The grid has been created using a dictionary data structure in python
    
def neighbours_of_position(coords):
    """Get neighbours of a position"""
    row = coords[0]
    column = coords[1]
    
    #Assign the neighbours for each of the positions
    #Top left to top right
    
    top_left = (row -1, column -1)
    top_center = (row -1, column)
    top_right = (row -1, column +1)
    
    #left and right neighbour
    
    middle_left = (row, column -1)
    middle_right = (row, column +1)
    
    #Bottom left to bottom right
    
    bottom_left = (row +1, column -1)
    bottom_center = (row +1, column)
    bottom_right = (row +1, column +1)
    
    return [top_left, top_center, top_right, middle_left, middle_right, bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """Get all possible neighbours for all the positions in the grid"""
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def path_to_word(grid, path):
    """Add all of the letters on a path to a string"""
    return ''.join([grid[p] for p in path])

def word_in_dictionary(word, dict):
    return word in dict

def search(grid, dictionary):
    """Search through the paths to match the strings to words in a dictionary"""
    neighbours = all_grid_neighbours(grid)
    paths = []
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word_in_dictionary(word, dictionary):
            paths.append(path)
        for next_position in neighbours[path[-1]]: #The last item in the list path is chosen when using path[-1] here.
            if next_position not in path:
                do_search(path + [next_position])
                
    for position in grid:
        do_search([position])
            
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
            
    return set(words)
    
def get_dictionary(dictionary_file):
    """Load dictionary file"""
    with open(dictionary_file) as f:
        return {w.strip().upper() for w in f}
    
def main():
    """This is a function that runs the whole project"""
    grid = make_grid(4, 4)
    dictionary = get_dictionary("words.txt")  
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
# Following code states that main() should only be run if the name given in the console is boggle.py. Main will not run when imported into the test_boggle.py.

if __name__ == "__main__":
    main()
    