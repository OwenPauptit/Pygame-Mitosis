import pygame, time, random

class Cell:

    def __init__(self,x,y,radius,colour,width,height):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.width = width
        self.height = height
        self.px = random.randint(-10,10)
        self.py = random.randint(-10,10)
    def drawSelf(self,screen):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.radius)

    def move(self):
        change = random.randint(1,5)
        if self.px+change > 15:
            hx = 15
        else:
            hx = self.px+change
        if self.px-change < -15:
            lx = -15
        else:
            lx = self.px-change
        x = random.randint(lx,hx)

        if self.py + change > 15:
            hy = 15
        else:
            hy = self.py + change
        if self.py - change < -15:
            ly = -15
        else:
            ly = self.py - change
        y = random.randint(ly, hy)
        # x = random.randint(-5,5)
        # y = random.randint(-5,5)
        # x = int((x+self.px)/2)
        # y = int((y+self.py)/2)
        self.x = self.x + x
        self.y = self.y + y
        if self.x < self.radius:
            self.x = self.radius
            self.px = random.randint(-2,5)
        elif self.x > self.width-self.radius:
            self.x = self.width-self.radius
            self.px = random.randint(-5,2)
        if self.y < self.radius:
            self.y = self.radius
            self.py = random.randint(-2,5)
        elif self.y > self.height - self.radius:
            self.y = self.height - self.radius
            self.py = random.randint(-5,2)

    def isClicked(self,screen):
        click = screen.get_at(pygame.mouse.get_pos()) == self.colour
        if click == 1:
            return True

    def divide(self):
        r,g,b = self.colour
        self.colour = (r+random.randint(-20,20),g+random.randint(-20,20),b+random.randint(-20,20))
        self.colour = checkColour(self.colour)
        self.radius = int(round(self.radius/1.4,0))
        newcol = (r+random.randint(-20,20),g+random.randint(-20,20),b+random.randint(-20,20))
        newcol = checkColour(newcol)
        newpx = self.px * -1
        newpy = self.py * - 1
        print (newcol, self.colour)
        cell = newCell(self.width,self.height,self.radius,newcol,newpx,newpy,self.x,self.y)
        return cell

    def grow(self):
        self.radius = int(round(self.radius * 1.4,0))

def checkColour(colour):
    colours = list(colour)
    for i in range(0,len(colours)):
        if colours[i] > 255:
            colours[i] = 255
            print ("set to 255")
        elif colours[i] < 0:
            colours[i] = 0
            print ("set to 0")
    return tuple(colours)

def newCell(width,height,radius=40,colour=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),px=random.randint(-10,10),py=random.randint(-10,10),x=-1,y=-1):
    if x == -1 and y == -1:
        x = random.randint(radius,width-radius)
        y = random.randint(radius,height-radius)
    newCell = Cell(x,y,radius,colour,width,height)
    return newCell

def main():
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Mitosis Simulator")
    screen.fill((255,255,255))
    cells = []
    cells.append(newCell(width,height))
    cells[0].drawSelf(screen)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickType = event.button
                for cell in cells:
                    if cell.isClicked(screen):
                        if clickType == 1: cells.append(cell.divide())
                        elif clickType == 3: cell.grow()
                        else: del cells[cells.index(cell)]
            if event.type == pygame.KEYDOWN:
                if event.key == ord("r"):
                    main()

        screen.fill((255,255,255))
        for cell in cells:
            cell.move()
            cell.drawSelf(screen)
        pygame.display.update()
        time.sleep(0.05)

if __name__ == "__main__":
    main()
