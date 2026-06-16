from setuptools import setup, find_packages
from typing import List

requirements=[]
HYPEN_DOT_E="-e ."
def get_requirement(file_path:str)->list[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements

setup(
    name="House_prediction",
    author="Warith",
    author_email="biliaminwarith68@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requirement=get_requirement("requirements.txt")
)