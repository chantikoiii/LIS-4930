# WIP
import sys
from datetime import datetime
from datetime import time
from datetime import date

def timeNow():
    current = datetime.now()
    setup = current.strftime("%X")
    print(setup)

    '''for i in setup:
        data = setup.strip().split("\t")
        print(data)'''

timeNow()
    
# WIP
# THIS IS NOT COMPLETE
    


