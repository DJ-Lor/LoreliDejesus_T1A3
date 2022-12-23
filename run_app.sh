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


