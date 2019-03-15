# BrailleCodec
A 8-braille encoder and decoder.


### What is Braille:
Braille is a reading and writing language for the blind and visually impaired, that consist of 6 or 8 dots in a 2 column cell named the braille cell.
todo: inset image of 6 and 8 dots braille cells here.

Braille cells dot are gived the numbers from 1 to 8.


### How does this encoder and decoder work
This encoder / decoder works by mapping each character to an 8 numbered pin number, each number representing a dot on the braille cell. The number consist, like binary code, by ones and zeros. "1" represent a raised dot on the braille cell and "0" represent a dot that's lowered / not raised.

#### An example
The letter "a" is written in braille by having dot 1 raised and all other dots lowered.
In this BrailleCodec, the letter "a" is represented by the pin "10000000".
Another example is the uppercase "A" is basicly the same as above but with dot 7 raised "10000010".

### Code example:
This example is written in python 3.

```python
import braillecodec
start = "Hello World 123" # note the uppercase letters.
braillecodec.encode(start)
'110010101000100011100000111000001010100000000000010111101010100011101000111000001001100000000000100000011100000110010001'
 
braillecodec.decode("110010101000100011100000111000001010100000000000010111101010100011101000111000001001100000000000100000011100000110010001")
"Hello World 123"
```

Look in the example.py file for a bigger example.


### installation
To install put the braillecodec file for your selected language in your project structure and import it live above.

### Contributing
Everybody is free to open issues and submit pull requests to improve this codec or add support in other languages.

### License
Copyright (C) [Nicklas Tegner - @NicklasMCHD](https://twitter.com/NicklasMCHD).
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, version 3 of the License.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.
