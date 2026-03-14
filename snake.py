import pygame

play_button = Button(WIN_SIZE[0] // 2 - BUTTON_SIZE[0] // 2, 
                     100,
                       BUTTON_SIZE[0],
                       BUTTON_SIZE[1],
                     ((236, 60, 0),(190,49,0),(236,60,0)),
                     ((255,255,255),(255,245,0),(235,29,0)),
                       "PLAY")
exit_button = Button(WIN_SIZE[0] // 2 - BUTTON_SIZE[0] // 2, 200, BUTTON_SIZE[0], BUTTON_SIZE[1],
                     ((236, 60, 0),(190,49,0),(236,60,0)),
                     ((255,255,255),(255,245,0),(235,29,0)), "EXIT")

game = True
change_state = False
which_window = "MENU"
while game:
    events = pygame.event.get()
    if which_window == "MENU":
        window.fill(BG_COLOR)
        play_button.draw(window)
        play_button.active()
        exit_button.draw(window)
        exit_button.active()
    if play_button.active():
        which_window = "GAME"
        time_start = pygame.time.get_ticks()
    if exit_button.active():
        which_window = "EXIT"
    elif which_window == "GAME":
        
        window .fill((255, 255, 255))
    elif which_window == "EXIT":
        game = False