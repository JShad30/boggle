def make_grid(width, height):
    """
    Creates a grid that will hold all the tiles for a boggle game
    """
    return{(row, column): ' ' for row in range(height)
        for column in range(width)
    }