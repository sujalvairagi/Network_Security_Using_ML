'''this file is essential 
    used by setuptools for packing and distribution'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_lst: List[str] = []

    '''this function returns the list of requirements from requirements.txt'''
    try:
        with open('requirements.txt', 'r') as file:
            lines= file.readlines()
        # PROCESS each line
        for line in lines:
            requirement = line.strip()
            if requirement and requirement!='-e .':
                requirement_lst.append(requirement)

    except Exception as e:
        print(f"Error occurred while reading requirements: {e}")

    return requirement_lst 

setup(
    name='your_package_name',
    version='0.1',
    author="sujal vairagi",
    author_email="sujal@example.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)