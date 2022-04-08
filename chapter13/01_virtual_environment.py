'''
    Virtual environment:
    An environment which is same as the system interpretor but is isolated from the other python environments on the system. Seperate module haru halnako laagi yo use hunchha
    
    To install it we use command:
        -pip install virtualenv
    
    To create a new environment we use command:
        -virtualenv myprojectenv
    it makes folder

    To use it we should activate it in terminal
        if linux: - source myprojectenv/bin/activate
        if windows powershell:  
            .\myprojectenv\Scripts\activate.ps1

    Now if we pip install something, something will be stored in virtual environment bhako module harulai pani feri install garnuparchha

    but by typing command 
        - deactivate
    it deactivates this project environment and it comes out to system interpretor

    or activate vs code ko interpretor choose garne thaubata garna milchha but new terminal kholesi matrai kaam garchha

    We can delete the virtual environment by deleting  folder

    We can see the list of packages in current environement by typing command:
        - pip freeze

    To add these in requirements.txt in same directory, we can use command 
        -pip freeze > requirements.txt

    we can distribute this file to other users and they can recreate the same environment using command:
        - pip install -r requirements.txt

    you can delete the env directory create new env directory activate it and run above command to recreate it


'''
import pandas
# import pygame # not availabe in current virtual env



