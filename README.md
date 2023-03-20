# Colored-Alphabet
An alphabet that is based solely on colors and not shapes of letters

<img src="https://github.com/hollowness-inside/Colored-Alphabet/blob/main/readme.png" width="100" height="100">
*The same text but in the Colored alphabet*

***

It wouldn't be an alphabet without a table designated for it
![alphabet](https://github.com/hollowness-inside/Colored-Alphabet/blob/main/alphabet.png)

Here's how it works:

A letter can be encoded with at most two colors. The first color is called `modifier` and the second, `stem`.

The `modifier` colors are in the left column of the table. 
They are usually darker.
Notice, there's no color for the second row of the table, meaning that the letters in that row are 
encoded with only one color, `stem`.

The `stem` colors are in the first row of the table.
***

# [Converter](https://github.com/hollowness-inside/Colored-Alphabet/tree/main/converter)
Use this to convert the Latin alphabet into the Colored alphabet.
The converter is a CLI tool

```
Usage: python3 main.py (-f FILE_NAME) (-t SOME_TEXT) [-l] -o OUTPUT.png
  -l  Draw colors in one row
```
