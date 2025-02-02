import jetson_inference as jet_inf
import jetson_utils as jet_ut


net = jet_inf.detectNet('ssd-mobilenet-v2', threshold=0.6)
#'ssd-mobilenet-v1','ssd-inception-v2','peoplenet','peoplenet-pruned',
#'dashcamnet','trafficcamnet','facedetect'

#net = jet_inf.imageNet('googlenet')
#'alexnet','googlenet','googlenet-12','resnet-18','resnet-50',
#'resnet-101','resnet-152','vgg-16','vgg-19','inception-v4'

cam = jet_ut.gstCamera(640, 480, '/dev/video1')
disp = jet_ut.glDisplay()
font = jet_ut.cudaFont()

while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    # classID, confident = net.Classify(frame, width, height)
    # item=net.GetClassDesc(classID)
    # font.OverlayText(frame, width, height, item, 5, 5, font.Magenta, font.Blue)
    # disp.RenderOnce(frame, width, height)

    detections = net.Detect(frame, width, height)
    disp.RenderOnce(frame, width, height)
    # dt = time.time() - timeStamp
    # timeStamp = time.time()
    # fps = 1 / dt
    # fpsFltr = 0.9*fpsFltr + 0.1*fps
    # print(str(round(fps, 1)) + ' fps ')
    disp.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    if KeyboardInterrupt is True:
        break

cam.release()
