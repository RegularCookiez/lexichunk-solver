# Lexichunk Solver Guide

Lexichunk is a word game where you have a deduce a final word by piecing together word chunks that are taken out of lists of words.

Each column of words has a specific group of letters taken away anywhere in the word. Those group of letters will be used as part the chunk word. Find the chunk word based on the removed groups of letters, from left to right.

![My Image](lexichunk_example.jpg)

To use the Python solver, simply enter the number of columns, then enter the words removed of their chunks separated by spaces.
The program will use a custom dictionary to solve for them, and output potential solutions below, separating each chunk with a slash.

---

Below is an example of how to use the Lexichunk solver. (You must have lexichunk.py and dictionary.txt installed in the same folder)

Let us say we are given the two columns `che ders bale pake` and `sten ase tax tough`.

We first enter the number of columns, which is 2:

```
your_username@HOSTNAME:~$ python3 lexichunk.py
How many columns are there?
2
```

The program will prompt you for the shortened words of each column.

Fill in the following:

```
What are the shortened words in Column 1?
che ders bale pake
```

```
What are the shortened words in Column 2?
sten ase tax tough
```

After inputting the columns, it will try to solve for the columns and display the current progress.

Once it's done, it will display all found solutions:

```
Lexichunk Solved!

Column 1: che ders bale pake
Column 2: sten ase tax tough

All Possible Chunks:
Column 1: anc
Column 2: hor

All Solutions (1)
anc/hor

Search completed in 15.23s.
```

As you can see, it found the solution anchor having found original words with those chunks.

While not displayed, you can determine them retroactively:

```
ch(anc)e d(anc)ers bal(anc)e p(anc)ake
s(hor)ten as(hor)e t(hor)ax t(hor)ough
```


