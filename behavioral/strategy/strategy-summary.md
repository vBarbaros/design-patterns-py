# Intent
When we need to define multiple algorithms, it's easier to encapsulate each of them
and make them interchangeable for a certain client/scope in which they are used.
The strategy makes it very flexible to be used depending on the clients that try to.

# Also known as
Policy

# Motivation
Given a set of Clients C and a set of Algorithms A, we can have the following situations:
* Clients in C supporting multiple algorithms from A, may become too complex and hard to maintain;
* Many algorithms from A may be needed at different times, and we want to support only those need at certain times;
* It would be difficult to add new Algorithms in A, and/or modify the existing ones if we let them become embedded with clients;

We can avoid these issues by encapsulating each algorithm into separate classes. An algorithm that
is encapsulated in this way, is called a strategy.

## Generic Example
### Class Diagram

### Link to 

## <Name 1> Example
### Class Diagram

### Link to 
## <Name 2> Example
### Class Diagram

### Link to 

#### Link to [Main README](../../README.md)

# Bibliography:
1. **Design Patterns Elements of Reusable Object-Oriented Software** (by Erich Gamma, Richard Helm, Ralph Johnson, John M. Vlissides)
2. [Strategy on https://www.tutorialspoint.com](https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm)