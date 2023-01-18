
class Menu:
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    bg = pygame.transform.scale(load_image('menu_bg.jpg'), (500, 500))
    pygame.display.set_caption('Fair Final')
    screen.blit(bg, (0, 0))
    head_font = pygame.font.SysFont('couriernew', 76, True)
    button_font = pygame.font.SysFont('arial', 43, True)
    header_text = head_font.render('Fair Final', True, (255, 255, 255))
    start_button_text = button_font.render('Начать', True, (255, 255, 255))
    screen.blit(header_text, (30, 50))
    screen.blit(start_button_text, (200, 175))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 175 < x < 340 and 160 < y < 230:
                    start()
                    pygame.display.flip()
        pygame.display.flip()

