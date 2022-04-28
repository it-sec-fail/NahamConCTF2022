# Prisoner
463 points - Warmups - 89 Solves - easy
Expires in: 01:00:12
Author: @JohnHammond#6971

Have you ever broken out of jail? Maybe it is easier than you think!

PS (not challenge related), thank you so much to Zero-Point Security for supporting NahamCon 2022!

Press the Start button on the top-right to begin this challenge.

## Solving

Connect to via ssh to the server

```shell
  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\
   / ||--_||_____||_--|| \
  (_(||)-| SP1337 |-(||)_)
          --------

Hello prisoner, welcome to jail.
Don't get any ideas, there is no easy way out!
: 
```

Okay - lets try to break out... 

STRC + C - nope
STRC + D - oh great.... python :)

Lets try to read the filesystem...

```python
>>> import os
>>> os.listdir(".")
['flag.txt', 'jail.py', '.user-entrypoint.sh', '.profile', '.bashrc']
```
Yes... okay... lets read the file :)

>>> with open('flag.txt','r') as file:
...     lines = file.readlines()
...     print(lines)
... 
['flag{c31e05a24493a202fad0d1a827103642}\n']


