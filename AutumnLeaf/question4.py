import os
 
env_var = input('enter an environment variable to search:\n')
 
if env_var in os.environ:
    print('{env_var} value is {os.environ.get[env_var]}')
else:
    print('{env_var} does not exist in the list')