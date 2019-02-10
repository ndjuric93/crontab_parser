# Crontab input parser

Simple crontab input parser written in Python3

## Example Inputs

### Example 1:

Input
```
python3 crontab_parser.py 5 0 1 2 0 /usr/bin/sample.sh
```
Output
```
Minute: 5
Hour: 0
Day of the month: 1
Month: 2
Day of the week: 0
Command: /usr/bin/sample.sh
```

### Example 2:

Please take a note that asterisk sign (*) has to be under quotes if ran from command line. If not, all of the file names will be passed as argument.

Input
```
python3 crontab_parser.py 0 0 1,15 1-3 '*' /bin/foo bar
```
Output
```
Minute: 0
Hour: 0
Day of the month: 1 15
Month: 1 2 3
Day of the week: 0 1 2 3 4 5 6
Command: /bin/foo bar
```

### Example 3

Input 
```
python3 crontab_parser.py 0 2-7/2 1-3 4 5 echo Hello world
```
Output
```
Minute: 0
Hour: 2 4 6
Day of the month: 1 2 3
Month: 4
Day of the week: 5
Command: echo Hello world
```
