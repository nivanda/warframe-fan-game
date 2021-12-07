from imageai.Detection import ObjectDetection

detector = ObjectDetection()

ModelPath = "assets/model/resnet50_coco_best_v2.1.0.h5"
InputPath = "assets/input/input.jpg"
OutputPath = "assets/output/output.jpg"

detector.setModelTypeAsRetinaNet()
detector.setModelPath(ModelPath)
detector.loadModel()

detection = detector.detectObjectsFromImage(input_image=InputPath, output_image_path=OutputPath)
for eachItem in detection:
    print(eachItem["name"], " : ", eachItem["percentage_probability"])