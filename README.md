# JetBrains Academy Project
- This project focusses mainly on the socket module of Python and specifically the client side.
- The project can't be run independently outside the test environment of Hyperskill.org.
- **To run outside a server side module must be written separately.**

## The objectives and sample running examples are following:

#### Objectives

The algorithm is the following:

Try all logins with an empty password.
When you find the login, try out every possible password of length 1.
When an exception occurs, you know that you found the first letter of the password.
Use the found login and the found letter to find the second letter of the password.
Repeat until you receive the ‘success’ message.
Finally, your program should print the combination of login and password in JSON format. The examples show two ways of what the output can look like.

#### Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

```> python hack.py localhost 9090
{
    "login" : "superuser",
    "password" : "aDgT9tq1PU0"
}
```
Example 2:

```
> python hack.py localhost 9090
{"login": "new_user", "password": "Sg967s"}
```
