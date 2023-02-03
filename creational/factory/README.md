# Main idea
The factory design pattern is a creational design pattern that provides an interface for 
creating objects in a super class, but allows subclasses to alter the type of objects that 
will be created.

# Also known as
* Factory method pattern 
* Virtual constructor pattern 
* Kit pattern

# Why you need it
In the factory pattern, a factory class creates objects of other classes based on a set of 
input parameters. The factory class is responsible for encapsulating the creation logic for 
a set of related objects, and providing a simple interface for creating these objects.

This pattern is useful when you need to create objects of various types that share a common 
interface, and the actual type of object to be created is not known until runtime. It allows 
you to create objects without specifying their concrete classes, and allows you to change the 
types of objects being created by changing the factory class.

## Generic Example
### Class Diagram
This is how factory design pattern could look like in the banking system.

Assume that a bank needs to process various types of transactions, such as deposits, 
withdrawals, and transfers. Each transaction type has its own logic for how it is processed, 
and the bank wants to allow for new types of transactions to be added easily.

### Link to 

## <Name 1> Example
### Class Diagram

### Link to 


[>> back-to-creational](../README.md)

[>> back-to-main](../../README.md)