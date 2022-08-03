# Un simple oracle 1 : Chosen Cipher Attack

## Task

We have access to an oracle that lets us decrypt anything we want and we are given the ciphertext.

## Process

Right off the bat, it's RSA. The exponent and modulus are given to us and we have something to decipher. We seem to be able to decrypt anything we want. Issue we can't decrypt the ciphertext using the oracle. If we formulate our problem mathematicaly, we get this :

$$ \text{Find } m \\
c \equiv m^e [n] $$

We can encrypt anything we want so we can try to figure out mathematically how can we trick it to decipher our message. So we bring out the text books and find that we can actually perform a Chosen Cipher Attack. Which goes like this :


$$ r \in N^\star, c' = c*r^e $$

We give $c'$ to the Oracle and he gives us this back :


$$ 
\begin{align}
 &m' \equiv (c')^d [n] \\
 \iff &m' \equiv (c*r^e)^d[n] \\ 
 \iff &m' \equiv c^d* (r^e)^d[n] \\
 \iff &m' \equiv (m^e)^d(r^e)^d [n]
\end{align}
$$

We know that

$$ (m^e)^d \equiv m [n] $$

So,

$$ m' = m * r [n] $$

And finally to get the deciphered text :

$$ m = m'/r $$

We do those operations in python and easy peasy, we get our flag :
