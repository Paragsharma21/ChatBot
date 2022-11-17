from tkinter import*
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3 
import sys
import tkinter as tk
from tkinter import filedialog, Text
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):   
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    print("what can i do for you")
    speak("what can i do for you")       
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'search' in query:
            speak('Searching web...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to web")
            print(results)
            speak(results)
        elif 'are you' in query:
            print('I am very good , enjoying my time , learning new things ')
            speak('I am very good , enjoying my time , learning new things')
        elif 'do' in query:
            print('I can search on web just say search before any question\nopen YouTube\nopen google\ntell simple questions and still learning\nplay games with you')
            speak('I can search on web just say search before any question , open YouTube , open google , tell simple questions and still learning\nplay games with you')
        elif 'hello' in query:
            print('hello Sir, how are you nice to meet you')
            speak('hello Sir, how are you nice to meet you')
        elif 'name' in query:
            print('my name is Phoebe , i am a voice chat bot')
            speak('my name is Phoebe , i am a voice chat bot')
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=VuG7ge_8I2Y")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\coool\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)
        elif 'wow' in query:
            print('thank you!')
            speak('thank you!')
        elif 'good' in query:
            print('amazing')
            speak('amazing')
        elif 'great' in query:
            print('i am flattred!!')
            speak('i am flattred!!')
        elif 'bye' in query:
            print("bye, come back soon till then i'll learn more!")
            speak("bye, come back soon till then i'll learn more!")
            exit()
        elif 'snake'in query:
            print("ok")
            import pygame
            import time
            import random
            
            pygame.init()
            
            white = (255, 255, 255)
            yellow = (255, 255, 102)
            black = (0, 0, 0)
            red = (213, 50, 80)
            green = (0, 255, 0)
            blue = (50, 153, 213)
            
            dis_width = 600
            dis_height = 400
            
            dis = pygame.display.set_mode((dis_width, dis_height))
            pygame.display.set_caption('Phoebe SNAKE GAME')
            
            clock = pygame.time.Clock()
            
            snake_block = 10
            snake_speed = 15 
            
            font_style = pygame.font.SysFont("bahnschrift", 25)
            score_font = pygame.font.SysFont("comicsansms", 35)
            
            
            def Your_score(score):
                value = score_font.render("Your Score: " + str(score), True, yellow)
                dis.blit(value, [0, 0])
            
            
            
            def our_snake(snake_block, snake_list):
                for x in snake_list:
                    pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
            
            
            def message(msg, color):
                mesg = font_style.render(msg, True, color)
                dis.blit(mesg, [dis_width / 6, dis_height / 3])
            
            
            def gameLoop():
                game_over = False
                game_close = False
            
                x1 = dis_width / 2
                y1 = dis_height / 2
            
                x1_change = 0
                y1_change = 0
            
                snake_List = []
                Length_of_snake = 1
            
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            
                while not game_over:
            
                    while game_close == True:
                        dis.fill(blue)
                        message("You Lost! Press C-Play Again or Q-Quit", red)
                        Your_score(Length_of_snake - 1)
                        pygame.display.update()
            
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    game_over = True
                                    game_close = False
                                if event.key == pygame.K_c:
                                    gameLoop()
            
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x1_change = -snake_block
                                y1_change = 0
                            elif event.key == pygame.K_RIGHT:
                                x1_change = snake_block
                                y1_change = 0
                            elif event.key == pygame.K_UP:
                                y1_change = -snake_block
                                x1_change = 0
                            elif event.key == pygame.K_DOWN:
                                y1_change = snake_block
                                x1_change = 0
            
                    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                        game_close = True
                    x1 += x1_change
                    y1 += y1_change
                    dis.fill(blue)
                    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                    snake_Head = []
                    snake_Head.append(x1)
                    snake_Head.append(y1)
                    snake_List.append(snake_Head)
                    if len(snake_List) > Length_of_snake:
                        del snake_List[0]
            
                    for x in snake_List[:-1]:
                        if x == snake_Head:
                            game_close = True
            
                    our_snake(snake_block, snake_List)
                    Your_score(Length_of_snake - 1)
            
                    pygame.display.update()
            
                    if x1 == foodx and y1 == foody:
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                        Length_of_snake += 1
            
                    clock.tick(snake_speed)
            
                pygame.quit()
                quit()
            
            
            gameLoop()
        elif 'brick'in query:
            import pygame
            import time

            SCREEN_SIZE = 640, 480


            #object dimensions
            BRICK_WIDTH = 60
            BRICK_HEIGHT = 15
            PADDLE_WIDTH = 60
            PADDLE_HEIGHT = 12
            BALL_DIAMETER = 16
            BALL_RADIUS = BALL_DIAMETER / 2

            MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
            MAX_BALL_X = SCREEN_SIZE[0] - BALL_DIAMETER
            MAX_BALL_Y = SCREEN_SIZE[1] - BALL_DIAMETER

            # paddle y coordinate
            PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10 

            #color constants
            BLACK = (0 ,0 , 0)
            WHITE = (255, 255, 255)
            BLUE = (0, 0, 255)
            BRICK_COLOR = (0, 255, 0) #GREEN

            #state constants
            STATE_BALL_IN_PADDLE = 0
            STATE_PLAYING = 1
            STATE_WON = 2
            STATE_GAME_OVER = 3
            STATE_CHANGING_LEVEL = 4



            class BrickBreak:
                
                def __init__(self):
                    pygame.init()
                    
                    self.screen = pygame.display.set_mode(SCREEN_SIZE)
                    pygame.display.set_caption("Phoebe BrickBreak Game")
                    
                    self.clock = pygame.time.Clock()
                    
                    if pygame.font:
                        self.font = pygame.font.Font(None, 30)
                    else:
                        self.font = None
                    
                    #change the variable to load a specific level first
                    #variable (level, score, lives)	
                    self.init_game(9, 0, 3)


                def init_game(self, thelevel, thescore, thelives):
                    self.level = thelevel
                    self.lives = thelives
                    self.score = thescore
                    self.state = STATE_BALL_IN_PADDLE
                
                    self.paddle = pygame.Rect(300, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
                    self.ball = pygame.Rect(300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)
                
                    self.ball_vel = [5, -5]
                
                    if self.level == 0:
                        self.create_bricks()
                    elif self.level == 1:
                        self.create_bricks1()
                    elif self.level == 2:
                        self.create_bricks2()
                    elif self.level == 3:
                        self.create_bricks3()
                    elif self.level == 4:
                        self.create_bricks4()
                    elif self.level == 5:
                        self.create_bricks5()
                    elif self.level == 6:
                        self.create_bricks6()
                    elif self.level == 7:
                        self.create_bricks7()
                    elif self.level == 8:
                        self.create_bricks8()
                    elif self.level == 9:
                        self.create_bricks9()
                        
                    
                ################################################################		
                ################################################################
                # here is all the code to create the bricks for different levels
                        
                #level 1
                def  create_bricks(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range (7):
                        x_ofs = 35
                        for j in range(8):
                            self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += BRICK_WIDTH + 10
                        y_ofs += BRICK_HEIGHT + 5
                        
                #level 2
                def create_bricks1(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range (7):
                        x_ofs = 45
                        for j in range(8):
                            if (j % 2 == 0):
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                                x_ofs += (BRICK_WIDTH + 20) * 2
                        y_ofs += BRICK_HEIGHT + 5
                        
                #level 3
                def create_bricks2(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8):
                        x_ofs = 35
                        if i % 2 == 1:
                            for j in range(8):
                                self.bricks.append(pygame.Rect(x_ofs,y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                                x_ofs += BRICK_WIDTH + 10
                            y_ofs += (BRICK_HEIGHT + 5) * 2
                
                # level 4
                def create_bricks3(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8):
                        x_ofs = 10
                        if i % 2 == 1:
                            for j in range(10):
                                if j % 2 == 1:
                                    self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                                    x_ofs += (BRICK_WIDTH + 10) * 2
                            y_ofs += (BRICK_HEIGHT + 5) * 2
                
                #level 5			
                def create_bricks4(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8):
                        x_ofs = 35
                        for j in range(8):
                            if j == i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                            
                #level 6
                def create_bricks5(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8):
                        x_ofs = 35
                        for j in range(8):
                            if j != i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                
                #level 7		
                def create_bricks6(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8, 0, -1):
                        x_ofs = 35
                        for j in range(8):
                            if j == i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                            
                #level 8	
                def create_bricks7(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8, 0, -1):
                        x_ofs = 35
                        for j in range(8):
                            if j == i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                    for i in range(8, 0, -1):
                        x_ofs = 35
                        for j in range(8):
                            if j == i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                
                #level 9	
                def create_bricks8(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(8):
                        x_ofs = 35
                        for j in range(8):
                            if j == i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                    for i in range(8):
                        x_ofs = 35
                        for j in range(8):
                            if j == i:
                                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += (BRICK_WIDTH + 10)
                        y_ofs += BRICK_HEIGHT + 5
                            
                    
                #level 10	
                def create_bricks9(self):
                    y_ofs = 35
                    self.bricks = []
                    for i in range(16):
                        x_ofs = 35
                        for j in range(8):
                            self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                            x_ofs += BRICK_WIDTH + 10
                        y_ofs += BRICK_HEIGHT + 5
                        
                    
                ###########################################################
                ###########################################################		
                        
                def draw_bricks(self):
                    for brick in self.bricks:
                        pygame.draw.rect(self.screen, BRICK_COLOR, brick)
                    
                    
                def check_input(self):
                    keys = pygame.key.get_pressed()
                
                    if keys[pygame.K_LEFT]:
                        self.paddle.left -= 10
                        if self.paddle.left < 0:
                            self.paddle.left = 0
                        
                    if keys[pygame.K_RIGHT]:
                        self.paddle.left += 10
                        if self.paddle.left > MAX_PADDLE_X:
                            self.paddle.left = MAX_PADDLE_X
                        
                    if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:
                        self.ball_vel = [5, -5]
                        self.state = STATE_PLAYING
                        
                    elif keys[pygame.K_RETURN] and self.state == STATE_WON:
                        self.level += 1
                        self.lives += 1
                        self.init_game(self.level, self.score, self.lives)
                        
                    elif keys[pygame.K_RETURN] and self.state == STATE_GAME_OVER:
                        self.init_game(0,0,3)
                    
                def move_ball (self):
                    self.ball.left += self.ball_vel[0]
                    self.ball.top += self.ball_vel[1]
                
                    if self.ball.left <= 0:
                        self.ball.left = 0
                        self.ball_vel[0] = -self.ball_vel[0]
                    elif self.ball.left >= MAX_BALL_X:
                        self.ball.left = MAX_BALL_X
                        self.ball_vel[0] = -self.ball_vel[0]
                    
                    if self.ball.top < 0:
                        self.ball.top = 0
                        self.ball_vel[1] = -self.ball_vel[1]
                    
                def handle_collisions(self):
                    for brick in self.bricks:
                        if self.ball.colliderect (brick):
                            self.score += 3
                            self.ball_vel[1] = -self.ball_vel[1]
                            self.bricks.remove(brick)
                            break
                    
                    if len(self.bricks) == 0:
                        self.state = STATE_WON
                        
                    if self.ball.colliderect (self.paddle):
                        self.ball.top = PADDLE_Y - BALL_DIAMETER
                        self.ball_vel[1] = -self.ball_vel[1]
                        
                    #if the ball hits the ground
                    elif self.ball.top > self.paddle.top:
                        self.lives -= 1
                        if self.lives > 0:
                            self.state = STATE_BALL_IN_PADDLE
                        else:
                            self.state = STATE_GAME_OVER
                            
                def show_stats(self):
                    if self.font:
                        font_surface = self.font.render("LEVEL: " + str(self.level + 1) + " SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, WHITE)
                        self.screen.blit(font_surface, (205, 5))
                    
                    
                def show_message(self, message):
                    if self.font:
                        size = self.font.size(message)
                        font_surface = self.font.render(message, False, WHITE)
                        x = (SCREEN_SIZE[0] - size[0])
                        y = (SCREEN_SIZE[1] - size[1]) / 1
                        self.screen.blit(font_surface, (x, y))
                    
                    
                def run(self):
                    while 1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            
                        self.clock.tick(50)
                        self.screen.fill(BLACK)
                        self.check_input()
                    
                        if self.state == STATE_PLAYING:
                            self.move_ball()
                            self.handle_collisions()
                        elif self.state == STATE_BALL_IN_PADDLE:
                            self.ball.left = self.paddle.left + self.paddle.width / 2
                            self.ball.top = self.paddle.top - self.ball.height
                            self.show_message("PRESS SPACE TO START")
                        elif self.state == STATE_GAME_OVER:
                            self.show_message("GAME OVER. PRESS ENTER TO RESTART")
                        elif self.state == STATE_WON:
                            self.show_message("YOU WON! PRESS ENTER TO PLAY THE NEXT LEVEL")
                        elif self.state == STATE_WON and self.level == 9:
                            self.show_message("CONGRATULATIONS, YOU'VE COMPLETED THE GAME!!")
                        
                        
                    
                        #draw paddle
                        pygame.draw.rect(self.screen, BLUE, self.paddle)
                    
                        #draw ball
                        pygame.draw.circle(self.screen, WHITE, (self.ball.left + BALL_RADIUS, self.ball.top + BALL_RADIUS), BALL_RADIUS)
                    
                        
                        self.draw_bricks()
                    
                        self.show_stats()
                    
                        pygame.display.flip()
                        
                        #have this here for cascading block drawing
                        #self.draw_bricks().py
                    
            if __name__ == "__main__":
                BrickBreak().run()
        elif 'game'in query:
            print("which game you want to play snake game or brick game")
            speak("which game you want to play snake game or brick game")
        elif '' in query: 
            speak("sorry i cant understand!")

