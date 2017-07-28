# C9-Login-API
An unofficial wrapper for Cloud9's services

### How to use it ###

```python
import C9

print C9.login("email","password") # Params= email/username,password

# It'll return a list, containing [False,"Dead"] if the account is dead
# or [True,"Working"] if it isn't

```
