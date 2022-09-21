#!/bin/bash
{ # try
    cd logic
    python ../main.py
    cd ..
} || { # catch
    { # try
        cd logic
        python3 ../main.py
        cd ..
    } || { # catch
        :
    }
}