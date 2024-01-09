import pygame

class Button:
    def __init__(self, x, y, width, height, color=(0, 0, 0), text='', padx=10, pady=2, fStyle='comicsans', fSize=16, fColor=(255, 255, 255), transparant=False):
        pygame.font.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.padx = padx
        self.pady = pady
        self.rect = (self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont(fStyle, fSize)
        self.text = self.font.render(text, 1, fColor)
        self.transparant = transparant

    def isOver(self):
        pos = pygame.mouse.get_pos()
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def clicked(self):
        if self.isOver():
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False

    def draw(self, win, outline=False, outlineColor=(0, 0, 0), outWidth=2, hoverColor=None, radius=-1, width=None):
        if hoverColor == None:
            hoverColor = self.color

        if outline:
            outBox = (self.x-outWidth, self.y-outWidth, self.width + outWidth*2, self.height + outWidth*2)
            pygame.draw.rect(win, outlineColor, outBox, outWidth, border_radius=radius)
        
        if self.isOver():
            pygame.draw.rect(win, hoverColor, self.rect, border_radius=radius)

        if not self.transparant:
            pygame.draw.rect(win, self.color, self.rect, border_radius=radius)
            
        win.blit(self.text, (self.x+self.padx, self.y+self.pady))
        # pygame.display.update()

if __name__ == "__main__":
    win = pygame.display.set_mode((600, 500))
    button = Button(270, 230, 28, 33, text='click me:)')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        win.fill((255, 255, 255))
        button.draw(win, outline=True, outlineColor=(255, 0, 0), hoverColor=(255, 255, 0))
        if button.clicked():
            print("Thanks for clicking")

        pygame.display.update()