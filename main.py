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

main_font = pygame.font.SysFont('comicsans', 35)

data = {"materials": {"alloyplate": 0, "argoncrystal": 0, "circuits": 0, "controlmodule": 0, "cryotic": 0, "ferrite": 0, "gallium": 0, 
        "hexenon": 0, "morphics": 0, "nanospores": 0, "neuralsensors": 0, "neurodes": 0, "orokincell": 0, "oxium": 0, "plastids": 0, 
        "polymerbundle": 0, "rubedo": 0, "salvage": 0, "tellurium": 0}, "primary": {"boltor": 0, "cedo": 0, "vulkar": 0}, 
        "secondary": {"furis": 0, "knell": 0, "kraken": 0}, "melee": {"fragor": 0, "heatsword": 0, "skana": 0}, 
        "parts": {"barrel": 0, "forma": 0, "receiver": 0, "stock": 0, "excalibursystems": 0, "excaliburneuroptics": 0, 
        "excaliburchassis": 0}, "warframes": {"excalibur": 0}}

def refresh():
    pass

def SaveLoadGame(load):
    if load:
        

def game():
    run = True
    while run:
        refresh()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

game()