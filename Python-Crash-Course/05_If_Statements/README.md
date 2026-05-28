## Completed Chapter 05 If Statements.  
### Resources and Materials.  
[📄 Click here to open the Annotated PDF](resources_used/05-if-statements-annotations.pdf)
### Key Insights and Progress Log.  
>Programming often involves examining a set of conditions and deiciding which action to take based on those conditions. Python's `if` statement allows us to examine the current state of a progeam and respond appropriately to that state.
>At the heart of `if` statement is an expression that can be evaluated as True or False and is called a `conditional test`.
>The first conditional test we learnt is `Checking for Equality`. The `equality operator` i.e... `==` returns `True ` if the values on the left and right side of the operator match, and `False` if they dont. Know that a single equal sign `=` is really a `statement` which sets the value of the variable as a label for a value, e.g... `car = "audi"` sets the value of the variable 'car' equal to the string ""audi"". on the other hand double equal sign, `==` asks a question, `car == "audi"` - "is the value of car equal to audi?" (which will return "True" if we had set the variable car as above). Know that checking for equality is case sensitive in python, sometimes it is advantageous but if you dont want it, you can use the lower() method, by brain! (know that the lower() method doesnt change the value that is originally stored).
>We can also `Check for Inequality` in python by using the `inequality operator`, i.e... `!=`, if the 2 values on either side of this operator does not match, it returns `True` and when they does, we get `False`.
>We can also easily do `Numerical Comparisons`, all the operators `==` `!=`, `>`, `<`, `>=`, `<=` work as you would expect them to, returning `True` or `False` as prompted, for example coding `age = 18` then `print(age > 27)` will return False... so on.
>We may want to `Check Multiple Conditions` at the same time, the keywords `and` and `or` can help in these situations. We can combine 2 conditional statements by an `and` to check if they are both True, or by an `or` to check if either is True, e.g... in 2 tests combined with `and` we will get `True` if both test passes, and a `False` if either or both tests fail / in 2 tests combined with `or`, we get `True` if either or both tests pass and a `False` only when both tests fail, after coding `age = 18`, `age > 17 and age<=27` returns `True` and `age < 5 or age == 27` returns `False`. (we can also seperate the 2 conditonal statements visually be putting them in parenthesis, doesnt affect the code but improves readability).
>We can also `Check Whether a Value Is in a List` by using the keyword `in`, e.g... `<value> in <list_name>` returns `True` if the list contains the value, and `False` if it does not (know that its case sensitive, it needs to be the exact value in the list for `True`) basically the keyword `in` tells python to check for the existence of <value> in <list_name> list. Conversely, we can also `Check Whether a Value is Not in a List`, by the keyword `not in` (works as obvious).
>A `Boolean Expression` is just another name for the conditonal test. A `Boolean Value` is either `True` or `False`, just like the value of a conditional exression after it has been evaluated.
>
>After understanding conditional statements, we can now write `if statements`, several kinds of them exist, we use the one that serves our purpose, depending on the number of conditions we need to test and how they need to be tested.
>`Simple if statements` has one test and one action
>```code
>if conditional test:
>     do something
>```
>We can put any conditional test in the first line and just about any action in the indented block following the test. If the conditional test evaluates to `True`, Python executes the indented code following the `if` statement, if the test evaluates to `False`, Python ignores the indented code following the `if` statement (indented code as in all of the indented lines just after the `if` statement) (indentation playes the same role in `if` statements as it did in `for` loops.).
>
>`if-else statements`, if we want to take one action when a conditional test passes and a different action in all other cases, we can use Python's `if-else syntax`. An if-else block is similar to a simple `if` statement, but the `else` statement allows us to define an action or set of actions  that are executed when the conditional test fails. The blueprint of an `if-else block` goes like:
>```code
>if statement:
>    do something
>else:
>    do something
>```
>if the if condition passes the indented lines below it are executed and the else block is ignored, and if the if condition fails, the indented code below it is ignored and the else block, i.e... the indented lines below `else:` are executed. (know that an `if-else-block` like this only works if we want python to always ecevute one of two possible actions, in a simple `if-else chain` like this, one of the two actions will always be executed.)
>`if-elif-else chain`, if we need to test more than 2 possible situations, we can use python's `if-elif-else syntax`. Python executes only one block in an if-elif-else chain. It runs a conditional test in order, until one passes, when it does, the indented code following that test is executed and Python skips the rest of the tests. The blueprint is:
>```code
>if statement:
>    do something
>elif statement:
>    do something
>elif statement:
>    do something
>.
>.
>.              # as many `elif` blocks as we want
>else:
>    do something
>```
>Know that the elif line is really just another if test, which runs only if the previous tests in the if-elif-else chain failed, and if all the `if` and `elif` tests failed in the `if-elif-else chain`, then the else block of code runs, else has no conditional test, it covers every single situation not covered by the preceding if and elif statements, know that we can also omit the else block from a potential `if-elif-else chain` and just end in an elif, this can be useful by making the code cleaner by setting clear boundries as conditions in every block rather than a general `else` block, with this change, every block of code must pass a specific condition in order to be executed. (The `else` block is a `catchall` statement. It matches any conditon that wasnt matched by a specific `if` or `elif` test, and that can sometimes inclide invalid or even malicious data.
> The `if-elif-else` chain is powerful, but its only appropriate to use when you need one test to pass. As soon as python finds one test that passes, it skips the rest of the tests, however sometimes its important to check all condition in interest, for this we can just use a series of simple `if` statements with no `elif` or `else` blocks. It will skip no blocks of code this way, it makes sense to use it if we want to act on every single condition that is true, just goes like:
>```code
>if statement:
>    do something
>if statement:
>    do something
>.
>.
>.
>if statement:
>    do something
>```
>In summary if we want one block of code to work to run, we use an `if-elif-else chain`. If more than one block of code needs to run, use a series of independent if statements.
>
>We can do some interesting work by `Using if statements with list`.
>An `if statement inside the for loop` can handle many situation appropriately, a simple blueprint is:
>```code
>requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza.")
```
