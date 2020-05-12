# Vinícius Brito Bastos Antunes: COMP-22

import random
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

# Exercício 1

def change_R( ):
    tess.color("red")

def change_G( ):
    tess.color("green")
    
def change_B( ):
    tess.color("blue")

def change_s( ):
    t = tess.pensize( )
    if t>1:
        tess.pensize(t-1)
    
def change_S( ):
    t = tess.pensize( )
    if t<20:
        tess.pensize(t+1)

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    # Exercício 2
    wn.ontimer(advance_state_machine, 3000)
        
# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.onkey(change_R, "r")
wn.onkey(change_G, "g")
wn.onkey(change_B, "b")
wn.onkey(change_s, '-')
wn.onkey(change_S, '+')
wn.ontimer(advance_state_machine, 3000)
wn.listen() # Listen for events
wn.mainloop()

# Exercício 3

def cleanword(x):
    import re
    r = re.sub(r'[^a-zA-Z]', "", x)
    return r

def extract_words(x):
    import re
    y = re.split(r'[\s-]+', x)
    s = len(y)
    for i in range(0, s):
        y[i]=cleanword(y[i])
        y[i]=y[i].lower()
    return y

def test(x):
    if x:
        print("Accepted")
    else:
        print("Rejected")

def has_dashdash(x):
    return x.find("--")!=-1

def longestword(x):
    r = 0
    for y in x:
        r = max(r, len(y))
    return r

def wordcount(x, y):
    return y.count(x)

def wordset(x):
    s = {x[0]}
    for y in x:
        s.add(y)
    S = list(s)
    S.sort( )
    return S

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")
test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))
test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])
test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)
test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])
test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)

# Exercício 4

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False    

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

"""
The greatest N such that
the solution lasts within one
minute is 12.
"""

def board_solve(N):
    rng = random.Random()   # Instantiate a generator
    bd = list(range(N))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Exercício 5
    
    def reflect_x(self):
        return Point(self.x, -self.y)
    
    # Exercício 6
    """
    The following method fails if
    the point is on the y axis.
    """
    def slope_from_origin(self):
        return self.y/self.x
    
    # Exercício 7
    
    def get_line_to(self, P):
        a = (P.y - self.y)/(P.x - self.x)
        b = P.y - a*P.x
        return (a, b)
    
# Exercício 8

"""
Following there are:
declare - a static method;
that's useful for specific and predefined operations
related to the class

pick_neutral - a class method;
that's interesting when dealing with
a class rather than an object

sqrt - an abstract method;
that's a good header to be implemented
inside the class' heirs, adapted to
the utility of each of them

"""

class Number:
    
    def __init__(self, v):
        self.value=v
    
    def declare( ):
        print("I'm a number!")
    
    def pick_neutral(cls):
        return cls(0)
    
    def sqrt(self):

# Exercício 9

"""
The following code
shows how MRO goes along heritage
"""

class Shape:
    geometric_type = 'Generic Shape'
    
    def area(self):
        raise NotImplementedError
    
    def get_geometric_type(self):
        return self.geometric_type
    
    def execute(self):
        print("Farewell, world!")

class Plotter:
    
    def execute(self):
        print("Hello, world!")
    
    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

"""
It goes from left to right, if there's no struggle
Output: Farewell, world!
"""

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

pol = Polygon()
pol.execute()

class Plotter(Shape):
    
    def execute(self):
        print("Hello, world!")
    
    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

"""
Otherwise, an error is thrown on the screen
Output: TypeError: Cannot create a consistent method resolution
order (MRO) for bases Shape, Plotter
"""

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

pol = Polygon()
pol.execute()
        
# Exercício 10

def ad(b):
    def wrapper( ):
        print("Todo mundo gosta muito de", b( ))
    return wrapper

@ad
def copy( ):
    r = input( )
    return r

# Exercício 11

def first_on_line(*queue):
    print(queue[0])

def total_cost(**budget):
    s = 0
    for key, value in budget.items():
        s+=value
    print('Total production cost =', s)

first_on_line("Armando", "Karla", "Yano")
total_cost(director=200, janitor=50, screenplay=350, actors=280)

# Exercício 12

class Operator:
    
    def soma(self, x, y):
        return x+y

class Soma(Operator):
    
    def soma(self, x, y):
        return x**2+y**2

op1 = Soma()
op2 = Operator()
op = [op1, op2]

"""
One can demand soma regardless
if the object is of Soma type or
Operator type, and the used function
will be the type's own.
"""

for y in op:
    print(y.soma(2, 3))

"""
Also note that print calls a
function soma from an object y,
and there's no worry about y's
type. It simply calls a function soma,
and checks if the object has such
method. That's Python's Duck Typing! 
"""