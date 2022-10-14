# Object Oriented Programming

## Pillars

### Inheritance

Also means what it reads as in objects inherit attributes and methods from other objects.
(The object Car is a parent to its child Volkswagen: many car brands can exist but Volkswagen makes cars their own way)
(e.g. Lamborghini makes sports cars(faster acceleration, wider tyres etc.) and Toyota makes general use cars (not
necessarily faster or with wide tyres). Each brand still makes cars, but each brand introduces different attributes to
their own/customer needs)

### Abstraction

Abstraction is basically generalisation, meaning implementing something and then generalising it enough for it to be
used by something different and somewhat related.
To mirror common features or attributes. ()

### Encapsulation

Means what it reads: to encapsulate something/ put it in a capsule. A small and confined space, resulting in a small
amount of functionality

### Polymorphism

- Overriding
    - The process of re-declaring a parent class' method with a different definition
- Overloading
    - The process of declaring a method with the same name multiple times, but with a different signature (parameter
      requirements)
- Ad hoc polymorphism
    - A common interface for an arbitrary set of individually specified types.
- Parametric polymorphism
    - Not specifying concrete types and instead use abstract symbols that can substitute for any
      type.
- Subtyping (also called subtype polymorphism or inclusion polymorphism)
    - When a name denotes instances of many classes
      related by some common superclass.

![](images/inheritance%20diagram.png)
1. create animal.py as a parent
2. create reptile.py as a child to inherit - abstract etc.
3. create snake.py and inherit from
4. create python_.py