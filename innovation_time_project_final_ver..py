## CSC 1980/2280 joint final project by Samuel Lewis
## Project contains the code for a completely running 2 player turtle based
## chess game.

### Import statements:
import turtle
import random

### Creating start screen turtles:
start_screen_title = turtle.Turtle()
start_screen_image = turtle.Turtle()
start_screen_start_text = turtle.Turtle()
enter_control_screen_text = turtle.Turtle()

### Creating controls screen turtles:
control_screen_title = turtle.Turtle()
control_screen_text = turtle.Turtle()

### Creating turtles to draw the chess board:
board = turtle.Turtle()
writer = turtle.Turtle()
board_screen_title = turtle.Turtle()

### Creating chess piece turtles:

# White pawns:
white_pawn_1 = turtle.Turtle()
white_pawn_2 = turtle.Turtle()
white_pawn_3 = turtle.Turtle()
white_pawn_4 = turtle.Turtle()
white_pawn_5 = turtle.Turtle()
white_pawn_6 = turtle.Turtle()
white_pawn_7 = turtle.Turtle()
white_pawn_8 = turtle.Turtle()

# white rooks:
white_rook_1 = turtle.Turtle()
white_rook_2 = turtle.Turtle()

# White knights:
white_knight_1 = turtle.Turtle()
white_knight_2 = turtle.Turtle()

# White bishops:
white_bishop_1 = turtle.Turtle()
white_bishop_2 = turtle.Turtle()

# White queen:
white_queen = turtle.Turtle()

# White king:
white_king = turtle.Turtle()

# Black pawns:
black_pawn_1 = turtle.Turtle()
black_pawn_2 = turtle.Turtle()
black_pawn_3 = turtle.Turtle()
black_pawn_4 = turtle.Turtle()
black_pawn_5 = turtle.Turtle()
black_pawn_6 = turtle.Turtle()
black_pawn_7 = turtle.Turtle()
black_pawn_8 = turtle.Turtle()

# Black rooks:
black_rook_1 = turtle.Turtle()
black_rook_2 = turtle.Turtle()

# Black knights:
black_knight_1 = turtle.Turtle()
black_knight_2 = turtle.Turtle()

# Black bishops:
black_bishop_1 = turtle.Turtle()
black_bishop_2 = turtle.Turtle()

# Black queen:
black_queen = turtle.Turtle()

# Black king:
black_king = turtle.Turtle()

### Creating the RulesAndControls class:
class RulesAndControls(object):
    '''models the RulesAndControls object. Attributes. name, text'''
    def __init__(self,text):
        '''takes the attributes and returns the appropriate Rules object'''
        self.text = text
    def __str__(self):
        '''returns a string version of Rules'''
        string = str(self.text)
        return string

### Creating the RulesAndControls objects:
control_0 = RulesAndControls('Pieces are indexed from left to right')
control_1 = RulesAndControls('Ex: white_pawn_1 would be the white pawn furthest to the left')
control_2 = RulesAndControls('To move a piece, call the "move" function in the IDLE OR, click and drag on screen')
control_3 = RulesAndControls('Ex: move(black_pawn_4,d5), or move(white_knight_1,f6')
control_4 = RulesAndControls('Taking a piece is handled similarly calling the "take" function in IDLE')
control_5 = RulesAndControls('Ex: take(white_queen), or take(black_pawn_2)')
control_6 = RulesAndControls('To check the status of a piece, type "piece_status(piece_name)" into IDLE')
control_7 = RulesAndControls('Ex: piece_status(white_pawn_1)')
control_8 = RulesAndControls('To reset the board for another game, call the reset function in the IDLE')
control_9 = RulesAndControls('Ex: reset_board()')
control_10 = RulesAndControls('To proceed to the chess game, type onward! into the IDLE prompt')


### Turtle attributes:
turtle.register_shape('title_screen_chess_knight.gif') # registers start_screen_image's shape to the start screen image .gif file
board.speed(0) # sets the board's speed to 'fastest'

### Registering chess piece shapes:
turtle.register_shape('BB.gif')
turtle.register_shape('BK.gif')
turtle.register_shape('BKn.gif')
turtle.register_shape('BP.gif')
turtle.register_shape('BQ.gif')
turtle.register_shape('BR.gif')
turtle.register_shape('WB.gif')
turtle.register_shape('WK.gif')
turtle.register_shape('WKn.gif')
turtle.register_shape('WP.gif')
turtle.register_shape('WQ.gif')
turtle.register_shape('WR.gif')

### Creating screen:
screen = turtle.Screen()
screen.bgcolor('#8a785d')

### Creating styles for the on screen text:
start_screen_title_style = ('Times New Roman', 40, 'italic')
start_screen_start_text_style = ('Times New Roman', 20, 'italic')
enter_control_screen_text_style = ('Times New Roman', 20, 'italic')
coordinate_indicator_text_style = ('Times New Roman', 11, 'bold','italic')
board_screen_title_style = ('Times New Roman', 20, 'italic')
control_screen_title_style = ('Times New Roman', 40, 'italic')
control_screen_text_style = ('Times New Roman', 16, 'bold')
control_screen_subtext_style = ('Times New Roman', 12, 'italic')

### Creating lists:
coordinate_indicator_list = [] # list to hold the coordinates for the coordinate indicators on the side of the chess board
writer_list = [] # list to hold the strings that will be written at the coordinates of coordinate_indicator_list
coordinate_list = [] # list to hold the coordinates for the chess piece status method
### Assigning coordinate indicator positons to variables:
a = -195,-225
b = -145,-225
c = -95,-225
d = -45,-225
e = 5,-225
f = 55,-225
g = 105,-225
h = 155,-225
num_1 = -225, -195
num_2 = -225,-145
num_3 = -225, -95
num_4 = -225,-45
num_5 = -225, 5
num_6 = -225, 55
num_7 = -225,105
num_8 = -225, 155

### Function to draw the coordinate indicators:
### Assigning coordinate values to squares on a chess board:
a1 = (-175,-175)# White rook 1 starting pos
a2 = (-175,-125)# White pawn 1 starting pos
a3 = (-175,-75)
a4 = (-175,-25)
a5 = (-175,25)
a6 = (-175,75)
a7 = (-175,125)# Black pawn 1 starting pos
a8 = (-175,175)# Black rook 1 starting pos
b1 = (-125,-175)# White knight 1 starting pos
b2 = (-125,-125)# White pawn 2 starting pos
b3 = (-125,-75)
b4 = (-125,-25)
b5 = (-125,25)
b6 = (-125,75)
b7 = (-125,125)# Black pawn 2 starting pos
b8 = (-125,175)# Black knight 1 starting pos
c1 = (-75,-175)# White bishop 1 starting pos
c2 = (-75,-125)# White pawn 3 starting pos
c3 = (-75,-75)
c4 = (-75,-25)
c5 = (-75,25)
c6 = (-75,75)
c7 = (-75,125)# Black pawn 3 starting pos
c8 = (-75,175)# Black bishop 1 starting pos
d1 = (-25,-175)# White queen starting pos
d2 = (-25,-125)# White pawn 4 starting pos
d3 = (-25,-75)
d4 = (-25,-25)
d5 = (-25,25)
d6 = (-25,75)
d7 = (-25,125)# Black pawn 4 starting pos
d8 = (-25,175)# Black queen starting pos
e1 = (25,-175)# White king starting pos
e2 = (25,-125)# White pawn 5 starting pos
e3 = (25,-75)
e4 = (25,-25)
e5 = (25,25)
e6 = (25,75)
e7 = (25,125)# Black pawn 5 starting pos
e8 = (25,175)# Black king 1 starting pos
f1 = (75,-175)# White bishop 2 starting pos
f2 = (75,-125)# White pawn 6 starting pos
f3 = (75,-75)
f4 = (75,-25)
f5 = (75,25)
f6 = (75,75)
f7 = (75,125)# Black pawn 6 starting pos
f8 = (75,175)# Black bishop 2 starting pos
g1 = (125,-175)# White knight 2 starting pos
g2 = (125,-125)# White pawn 7 starting pos
g3 = (125,-75)
g4 = (125,-25)
g5 = (125,25)
g6 = (125,75)
g7 = (125,125)# Black pawn 7 starting pos
g8 = (125,175)# Black knight 2 starting pos
h1 = (175,-175)# White rook 2 starting pos
h2 = (175,-125)# White pawn 8 starting pos
h3 = (175,-75)
h4 = (175,-25)
h5 = (175,25)
h6 = (175,75)
h7 = (175,125)# Black pawn 8 starting pos
h8 = (175,175)# Black rook 2 starting pos

### Adding coordinate variables to a list:
coordinate_indicator_list.extend((a,b,c,d,e,f,g,h,num_1,num_2,num_3,num_4,num_5,
                                  num_6,num_7,num_8))
writer_list.extend(('a','b','c','d','e','f','g','h','1','2','3','4','5','6','7',
                    '8'))
coordinate_list.extend((a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,
                        c3,c4,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,e1,e2,e3,e4,
                        e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,
                        g7,g8,h1,h2,h3,h4,h5,h6,h7,h8))
### Drawing the start screen:
def draw_start_screen():
    '''creates the elements that make up the welcome/start screen'''
    # Setting the bg color for when the back to start function is called
    screen.bgcolor('#8a785d')
    # Start screen text
    start_screen_title.hideturtle()
    start_screen_title.penup()
    start_screen_title.goto(0,225)
    start_screen_title.write('Welcome to Turtle Chess!', align = 'center',
                            font = start_screen_title_style)

    # Start screen image
    start_screen_image.shape('title_screen_chess_knight.gif')

    # Start screen start game text
    start_screen_start_text.hideturtle()
    start_screen_start_text.penup()
    start_screen_start_text.goto(0,-225)
    start_screen_start_text.write('To begin the game, type "start" into the IDLE',
                                     align = 'center', font =
                                     (start_screen_start_text_style))

    # Start screen goto control screen message
    enter_control_screen_text.hideturtle()
    enter_control_screen_text.penup()
    enter_control_screen_text.goto(0,-250)
    enter_control_screen_text.write('To enter the controls screen, type "controls"'
                                       ' into the IDLE', align = 'center', font =
                                       (enter_control_screen_text_style))
    return

### Drawing the controls screen:
def draw_controls_screen():
    '''creates the elements that make up the controls screen'''
    control_screen_title.hideturtle()
    control_screen_title.penup()
    control_screen_title.goto(0,225)
    control_screen_title.write('Turtle Chess Controls', align = 'center',
                            font = start_screen_title_style)
    print(control_0)
    print()
    control_screen_text.goto(0,175)
    control_screen_text.write('Pieces are indexed from left to right', align
                              = 'center', font = (control_screen_text_style))
    print(control_1)
    print()
    control_screen_text.goto(0,150)
    control_screen_text.write('Ex: white_pawn_1 would be the white pawn furthest to the left',
                              align = 'center', font = (control_screen_subtext_style))
    print(control_2)
    print()
    control_screen_text.goto(0,100)
    control_screen_text.write('To move a piece, call the "move" function in the IDLE OR, click and drag on screen',
                              align = 'center', font = (control_screen_text_style))
    print(control_3)
    print()
    control_screen_text.goto(0,75)
    control_screen_text.write('Ex: move(black_pawn_4,d5), or move(white_knight_1,f6', align = 'center',
                              font = (control_screen_subtext_style))
    print(control_4)
    print()
    control_screen_text.goto(0,25)
    control_screen_text.write('Taking a piece is handled similarly calling the "take" function in IDLE',
                              align = 'center', font = (control_screen_text_style))
    print(control_5)
    print()
    control_screen_text.goto(0,0)
    control_screen_text.write('Ex: take(white_queen), or take(black_pawn_2)',
                              align = 'center', font = (control_screen_subtext_style))
    print(control_6)
    print()
    control_screen_text.goto(0,-50)
    control_screen_text.write('To check the status of a piece, type "piece_status(piece_name)" into IDLE',
                             align = 'center', font = (control_screen_text_style))
    print(control_7)
    print()
    control_screen_text.goto(0,-75)
    control_screen_text.write('Ex: piece_status(white_pawn_1)', align = 'center', font = (control_screen_subtext_style))
    print(control_8)
    print()
    control_screen_text.goto(0,-125)
    control_screen_text.write('To reset the board for another game, call the reset function in the IDLE',
                              align = 'center', font = (control_screen_text_style))
    print(control_9)
    print()
    control_screen_text.goto(0,-150)
    control_screen_text.write('Ex: reset_board()', align = 'center', font =
                              (control_screen_subtext_style))
    print(control_10)
    print()
    control_screen_text.goto(0,-200)
    control_screen_text.write('To proceed to the chess game, type onward! into the IDLE prompt',
                             align = 'center', font = (control_screen_text_style))
    
    
    ### function to go on to the game after viewing the controls screen:
def onward_to_chess_game():
    '''detects when the user wants to go on from the controls screen to the game screen and draws the screen for the user'''
    onward_to_game = input('Type "onward!" into the IDLE if you are done checking the controls:')

    if onward_to_game == 'onward!':
        screen.clear()# Clears the screen for a new screen to be drawn
        screen.bgcolor('#8a785d')# Resets the bg color after the screen clear
        draw_chess_board_screen()# Calls the draw_chess_board_screen function
        draw_coordinate_indicators(0)
        set_piece_starting_pos()

### Creating the chess game:
    
### Drawing the actual chess board:
def draw_box(t,x,y,size,fill_color):
    '''uses turtle to draw a box and fill in colors'''
    t.penup() 
    t.goto(x,y) 
    t.pendown()
 
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color
 
    for i in range(0,4):
        board.fd(size) 
        board.rt(90) 
 
    t.end_fill() # Fill the square

def draw_chess_board_screen():
    '''uses draw_box() to create a chess board'''
    square_color = "#573a2e" # First chess board square is dark brown
    start_x = -200 # Starting x position of the chess board
    start_y = -150 # Starting y position of the chess board
    box_size = 50 # Pixel size of each square in the chess board
    for i in range(0,8): # 8x8 chess board
        for j in range(0,8):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            square_color = '#573a2e' if square_color == '#fccc74' else '#fccc74' # toggle after a column
        square_color = '#573a2e' if square_color == '#fccc74' else '#fccc74' # toggle after a row

    ### Drawing the board screen title:
    board_screen_title.hideturtle()
    board_screen_title.penup()
    board_screen_title.lt(90)
    board_screen_title.fd(225)
    board_screen_title.write('Turtle Chess!', align = 'center',
                            font = board_screen_title_style)

### Function to draw coordinate indicators:
def draw_coordinate_indicators(i):
    '''draws the coordinate indicators along the sides of the chess board'''
    index = i
    max_index = 16
    if index == max_index:
        return
    else:
        writer.goto(coordinate_indicator_list[index])
        writer.write(writer_list[index],font = (coordinate_indicator_text_style))
        draw_coordinate_indicators(i+1)

### Function to set the initial piece position of the chess piece turtles:
def set_piece_starting_pos():
    '''sets the starting positions of all the chess pieces'''
    ### Setting chess pieces shapes:
    white_pawn_1.shape('WP.gif')
    white_pawn_2.shape('WP.gif')
    white_pawn_3.shape('WP.gif')
    white_pawn_4.shape('WP.gif')
    white_pawn_5.shape('WP.gif')
    white_pawn_6.shape('WP.gif')
    white_pawn_7.shape('WP.gif')
    white_pawn_8.shape('WP.gif')

    black_pawn_1.shape('BP.gif')
    black_pawn_2.shape('BP.gif')
    black_pawn_3.shape('BP.gif')
    black_pawn_4.shape('BP.gif')
    black_pawn_5.shape('BP.gif')
    black_pawn_6.shape('BP.gif')
    black_pawn_7.shape('BP.gif')
    black_pawn_8.shape('BP.gif')

    white_rook_1.shape('WR.gif')
    white_rook_2.shape('WR.gif')

    black_rook_1.shape('BR.gif')
    black_rook_2.shape('BR.gif')

    white_knight_1.shape('WKn.gif')
    white_knight_2.shape('WKn.gif')

    black_knight_1.shape('BKn.gif')
    black_knight_2.shape('BKn.gif')

    white_bishop_1.shape('WB.gif')
    white_bishop_2.shape('WB.gif')

    black_bishop_1.shape('BB.gif')
    black_bishop_2.shape('BB.gif')

    white_queen.shape('WQ.gif')

    black_queen.shape('BQ.gif')

    white_king.shape('WK.gif')

    black_king.shape('BK.gif')
    
    # Making the pieces visible:
    white_pawn_1.showturtle()
    white_pawn_2.showturtle()
    white_pawn_3.showturtle()
    white_pawn_4.showturtle()
    white_pawn_5.showturtle()
    white_pawn_6.showturtle()
    white_pawn_7.showturtle()
    white_pawn_8.showturtle()

    black_pawn_1.showturtle()
    black_pawn_2.showturtle()
    black_pawn_3.showturtle()
    black_pawn_4.showturtle()
    black_pawn_5.showturtle()
    black_pawn_6.showturtle()
    black_pawn_7.showturtle()
    black_pawn_8.showturtle()

    white_rook_1.showturtle()
    white_rook_2.showturtle()

    black_rook_1.showturtle()
    black_rook_2.showturtle()

    white_knight_1.showturtle()
    white_knight_2.showturtle()

    black_knight_1.showturtle()
    black_knight_2.showturtle()

    white_bishop_1.showturtle()
    white_bishop_2.showturtle()

    black_bishop_1.showturtle()
    black_bishop_2.showturtle()

    white_queen.showturtle()

    black_queen.showturtle()

    white_king.showturtle()

    black_king.showturtle()
    
    # Setting penup:
    white_pawn_1.penup()
    white_pawn_2.penup()
    white_pawn_3.penup()
    white_pawn_4.penup()
    white_pawn_5.penup()
    white_pawn_6.penup()
    white_pawn_7.penup()
    white_pawn_8.penup()

    black_pawn_1.penup()
    black_pawn_2.penup()
    black_pawn_3.penup()
    black_pawn_4.penup()
    black_pawn_5.penup()
    black_pawn_6.penup()
    black_pawn_7.penup()
    black_pawn_8.penup()

    white_rook_1.penup()
    white_rook_2.penup()

    black_rook_1.penup()
    black_rook_2.penup()

    white_knight_1.penup()
    white_knight_2.penup()

    black_knight_1.penup()
    black_knight_2.penup()

    white_bishop_1.penup()
    white_bishop_2.penup()

    black_bishop_1.penup()
    black_bishop_2.penup()

    white_queen.penup()

    black_queen.penup()

    white_king.penup()

    black_king.penup()

    # White pawns:
    white_pawn_1.goto(a2)
    white_pawn_2.goto(b2)
    white_pawn_3.goto(c2)
    white_pawn_4.goto(d2)
    white_pawn_5.goto(e2)
    white_pawn_6.goto(f2)
    white_pawn_7.goto(g2)
    white_pawn_8.goto(h2)

    # Blacks pawns:
    black_pawn_1.goto(a7)
    black_pawn_2.goto(b7)
    black_pawn_3.goto(c7)
    black_pawn_4.goto(d7)
    black_pawn_5.goto(e7)
    black_pawn_6.goto(f7)
    black_pawn_7.goto(g7)
    black_pawn_8.goto(h7)

    # White rooks:
    white_rook_1.goto(a1)
    white_rook_2.goto(h1)

    # Black rooks:
    black_rook_1.goto(a8)
    black_rook_2.goto(h8)

    # White knights:
    white_knight_1.goto(b1)
    white_knight_2.goto(g1)

    # Black knights:
    black_knight_1.goto(b8)
    black_knight_2.goto(g8)

    # White bishops:
    white_bishop_1.goto(c1)
    white_bishop_2.goto(f1)

    # Black bishops:
    black_bishop_1.goto(c8)
    black_bishop_2.goto(f8)

    # White queen:
    white_queen.goto(d1)

    # Black queen:
    black_queen.goto(d8)

    # White king:
    white_king.goto(e1)

    # Black king:
    black_king.goto(e8)

### Function to handle which player plays as the white pieces:
def coin_flip_for_who_plays_white():
    '''tosses a coin for which player plays as the white pieces'''
    string_to_manipulate = 'Player who called will play as the white pieces. Player who called will play as the black pieces.'
    print("Select a player to call the coin toss.")
    user_selection = input("heads or tails:")
    coin = ["heads","tails"]
    toss = random.choice(coin)
    print(toss)
    if user_selection == toss:
        print(string_to_manipulate[0:47])
    else:
        print(string_to_manipulate[49:-1])
        print("remember, the white pieces always move first")

### Changing screens based on user input:
def change_screens():
    '''based on the users input clears the screen and draws the new screen
       desired by the user'''
    
    print('Please enter "start" or "controls" to begin')
    user_selection = input('start or controls:')
    if user_selection == "start":
        screen.clear()# Clears the screen for a new screen to be drawn
        screen.bgcolor('#8a785d')# Resets the bg color after the screen clear
        draw_chess_board_screen()# Calls the draw_chess_board_screen function
        draw_coordinate_indicators(0)
        set_piece_starting_pos()
        coin_flip_for_who_plays_white()

    elif user_selection == "controls":
       screen.clear()# Clears the screen for a new screen to be drawn
       screen.bgcolor('#8a785d')# Resets the bg color after the screen clear
       ## Call the draw control screen funtion here
       draw_controls_screen()
       onward_to_chess_game()
    else:
        print('User input not valid, please enter a valid input')

### Function calls:
draw_start_screen()
change_screens()

### Chess controls:

def move(turtle,coordinate):
    '''handles the movement of the chess pieces'''
    turtle.goto(coordinate)

def take(turtle):
    '''handles the taking of a piece during the chess game'''
    if turtle == white_king or turtle == black_king:
        turtle.hideturtle()
        print("YOU WIN! type reset_board() in the IDLE to play again")
    turtle.hideturtle()

def reset_board():
    '''resets the board for another fabulous game of turtle chess!'''
    set_piece_starting_pos()

def is_visible(turtle):
    '''checks if a turtle is visible'''
    turtle.isvisible()

def piece_status(turtle):
    '''checks the status of a turtle and detects if it has been taken/shows its position if not'''
    is_visible(turtle)
    if is_visible(turtle) == False:
        print("Piece has been taken and is no longer in play")
    else:
        print("piece is still in play")
        for i in range(50):
            turtle.hideturtle()
            turtle.showturtle()
            

### Allowing chess pieces to be moved by a click and drag:
white_pawn_1.ondrag(white_pawn_1.goto)
white_pawn_2.ondrag(white_pawn_2.goto)
white_pawn_3.ondrag(white_pawn_3.goto)
white_pawn_4.ondrag(white_pawn_4.goto)
white_pawn_5.ondrag(white_pawn_5.goto)
white_pawn_6.ondrag(white_pawn_6.goto)
white_pawn_7.ondrag(white_pawn_7.goto)
white_pawn_8.ondrag(white_pawn_8.goto)

black_pawn_1.ondrag(black_pawn_1.goto)
black_pawn_2.ondrag(black_pawn_2.goto)
black_pawn_3.ondrag(black_pawn_3.goto)
black_pawn_4.ondrag(black_pawn_4.goto)
black_pawn_5.ondrag(black_pawn_5.goto)
black_pawn_6.ondrag(black_pawn_6.goto)
black_pawn_7.ondrag(black_pawn_7.goto)
black_pawn_8.ondrag(black_pawn_8.goto)

white_rook_1.ondrag(white_rook_1.goto)
white_rook_2.ondrag(white_rook_2.goto)

black_rook_1.ondrag(black_rook_1.goto)
black_rook_2.ondrag(black_rook_2.goto)

white_knight_1.ondrag(white_knight_1.goto)
white_knight_2.ondrag(white_knight_2.goto)

black_knight_1.ondrag(black_knight_1.goto)
black_knight_2.ondrag(black_knight_2.goto)

white_bishop_1.ondrag(white_bishop_1.goto)
white_bishop_2.ondrag(white_bishop_2.goto)

black_bishop_1.ondrag(black_bishop_1.goto)
black_bishop_2.ondrag(black_bishop_2.goto)

white_queen.ondrag(white_queen.goto)

black_queen.ondrag(black_queen.goto)

white_king.ondrag(white_king.goto)

black_king.ondrag(black_king.goto)
