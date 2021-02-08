import argparse
import logging
import time

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
import scripts.label_image as label_img

logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0
def cropHands(points, frame):
    # define croping values
    minusX = 70
    minusY = 70
    h = 200
    w = 200

    # output
    if (points[0] >= minusX and points[1] >= minusY):
        x = points[0] - minusX
        y = points[1] - minusY
    else:
        x = points[0]
        y = points[1]
    
        # Croping the frame
    crop_frame = frame[y:y+h, x:x+w]

    return crop_frame


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)

    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    args = parser.parse_args()

    w, h = model_wh(args.resize)
    if w > 0 and h > 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))

    cam = cv2.VideoCapture(args.camera)

    count = 0
    while True:
    
        ret_val, image1 = cam.read()
        
        humans = e.inference(image1, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)

        img = TfPoseEstimator.draw_humans(image1, humans, imgcopy=True)
        
        for human in humans:
            for i in human.body_parts.keys():
                if i == 7:
                    left_wrist_point = human.body_parts[7]
                    print('wrist aaa')
                    print(left_wrist_point.x)
                    print(left_wrist_point.y)
                    image_h, image_w = image1.shape[:2]
                    center = (int(left_wrist_point.x * image_w + 0.5), int(left_wrist_point.y * image_h + 0.5))
                    print(center)
                    crop_frame = cropHands(center, image1)
                    cv2.imshow('frame',crop_frame)
                
        cv2.imshow('tf-pose-estimation result', img)
        
        fps_time = time.time()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += 1

    cv2.destroyAllWindows()

# =============================================================================
# For running the script simply run the following in the cmd prompt/terminal :
# python run_webcam.py --model=mobilenet_thin --resize=432x368 --camera=0
# =============================================================================
