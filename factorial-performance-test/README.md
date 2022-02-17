# Factorial Performance Test 

I was curious which implementation of a factorial would have a better performance: 
1. Recursive factorial
1. Iterative factorial (using the enhanced for loop)
1. Functional (using reduce)

Since Python does not have tail call optimization, I imagined that the recursive algorithm would probably be the least performant. 

I wasn't sure about the iterative or functional approaches. Functional functions have the advantadge of being written in c-code and are thus faster. However, the cost of using a lambda function instead of a direct operation could make it worse. In the end, the practical tests show that the iterative approach has a better performance than the functional one. 