

def minimum_moves(grid, startX, startY, goalX, goalY):
    # Complete this function
    minimum_moves = 0
    '''
    tempX = startX
    tempY = startY
    count = 0
    if tempX == goalX and tempY == goalY:
        return count
    elif tempX ==
    '''
    return minimum_moves


if __name__ == "__main__":
    n = int(input().strip())
    grid = input().strip().split(' ')
    startX, startY, goalX, goalY = input().strip().split(' ')
    startX, startY, goalX, goalY = [int(startX), int(startY), int(goalX), int(goalY)]
    result = minimum_moves(grid, startX, startY, goalX, goalY)
