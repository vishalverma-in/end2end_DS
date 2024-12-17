from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()     # read requirements line by line
        requirements = [req.replace("\n", " ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name = 'ml_project',
    version = '0.0.1',
    author = 'vishal_verma',
    author_email = 'vishalverma.code@gmail.com',
    packages = find_packages(),               # it finds __init__.py files in the directory and start building that package where it is found
    install_requires = get_requirements('requirements.txt')  
)