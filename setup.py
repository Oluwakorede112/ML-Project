from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .' # the '-e .'  in the requirements.txt file actually connects the setup file to build up but we actually do not need it in our setup file here. we just use it to connect the setup file to build up with those libraries.
# it mapps the setup.py file. It is an indication that the setup.py file is there and then the entire packages gets built (where, we'd have all the entire info in the setup below gets built).
def get_requirements(file_path:str) ->List[str]:
   
   '''
   this function will return the list of requirements
   '''
   requirements = []
   with open(file_path) as file:
       requirements = file.readlines() #reads each line in the file
       requirements = [r.replace('\n', "") for r in requirements] #when it tries to return the list, it would return new lines (\n), so we had to replace the newlines with an empty string.
       
       if HYPHEN_E_DOT in requirements:
           requirements.remove(HYPHEN_E_DOT) #removes the '-e .' if it exists in the list.

   return requirements

 
setup(
    name = 'ML Project',
    version= '0.0.1',
    author = 'Elijah Ogundipe',
    author_email='elijahhayomedey@gmail.com',
    find_packages = find_packages(), #returns a list of all python items (packages or modules, depending on the finder implementation), found within the directory 'where'. 'Where', is the root directory which will be searched. it should be supplied as a "cross-platform" (i.e URL-style) path; it will be converted to the appropriate local path.
    include_package_data=True,
    description='Machine Learning project for predicting house prices',
    url='https://github.com/ElijahOgundipe/ML-Project',
    install_requires=get_requirements('requirements.txt')
)