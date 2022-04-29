# Jurassic Park
50 points - Web - 946 Solves - easy
Expires in: 00:59:15
Author: @artemis19#5698

Dr. John Hammond has put together a small portfolio about himself for his new theme park, Jurassic Park. Check it out here!

PS (not challenge related), thank you so much to INTIGRITI for supporting NahamCon 2022!

Press the Start button on the top-right to begin this challenge.

## Solving
robots.txt

```
User-agent: *
Disallow: /ingen/
```

Content of the ingen dir
```
Index of /ingen
Parent Directory
flag.txt
```

There it is... :)

curl -s http://challenge.nahamcon.com:31171//ingen/flag.txt
