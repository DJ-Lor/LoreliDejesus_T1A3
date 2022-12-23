# #!/bin/bash

if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    py3v="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python -m venv venv
        source venv/bin/activate
        pip install email_validator
        python ./main.py
    elif [[ $py3v == "Python 3"* ]]
    then
        python3 -m venv venv
        source venv/bin/activate
        pip install email_validator
        python3 ./main.py

    else
        echo "You've got the wrong version of python. Please check out https://installpython3.com/" >&2
    fi 
else
    echo "You don't have python, go get it!" >&2
fi



# if ! python -V 2>&1 &> /dev/null || command python -v &> /dev/null
# then
#     echo 'You do not have python installed. Please check out https://installpython3.com/'
#     exit
# fi

# if command python3 -v &> /dev/null
# then 
#     python3 -m venv venv
#     source venv/bin/activate
#     pip install os, email_validator, json
# fi

# if command python -v &> /dev/null
# then 
#     python3 -m venv venv
#     source venv/bin/activate
#     pip install os, email_validator, json
# fi

# python3 ./main.py



# # check if python is installed and what version

# if [[ -x "$(command -v python)" ]]
# then
#     pyv="$(python -V 2>&1)"
#     if [[ $pyv == "Python 3"* ]]
#     then
#         python chmod +x ./main.py
#         python3 -m venv venv
#         source venv/bin/activate
#         pip install os, email_validator, json
#         python3 ./main.py

#     else
#         echo "You've got the wrong version of python, download version 3 & up!" >&2
#     fi 
# else
#     echo "You don't have python, go get it!" >&2
# fi

# # download and activate virtual environment

# # python3 -m venv venv

# # source venv/bin/activate

# # install packages 

# pip install os, email_validator, json

# #run the python file

# python3 ./main.py