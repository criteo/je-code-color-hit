from kivy.lang import Builder


# Building the root and objects
Builder.load_string('''
<Root>:
    canvas:
        Rectangle:
            size: self.size
            source: '../images/cat1.jpg'
        Rectangle:
            pos: self.width / 2 - (self.width / 80 + self.height / 80)/2, self.height / 5 - (self.width / 80 + self.height / 80)/2
            size: (self.width / 80 + self.height / 80) , (self.width + self.height) / 500
        Rectangle:
            pos: self.width / 5, self.height / 20
            size: 3 * self.width / 5, (self.width + self.height) / 500
    Label:
        font_size: self.width / 5
        pos: 3 * root.width / 4 - self.width / 2, root.center_y /80 - self.height/3 
        text:"Score: " +  str(root.score)   
    Label:
        font_size: self.width / 5
        pos: root.width / 2 - self.width / 2, root.center_y/80 - self.height/3 
        text: "Attempt: " + str(root.attempt)
    Label:
        font_size: self.width / 5
        pos:  root.width / 4 - self.width / 2, root.center_y/80 - self.height/3 
        text: "Max score " + str(root.max_score)
<ClockRect>:
    size: self.s, self.s
    canvas:
        Color:
            rgba: self.r, self.g, self.b, 1
        Line:
            width: 2.
            rectangle: (self.x, self.y, self.width, self.height)
<AnimBall>:
    canvas:
        Color:
            rgba: self.r, self.g, self.b, 1
        Ellipse:
            pos: self.pos
            size: self.size
            source: '../images/cat_ball.jpg'
''')
