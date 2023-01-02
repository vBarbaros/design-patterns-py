# Main idea
In object-oriented programming, the chain-of-responsibility design pattern is a design 
pattern consisting of a source of command objects and a series of processing objects. 
Each processing object contains logic that defines the types of command objects that it 
can handle; the rest are passed to the next processing object in the chain. A mechanism also 
exists for adding new processing objects to the end of this chain.

# Also known as
* Chain of command
* Responsibility chain
* Chain of delegation
* Responsibility chain pattern
* Chain of authority
* Chain of handling
* Chain of processing
* Chain of control

# Why you need it
This pattern allows a request to be passed through a chain of objects until it is handled,
without the sender of the request necessarily knowing which object will handle the request. 
It also allows new processing objects to be added to the chain dynamically.

# When to use
The chain-of-responsibility pattern is useful in situations where a request may be handled by 
any one of a number of objects in a system, and the exact handler is not known beforehand. 
It can also be used to reduce coupling between classes, as the exact type and number of handler 
objects is not known at compile-time.

## Generic Example
### Class Diagram
![](cor/.png)

### Link to [source-code for COR - generic example](cor_generic.py)

## Loan Application Example
### Class Diagram
![](diagrams/strategy-investment.png)

### Link to [source-code for COR - loan application example](cor_loan_application.py)


<hr>

[>> back-to-creational](../README.md)

[>> back-to-main](../../README.md)