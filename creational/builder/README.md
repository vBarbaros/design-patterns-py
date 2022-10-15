# Main idea
Separate the construction of a complex object from its representation 
so that the same construction process can create different representations.


# Also known as
N/A

# Why you need it
When a specific functionality is provided by a considerably complex class
you would prefer to have a template of such a class so that for variations
of the aforementioned functionality it is easy add new classes of similar
complexity.

## Generic Example
### Class Diagram
![](diagrams/builder-generic.png)

### Link to [source-code for builder - generic example](builder_generic.py)


## Financial Portfolio Example


### Class Diagram
![](diagrams/builder-financial-portfolio.png)

### Link to [source-code for builder - financial portfolio example](builder_portfolio.py)



<hr>

[>> back-to-creational](../README.md)

[>> back-to-main](../../README.md)