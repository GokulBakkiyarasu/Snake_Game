from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.position = 2
        self.move_distance = [10, 15, 20]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def append_segment(self):
        self.position += 1
        self.add_segment(position=(self.position, 0))

    def move_easy(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.move_distance[0])

    def move_medium(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.move_distance[1])

    def move_hard(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.move_distance[2])

    def up(self):
        if not self.head.heading() == SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if not self.head.heading() == NORTH:
            self.head.setheading(SOUTH)

    def right(self):
        if not self.head.heading() == WEST:
            self.head.setheading(EAST)

    def left(self):
        if not self.head.heading() == EAST:
            self.head.setheading(WEST)
