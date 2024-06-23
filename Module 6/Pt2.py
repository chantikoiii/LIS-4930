from datetime import datetime  
from datetime import timedelta  
  
# taking current date and adding 2 years (104 weeks) & subtracting 60 seconds
print(datetime.now() + timedelta(weeks=104) - timedelta(seconds=60))