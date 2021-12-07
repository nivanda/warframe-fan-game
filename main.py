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

data = {"materials": {"alloyplate": 0, "argoncrystal": 0, "circuits": 0, "controlmodule": 0, "cryotic": 0, "ferrite": 0, "gallium": 0, 
        "hexenon": 0, "morphics": 0, "nanospores": 0, "neuralsensors": 0, "neurodes": 0, "orokincell": 0, "oxium": 0, "plastids": 0, 
        "polymerbundle": 0, "rubedo": 0, "salvage": 0, "tellurium": 0}, "primary": {"boltor": 0, "cedo": 0, "vulkar": 0}, 
        "secondary": {"furis": 0, "knell": 0, "kraken": 0}, "melee": {"fragor": 0, "heatsword": 0, "skana": 0}, 
        "parts": {"barrel": 0, "forma": 0, "receiver": 0, "stock": 0, "excalibursystems": 0, "excaliburneuroptics": 0, 
        "excaliburchassis": 0}, "warframes": {"excalibur": 0}}

mainMenu1 = main_font.render("INVENTORY", 1, (255, 255, 255))
mainMenu2 = main_font.render("RESEARCH", 1, (255, 255, 255))
mainMenu3 = main_font.render("CRAFT", 1, (255, 255, 255))
mainMenu4 = main_font.render("SCAN", 1, (255, 255, 255))
    

def refresh():
    win.fill((0, 0, 0))
    win.blit(mainMenu1, (50, 25))
    win.blit(mainMenu2, (50, 25 + mainMenu1.get_height() + 25))
    win.blit(mainMenu3, (50, 25 + mainMenu1.get_height() + mainMenu2.get_height() + 50))
    win.blit(mainMenu4, (50, 25 + mainMenu1.get_height() + mainMenu2.get_height() + mainMenu3.get_height() + 75))


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
    SaveLoadGame(True)
    run = True
    while run:
        refresh()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveLoadGame(False)
                run = False
        pygame.display.update()

game()