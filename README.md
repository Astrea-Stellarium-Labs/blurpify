# blurpify
A remake of a program that "blurpifies" images by converting them to shades of (old) blurple.

## Installation

**Python 3.8+ is required.** It's possible to make a fork that supports a Python version lower than that, but I won't support it.

I'll eventually add this to PyPI, but for now, you can install it via:
```sh
pip install -U git+https://github.com/Sonic4999/blurpify.git
```

## How to Use
If you wish to use it as a standard library, here's an example of how to do so:
```python
import blurpify

input_file = "C:/path/to/your/input.jpg"
output_file = "C:/path/to/your/output.jpg"

blurpify.convert(input_file, output_file)
```

If you wish to use it from the command line, open up your favorite command prompt and use:
```sh
blurpify C:/path/to/your/input.jpg
```

If you wish to make the output file a seperate file, use:
```sh
blurpify C:/path/to/your/input.jpg C:/path/to/your/output.jpg
```

## TODO
- Add support for animated GIFs

## Original version
The original version has been taken down, but you can find an archive of it
[here](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/memethyl/blurpify).

## Possibly Asked Questions:
> Didn't you just make another program that blurplifies images?

Yes, [here](https://github.com/Sonic4999/blurplefier-standalone), but that *blurplifies* images, not *blurpifies* them.
Plus, these two do two entirely different things, even if they achieve similar goals.
And this is a remake of an old program, the other one is a modification of an existing and still supported one.

> Why not merge this with that other program then?

Would be too hard, or at least too... for the lack of better words, awkward.
The other program isn't meant to use a method that is entirely different from the methods already built-in.
I figured this was easier to do than to try to make it work.

> The original version's repo was deleted, right? Is it a good idea to do this?

Who knows. Hopefully it is. I like the results of this too much, anywho.

> This isn't even like the original version! The colors are slightly different!

That's not a question. Regardless, yeah, it isn't. The original project used a different method of grayscaling that's hard to replicate in Python, so I didn't bother, instead just using Pillow's default grayscaling (which works fine for most people). By default, the program attempts to do some slight brightness and contrast adjustments to get things closer to the original version, but it's not perfect, and you can disable this if you want. I don't intend to fix this 'problem' regardless.

> Why make this?

`blurplefier-standalone` wasn't a great help with [my Blurplefied Resource Pack for Minecraft](https://github.com/Sonic4999/Blurplefied-Resource-Pack), as it made images that were completely different from what I wanted.
This is much closer to the program I used to make those packs (this being a remake of that program), and so should be closer to how I need it.
