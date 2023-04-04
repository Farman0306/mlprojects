from setuptools import find_packages,setup
from typing import List

hypen_e = '-e .'

def get_requirements(file_path)->List[str]:

    """
    this func will return the list of requirements
    """
    req =[]
    with open(file_path) as f:
        req = f.readlines()
        req = [i.replace("\n","") for i in req]

        if hypen_e in req:
            req.remove(hypen_e)
    return req





setup(
name = 'mlproject',
version='0.0.1',
author='Farman',
author_email='test95myemail@gmail.com',
packages= find_packages(),
install_requires=get_requirements('requirements.txt')

)