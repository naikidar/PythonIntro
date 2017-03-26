import turtle

def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.speed(0)
 #   draw_square(brad,100,90,"green")
    
    for i in range(1,37):
        draw_square(brad,100,90,"green")
        draw_square(brad,50,90,"blue")
        draw_cirlce(brad,"cyan",25)
        draw_cirlce(brad,"pink",50)
        brad.right(10)

    brad.right(90)
    brad.forward(200)

    for i in range(1,11):
        draw_cirlce(brad,"dark green",i*5)
        draw_cirlce(brad,"dark green",-i*5)

            
    window.exitonclick()
    

def draw_square(someturtle,f,r,c):
    someturtle.color(c)
    for i in range(1,5):
        someturtle.forward(f)
        someturtle.right(r)

def draw_cirlce(someturtle,c,s):
    someturtle.color(c)
    someturtle.circle(s)


draw_art()
    
