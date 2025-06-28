---
repo: Textualize/rich
readme_filename: Textualize_rich_README.md
stars: 52598
forks: 1849
watchers: 52598
contributors_count: 260
license: MIT
Header 2: Using the Console
---
For more control over rich terminal content, import and construct a Console object.  
```python
from rich.console import Console

console = Console()
```  
The Console object has a `print` method which has an intentionally similar interface to the builtin `print` function. Here's an example of use:  
```python
console.print("Hello", "World!")
```  
As you might expect, this will print `"Hello World!"` to the terminal. Note that unlike the builtin `print` function, Rich will word-wrap your text to fit within the terminal width.  
There are a few ways of adding color and style to your output. You can set a style for the entire output by adding a `style` keyword argument. Here's an example:  
```python
console.print("Hello", "World!", style="bold red")
```  
The output will be something like the following:  
!Hello World  
That's fine for styling a line of text at a time. For more finely grained styling, Rich renders a special markup which is similar in syntax to bbcode. Here's an example:  
```python
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
```  
!Console Markup  
You can use a Console object to generate sophisticated output with minimal effort. See the Console API docs for details.