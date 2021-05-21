import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
 
pipeline.start(config)

align_to = rs.stream.color
align = rs.align(align_to)

try:
    while True:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)   
        depth_frame = aligned_frames.get_depth_frame() 
        color_frame = aligned_frames.get_color_frame()
        
        if not depth_frame or not color_frame:
            continue
     
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
 
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_WINTER)

#################加入這段程式#####################
        print("shape of color image:{0}".format(color_image.shape))
        print("shape of depth image:{0}".format(depth_colormap.shape))
        print("depth value in m:{0}".format(depth_frame.get_distance(320, 240)))

        text_depth = "depth value of point (320,240) is "+str(np.round(depth_frame.get_distance(320, 240),4))+"meter(s)"
        color_image = cv2.circle(color_image,(320,240),1,(0,255,255),-1)
        color_image=cv2.putText(color_image, text_depth, (10,20),  cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1, cv2.LINE_AA)

##################################################

        images = np.hstack((color_image, depth_colormap))
        
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
 
 
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
 
finally:
    pipeline.stop()
