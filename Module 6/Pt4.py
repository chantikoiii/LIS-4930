from datetime import datetime

def treeCheck(f,i):
    while i >= 12:
# assuring inch input does not exceed 1 foot
        print('Inches must not exceed 11. Please reenter:')
        n=int(input())
        i=n
# incorporating current time & formating apperance
    setup = datetime.now()
    layout = setup.strftime('%A %b %e %Y')
    print('Since', layout, 'your tree is',f, '\'',i,'" tall!')
    
treeCheck(5,8)



