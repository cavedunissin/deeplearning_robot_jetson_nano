## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)

##########################################################################
align_to = rs.stream.color
align = rs.align(align_to)
##########################################################################
try:
    while True:
        frames = pipeline.wait_for_frames()

        #######################################
        aligned_frames = align.process(frames)
        #######################################

        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_WINTER)

        ###############################################################################################################
        face_cascade = cv2.CascadeClassifier('/home/jetsonnano/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5, minSize=(50,50))
        for (x, y, w, h) in faces:
            cv2.rectangle(color_image, (x, y-5), (x+w,y+h), (255, 0, 0), 2)
            text_depth = "depth is "+str(np.round(depth_frame.get_distance(int(x+(1/2)*w),int(y+(1/2)*h)),3))+"m"
            color_image=cv2.putText(color_image,text_depth,(x,y-5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1,cv2.LINE_AA)
        ################################################################################################################

        images = np.hstack((color_image, depth_colormap))

        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
  
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break

finally:
    pipeline.stop()
