---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Go
---

What are some characteristics of the Go programming language?  
* Strong and static typing - the type of the variables can't be changed over time and they have to be defined at compile time
* Simplicity
* Fast compile times
* Built-in concurrency
* Garbage collected
* Platform independent
* Compile to standalone binary - anything you need to run your app will be compiled into one binary. Very useful for version management in run-time.  
Go also has good community.
  

What is the difference between var x int = 2 and x := 2?  
The result is the same, a variable with the value 2.  
With var x int = 2 we are setting the variable type to integer while with x := 2 we are letting Go figure out by itself the type.
  

True or False? In Go we can redeclare variables and once declared we must use it.  
False. We can't redeclare variables but yes, we must used declared variables.
  

What libraries of Go have you used?  
This should be answered based on your usage but some examples are:  
* fmt - formatted I/O
  

What is the problem with the following block of code? How to fix it?  
```
func main() {
var x float32 = 13.5
var y int
y = x
}
```

  

The following block of code tries to convert the integer 101 to a string but instead we get "e". Why is that? How to fix it?  
```go
package main

import "fmt"

func main() {
var x int = 101
var y string
y = string(x)
fmt.Println(y)
}
```
  
It looks what unicode value is set at 101 and uses it for converting the integer to a string.
If you want to get "101" you should use the package "strconv" and replace y = string(x) with y = strconv.Itoa(x)
  

What is wrong with the following code?:  
```
package main

func main() {
var x = 2
var y = 3
const someConst = x + y
}
```
  
Constants in Go can only be declared using constant expressions.
But `x`, `y` and their sum is variable.

const initializer x + y is not a constant
  

What will be the output of the following block of code?:  
```go
package main

import "fmt"

const (
x = iota
y = iota
)
const z = iota

func main() {
fmt.Printf("%v\n", x)
fmt.Printf("%v\n", y)
fmt.Printf("%v\n", z)
}
```
  
Go's iota identifier is used in const declarations to simplify definitions of incrementing numbers. Because it can be used in expressions, it provides a generality beyond that of simple enumerations.

`x` and `y` in the first iota group, `z` in the second.

Iota page in Go Wiki
  

What _ is used for in Go?  
It avoids having to declare all the variables for the returns values.
It is called the blank identifier.

answer in SO
  

What will be the output of the following block of code?:  
```go
package main

import "fmt"

const (
_ = iota + 3
x
)

func main() {
fmt.Printf("%v\n", x)
}
```
  
Since the first iota is declared with the value `3` (` + 3`), the next one has the value `4`
  

What will be the output of the following block of code?:  
```go
package main

import (
"fmt"
"sync"
"time"
)

func main() {
var wg sync.WaitGroup

wg.Add(1)
go func() {
time.Sleep(time.Second * 2)
fmt.Println("1")
wg.Done()
}()

go func() {
fmt.Println("2")
}()

wg.Wait()
fmt.Println("3")
}
```
  
Output: 2 1 3  
Aritcle about sync/waitgroup  
Golang package sync
  

What will be the output of the following block of code?:  
```go
package main

import (
"fmt"
)

func mod1(a []int) {
for i := range a {
a[i] = 5
}

fmt.Println("1:", a)
}

func mod2(a []int) {
a = append(a, 125) // !

for i := range a {
a[i] = 5
}

fmt.Println("2:", a)
}

func main() {
s1 := []int{1, 2, 3, 4}
mod1(s1)
fmt.Println("1:", s1)

s2 := []int{1, 2, 3, 4}
mod2(s2)
fmt.Println("2:", s2)
}
```
  
Output: 
1 [5 5 5 5]
1 [5 5 5 5]
2 [5 5 5 5 5]
2 [1 2 3 4]
  
In `mod1` a is link, and when we're using `a[i]`, we're changing `s1` value to.
But in `mod2`, `append` creates new slice, and we're changing only `a` value, not `s2`.  
Aritcle about arrays,
Blog post about `append`
  

What will be the output of the following block of code?:  
```go
package main

import (
"container/heap"
"fmt"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i]   
Output: 3  
Golang container/heap package
