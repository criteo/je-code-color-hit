from kivy.lang import Builder


# Building the root and objects
Builder.load_string('''
<Root>:
    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            size: self.size
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.width / 2 - (self.width / 80 + self.height / 80)/2, self.height / 5 - (self.width / 80 + self.height / 80)/2
            size: (self.width / 80 + self.height / 80) , (self.width + self.height) / 500
        Rectangle:
            pos: self.width / 5, self.height / 20
            size: 3 * self.width / 5, (self.width + self.height) / 500
<AnimBall>:
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size
            source: '../images/cat_ball.jpg'
''')
