# Un simple oracle 2 : Chosen Cipher Attack but with a twist

# Task

Same as before except, the modulus is hidden from us.

# Process

Well this one is the same as before except for the last step we need the modulus and they just hid it away from us.

Let's take a look at the operation done by the oracle :

$$ m \equiv c^d[n] $$

Well, quick and easy maths, let's try to just input -1 because : 

$$ \text{if $d$ is odd : } \\ (-1)^d \equiv n-1  [n] \\
\text{else:} \\ (-1)^d \equiv n-1  [n] 
$$

Well bingo ! Then we just repeat the same thing as in the first part and get our flag using python.