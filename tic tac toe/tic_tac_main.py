import pygame

class Game:
    def __init__(self):
        pygame.init()

        # WINDOW 
        self.screen_width = 300
        self.screen_height = 300
        self.window = pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption("TIC TAC TOE")

        self.bg = (255,255,200)
        self.line_width = 6

        # COLOURS
        self.black = (0,0,0)
        self.green = (0,255,0)
        self.red = (255,0,0)
        self.blue = (0,0,255)

        

        # MARKERS
        self.markers = []

        for i in range(3):
            row = [0] * 3
            self.markers.append(row)
        

        # MOUSE VARIABLES
        self.pos = ()

        # PLAYER
        self.player = 1

        self.winner = None

        self.game_over = False

        # FONTS

        self.font = pygame.font.SysFont(None, 40)
    
        

    def draw_grid(self):
        self.window.fill(self.bg)

        for x in range(1,3):
            pygame.draw.line(self.window,self.black,
            (0,x*100), (self.screen_width, x*100),self.line_width)

            pygame.draw.line(self.window,self.black,
            (100*x,0), (100*x,self.screen_height),self.line_width)


    def draw_marker(self):

        # CHECK WHICH BOXES ARE OCCUPIED BY PLAYER 1 OR 2
        x_pos = 0
        for x in self.markers:
            y_pos = 0
            for y in x:
                if y == 1:

                    # PLAYER 1 - CROSS
                    pygame.draw.line(self.window, self.green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), self.line_width)
                    pygame.draw.line(self.window, self.green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), self.line_width)

                if y == -1:

                    # PLAYER 2- CIRCLE
                    pygame.draw.circle(self.window, self.red, (x_pos * 100 + 50, y_pos *100 + 50), 38, self.line_width)
                y_pos +=  1
            
            x_pos += 1



    def check_winner(self):

        y_pos = 0 

        for x in self.markers:
            # Check ROWS

            if sum(x) == 3:
                self.winner = 1
                self.game_over = True
            
            if sum(x) == -3:
                self.winner = 2
                self.game_over = True

            
            # Check COLUMNS

            if self.markers[0][y_pos] + self.markers[1][y_pos] + self.markers[2][y_pos] == 3:
                self.winner = 1
                self.game_over = True
            
            if self.markers[0][y_pos] + self.markers[1][y_pos] + self.markers[2][y_pos] == -3:
                self.winner = 2
                self.game_over = True
            
            y_pos += 1

            # Check CROSS

            if self.markers[0][0] + self.markers[1][1] + self.markers[2][2] == 3 or self.markers[0][2] + self.markers[1][1] + self.markers[2][0] == 3:
                self.winner = 1
                self.game_over = True

            if self.markers[0][0] + self.markers[1][1] + self.markers[2][2] == -3 or self.markers[0][2] + self.markers[1][1] + self.markers[2][0] == -3:
                self.winner = 2
                self.game_over = True
            

    def draw_winner(self):
        win_text = f"Player {self.winner} won!"
        win_img = self.font.render(win_text, True, self.blue)
        pygame.draw.rect(self.window, self.green, (self.screen_width//2 -100, self.screen_height//2 - 60, 200, 50))
        self.window.blit(win_img, (self.screen_width//2 - 100, self.screen_height//2 -50))




    def run(self):
        running =  True
        clicked = False


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if self.game_over == False:
                    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                        clicked = True
                    
                    if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                        clicked = False

                        self.pos = pygame.mouse.get_pos()
                        self.cell_x = self.pos[0]
                        self.cell_y = self.pos[1]
                        if self.markers[self.cell_x // 100][self.cell_y//100] == 0:
                            self.markers[self.cell_x // 100][self.cell_y // 100] = self.player
                            self.player *= -1   # SWITCH PLAYER TURN

                            self.check_winner() # CHECK FOR WINNER

                        
            
                



            self.draw_grid()
            self.draw_marker()

            if self.game_over == True:
                self.draw_winner()

            pygame.display.update()

            #





if __name__ == '__main__':
    game = Game()
    game.run()