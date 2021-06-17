
# Vue Snowman

Let's write a program to play a game of [Snowman](https://en.wikipedia.org/wiki/Snowman_(game))! Snowman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.


## Part 1: Get a Random Word

We can use [Axios](../docs/13%20-%20APIs%20and%20Ajax.md#ajax-in-axios) to send a request to this random word API.

```
https://random-word-api.herokuapp.com/word/?swear=0
```

## Part 2: Initialize the Display

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. Allow the user 10 tries to guess the letters of the word. If the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

```
_ _ _ _ _ _ _ _ _
Guesses remaining: 10
Guess a letter: a
2 a's found

_ a _ _ _ _ a _ _
Guesses remaining: 10
Guess a letter: k
0 k's found

_ a _ _ _ _ a _ _
Guesses remaining: 9
Guess a letter:
```


## Part 2

Keep track of the letters the user has already guessed. If they guess a letter they've guessed before, tell them and do **not** subtract 1 from their guesses.

```
_ _ _ _ _ _ _ _ _
Guesses remaining: 10
Already guessed:
Guess a letter: a
2 a's found

_ a _ _ _ _ a _ _
Guesses remaining: 10
Already guessed: a
Guess a letter: a
You've already guessed that
```

## Part 3

Allow the user to user to guess the whole word- if they enter more than one letter check if the string entered matches the secret word, and if so, they win!

## Part 4

We can use the following ASCII art (inspired by this [code golf](https://codegolf.stackexchange.com/questions/49671/do-you-want-to-code-a-snowman)) to show the user how many wrong guesses they've made. Hint: use the number of incorrect guesses as an index into this list.

```python
snowman_pics = [r'''



 (   )
''', r'''


 (   )
 (   )
''', r'''

 (   )
 (   )
 (   )
''', r'''

 (   )
 (   )
 ( : )
''', r'''

 (   )
 ( : )
 ( : )
''', r'''

 ( . )
 ( : )
 ( : )
''', r'''
 _===_
 ( . )
 ( : )
 ( : )
''', r'''
 _===_
 ( .O)
 ( : )
 ( : )
''',r'''
 _===_
 (-.O)
 ( : )
 ( : )
''', r'''
 _===_
 (-.O)
<( : )
 ( : )
''', r'''
 _===_
 (-.O)
<( : )\
 ( : )
''']
```

