#!/bin/bash
{ # try
    cd logic
    python ../main.py
    cd ..
    #save your output

} || { # catch
    { # try
        cd logic
        python3 ../main.py
        cd ..
        #save your output

    } || { # catch
        :
    }
}