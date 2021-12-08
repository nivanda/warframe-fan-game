from imageai.Detection import ObjectDetection
import pygame, os, sys, json

pygame.init()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("assets/model/resnet50_coco_best_v2.1.0.h5")
detector.loadModel()

WIDTH = 1000
HEIGHT = 700

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warframe crafter with imageAI")

main_font = pygame.font.SysFont('comicsans', 60)
second_font = pygame.font.SysFont('comicsans', 20)

data = {"materials": {"alloyplate": 0, "argoncrystal": 0, "circuits": 0, "controlmodule": 0, "cryotic": 0, "ferrite": 0, "gallium": 0, 
        "hexenon": 0, "morphics": 0, "nanospores": 0, "neuralsensors": 0, "neurodes": 0, "orokincell": 0, "oxium": 0, "plastids": 0, 
        "polymerbundle": 0, "rubedo": 0, "salvage": 0, "tellurium": 0}, "primary": {"boltor": 0, "cedo": 0, "vulkar": 0}, 
        "secondary": {"furis": 0, "knell": 0, "kraken": 0}, "melee": {"fragor": 0, "heatsword": 0, "skana": 0}, 
        "parts": {"barrel": 0, "forma": 0, "receiver": 0, "stock": 0, "excalibursystems": 0, "excaliburneuroptics": 0, 
        "excaliburchassis": 0}, "warframes": {"excalibur": 0}}

close = second_font.render("CLOSE", 1, (255, 255, 255))

mainMenu1 = main_font.render("INVENTORY", 1, (255, 255, 255))
mainMenu2 = main_font.render("RESEARCH", 1, (255, 255, 255))
mainMenu3 = main_font.render("CRAFT", 1, (255, 255, 255))
mainMenu4 = main_font.render("SCAN", 1, (255, 255, 255))

inventory1 = second_font.render("MATERIALS", 1, (255, 255, 255))
inventory2 = second_font.render("BLUEPRINTS", 1, (255, 255, 255))
inventory3 = second_font.render("PARTS", 1, (255, 255, 255))
inventory4 = second_font.render("MELEE", 1, (255, 255, 255))
inventory5 = second_font.render("PRIMARY", 1, (255, 255, 255))
inventory6 = second_font.render("SECONDARY", 1, (255, 255, 255))
inventory7 = second_font.render("WARFRAMES", 1, (255, 255, 255))

menuSelector = "main menu"
    

def refresh():
    win.fill((0, 0, 0))
    if menuSelector == "main menu":
        win.blit(mainMenu1, (50, 25))
        win.blit(mainMenu2, (50, 25 + mainMenu1.get_height() + 25))
        win.blit(mainMenu3, (50, 25 + mainMenu1.get_height() + mainMenu2.get_height() + 50))
        win.blit(mainMenu4, (50, 25 + mainMenu1.get_height() + mainMenu2.get_height() + mainMenu3.get_height() + 75))
    elif menuSelector == "inventory":
        win.blit(inventory1, (25, 10))
        win.blit(inventory2, (inventory1.get_width() + 40, 10))
        win.blit(inventory3, (inventory1.get_width() + inventory2.get_width() + 55, 10))
        win.blit(inventory4, (inventory1.get_width() + inventory2.get_width() + inventory3.get_width() + 70, 10))
        win.blit(inventory5, (inventory1.get_width() + inventory2.get_width() + inventory3.get_width() + inventory4.get_width() + 85, 10))
        win.blit(inventory6, (inventory1.get_width() + inventory2.get_width() + inventory3.get_width() + inventory4.get_width() + inventory5.get_width() + 100, 10))
        win.blit(inventory7, (inventory1.get_width() + inventory2.get_width() + inventory3.get_width() + inventory4.get_width() + inventory5.get_width() + inventory6.get_width() + 115, 10))
        win.blit(close, (25, HEIGHT - 15 - close.get_height()))
    elif menuSelector == "research":
        pass
    elif menuSelector == "craft":
        pass
    elif menuSelector == "scan":
        pass


def SaveLoadGame(load):
    global data
    if load:
        if os.path.exists("savegames/save.json"):
            with open("savegames/save.json", 'r') as save:
                data = json.load(save)
    else:
        with open("savegames/save.json", 'w') as save:
            json.dump(data, save)

def game():
    global menuSelector, data
    SaveLoadGame(True)
    run = True
    while run:
        refresh()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveLoadGame(False)
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuSelector == "main menu":
                    menu1 = mainMenu1.get_rect(topleft = (50, 25))
                    menu2 = mainMenu2.get_rect(topleft = (50, 25 + mainMenu1.get_height() + 25))
                    menu3 = mainMenu3.get_rect(topleft = (50, 25 + mainMenu1.get_height() + mainMenu2.get_height() + 50))
                    menu4 = mainMenu4.get_rect(topleft = (50, 25 + mainMenu1.get_height() + mainMenu2.get_height() + mainMenu3.get_height() + 75))
                    if menu1.collidepoint(event.pos):
                        menuSelector = "inventory"
                    elif menu2.collidepoint(event.pos):
                        pass
                    elif menu3.collidepoint(event.pos):
                        pass
                    elif menu4.collidepoint(event.pos):
                        menuSelector = "scan"
        pygame.display.update()

game()