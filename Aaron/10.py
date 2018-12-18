import pygame

f = open('input10.txt')
lines = f.readlines()

# start by reading the lines
def parseLine(line):
    position = line.split("<")[1].split(">")[0]
    position = position.split(",")
    x = int(position[0])
    y = int(position[1])

    velocity = line.split("<")[2].split(">")[0]
    velocity = velocity.split(",")
    vx = int(velocity[0])
    vy = int(velocity[1])

    return x, y, vx, vy

# Moving object class that I can eval (render) at a specific second
class MovingObject:
    def __init__(self, x, y, vx, vy):
        self.startX = x
        self.startY = y
        self.vx = vx
        self.vy = vy

    def render(self, screen, second, offsetX, offsetY ):
        pygame.draw.rect(screen, (255,255,255), [self.startX + self.vx * second + offsetX, self.startY + self.vy * second + offsetY, 1, 1], 0)

# dump parsed lines into points list
points = []
for i in range(len(lines)):
    parsed = parseLine(lines[i])
    points.append(MovingObject(parsed[0], parsed[1], parsed[2], parsed[3]))

# pygame screen setup
(width, height) = (100, 50)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

# starting condition variables
time = 10634
offsetX = -150
offsetY = -100

def update():
    global time, offsetX, offsetY

    # Animate time at a desired speed
    #  I used this to guesstimate where the correct second would be
    # Basically: set high velocity, wait for things to zip by, restart near that time, with slower speed, repeat
    #  and finally, just comment out the line to display a static second in time
    # time += 0.01

    # this is what I used to guesstimate from
    # print(int(time))

    screen.fill((0,0,0))
    for p in points:
        p.render(screen, int(time), offsetX, offsetY)

    pass

# pygame loop
running = True
while running:
    update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False