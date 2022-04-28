# Personnel
500 points - Web - 2 Solves - easy
Author: @JohnHammond#6971

A challenge that was never discovered during the 2021 Constellations mission... now ungated :)

PS (not challenge related), thank you so much to HackerOne for supporting NahamCon 2022!

Press the Start button on the top-right to begin this challenge.
Attachments: [app.py](app.py)

## Solving
Look at the `app.py`
There is the sourcecode of the flask webpage.
Especially the regex to find the user looks interessting

```python
        if name:
            if name[0].isupper():
                name = name[1:]

        results = re.findall(r"[A-Z][a-z]*?" + name + r"[a-z]*?\n", users, setting)
        results = [x.strip() for x in results if x or len(x) > 1]

```

So, if we try to put a regex into the field... what would happen?

A `.` will print all kind of names...
Lets try an `or` search with `|`... something like `|.*` to get everything... 
There it is :) 

> flag{f0e659b45b507d8633065bbd2832c627}
