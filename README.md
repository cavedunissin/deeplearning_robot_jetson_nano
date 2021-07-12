# [初學 Jetson Nano 不說 No - CAVEDU 教你一次懂]
CAVEDU 出版之 Jetson Nano 書籍範例與相關資源

## 作者
* 曾吉弘博士，CAVEDU教育團隊技術總監、MIT CSAIL訪問學者、NVIDIA Jetson AI ambassador
* 郭俊廷，CAVEDU教育團隊資深講師、NVIDIA Jetson AI specialist

<img src=./pics/ambassador_DavidTseng.png width="400" height="">

## 章節
* 第一章：AI、神經網路與邊緣裝置
    - 1.1 邊緣運算裝置
    - 1.2 單板電腦
    - 1.3 NVIDIA線上資源
    - 1.4 NVIDIA Jetson 家族
    - 1.5 Jetson Nano 4GB開發套件開箱
* 第二章：Jetson Nano 單板電腦
    - 2.1 Jetson Nano開機！
    - 2.2 OpenCV電腦視覺函式庫
* 第三章：深度學習結合視覺辨識
    - 3.1 深度學習介紹
    - 3.2 jetson-inference相關軟體安裝
    - 3.3 影像辨識範例
    - 3.4 物件偵測範例
    - 3.5 影像分割範例
* 第四章：GPIO硬體控制
    - 4.1 Jetson Nano GPIO腳位介紹
    - 4.2 安裝GPIO套件
    - 4.3 數位輸入、輸出
    - 4.4 I2C LCD 螢幕
* 第五章：Jetbot機器人動作控制
    - 5.1 Jetbot
    - 5.2 Jupyter Lab基礎操作介紹
    - 5.3 Jetbot範例程式
* 第六章：JetBot深度視覺機器人
    - 6.1 淺談深度學習
    - 6.2 障礙迴避
    - 6.3 道路跟隨
* 第七章：Intel RealSense 深度視覺攝影機
    - 7.1 Intel RealSense景深攝影機
    - 7.2 在Jetson Nano上安裝RealSense 套件
    - 7.3 在RealSense Viewer中檢視深度影像
    - 7.4 RealSense的Python範例
    - 7.5 使用RealSense D435-辨識人臉與距離

## 相關連結
* 開機用 SD 卡映像檔下載：https://developer.nvidia.com/jetson-nano-sd-card-image-441
* CAVEDU 技術部落格相關文章：https://blog.cavedu.com/?s=jetson
* 購書：https://robotkingdom.com.tw/product/9789869329989/
* 購買 Jetson Nano套件：https://robotkingdom.com.tw/product/nvidia-jetson-nano-developer-kit-set-b01/
* 購買 RK-jetbot：https://robotkingdom.com.tw/?s=jetbot&post_type=product
<img src=https://robotkingdom.com.tw/wp-content/uploads/2020/03/IMG_5024-scaled.jpg width="500" height="">

## Jetbot 材料表

* 機器人王國商城購買連結:https://robotkingdom.com.tw/product/rk-jetbot-luxurious/
* NVIDIA原廠建議之材料表：https://github.com/NVIDIA-AI-IOT/jetbot/wiki/bill-of-materials
* 1．JETSON NANO DEVELOPMENT KIT *1+風扇*1
* 2．64GB Micro SD卡 *1
* 3．5V4A變壓器(接頭外徑5.5mm/內徑2.1mm)*1
* 4．TT馬達*2(已焊線)
* 5．DFRobot DFR0592馬達驅動板*1
* 6．全向輪*1
* 7．PQI 12000mAh Type C雙輸出行動電源*1
* 8．Type C TO Micro USB線*1
* 9．USB線紅黑剝線頭*1
* 10．壓克力車身*1
* 11．攝影機支架3D列印件固定座*1
* 12．IMX219 MIPI 高品質視覺攝像模組*1
* 13．輪胎*2
* 14．D-Link N150無線網卡*1
* 15．金屬螺絲螺帽+塑膠螺絲螺帽*N

<img src=https://robotkingdom.com.tw/wp-content/uploads/2019/12/IMG_2420-scaled.jpg width="500" height="">


## 各章註解
**第一章：AI、神經網路與邊緣裝置**
*	[註1-1] Bringing AI to the device: Edge AI chips come into their own:  https://www2.deloitte.com/cn/en/pages/technology-media-and-telecommunications/articles/tmt-predictions-2020-ai-chips.html
*	[註1-2] 何謂邊緣運算？https://blogs.nvidia.com.tw/2019/10/22/what-is-edge-computing/
*	[註1-3] Raspberry Pi 4: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/
*	[註1-4] tinyML: https://www.tinyml.org/summit/
*	[註1-5] NVIDIA developer blog: https://developer.nvidia.com/blog/tag/jetson-nano/
*	[註1-6] NVIDIA developer forum: https://forums.developer.nvidia.com/ https://devtalk.nvidia.com/default/board/139/embedded-systems/1
*	[註1-7] NVIDIA開發者網站：https://developer.nvidia.com/
*	[註1-8]NVIDIA DLI: https://www.nvidia.com/zh-tw/deep-learning-ai/education/
*	[註1-9] Getting Started With AI On Jetson Nano: https://courses.nvidia.com/courses/course-v1:DLI+C-RX-02+V1/about
*	[註1-10] Getting Started with DeepStream for Video Analytics on Jetson Nano: https://courses.nvidia.com/courses/course-v1:DLI+C-IV-02+V1/info
*	[註1-11] Jetson 人工智慧認證： https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs
*	[註1-12] Jetson Nano專案彙整：https://developer.nvidia.com/embedded/community/jetson-projects
*	[註1-13] Jetson系列原廠頁面：https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/ ; https://developer.nvidia.com/embedded/jetson-modules
*	[註1-14] CAVEDU技術部落格Jetson相關文章：blog.cavedu.com/?s=jetson
*	[註1-15] Jetson TX: https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/jetson-tx2/
*	[註1-16] MIT Racecar: https://racecar.mit.edu/
*	[註1-17] Jetson AGX Xavier: https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/jetson-agx-xavier/
*	[註1-18] Volvo 選用 NVIDIA DRIVE 開發量產車款：https://www.nvidia.com/zh-tw/about-nvidia/press-releases/2019/volvo-chooses-nvidia-drive-to-develop-production-models/
*	[註1-19]Jetson nano: https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/jetson-nano/
*	[註1-20] Jetbot open source robot project: https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/jetbot-ai-robot-kit/
*	[註1-21] Duckietown – Learning Autonomy: https://www.duckietown.org/ ; https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/jetson-nano/duckietown/
*	[註1-22] Jetson NX: https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/jetson-xavier-nx/
*	[註1-23] JetRacer: https://github.com/NVIDIA-AI-IOT/jetracer)
*	[註1-24] Jetson系列規格比較: https://www.nvidia.com/zh-tw/autonomous-machines/embedded-systems/ ; https://developer.nvidia.com/embedded/jetson-nano-dl-inference-benchmarks
*	[註1-25] Jetson系列之神經網路推論速度比較：https://developer.nvidia.com/embedded/jetson-benchmarks 
*	[註1-26] Jetson Nano與其他SBC效能比較：https://devblogs.nvidia.com/jetson-nano-ai-computing/
*	[註1-27] Jetson Nano快速上手頁面：https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit

**第二章：Jetson Nano 單板電腦**
* p64 CSI camera 測試指令：
<code>gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=3820, height=2464, framerate=21/1, format=NV12' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=616' ! nvvidconv ! nvegltransform ! nveglglessink -e</code>

*   [註2-1] Jetson Nano主頁面：https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro
*	[註2-2] Jetson Nano映像檔載點：https://developer.nvidia.com/jetson-nano-sd-card-image-441
*	[註2-3] balenaEtcher: https://www.balena.io/etcher/ NVIDIA有提供各作業系統的英文教學
*	[註2-4] Win32 Disk Imager:https://sourceforge.net/projects/win32diskimager/
*	[註2-5] Jetson Nano各接頭介紹：https://developer.nvidia.com/zh-cn/embedded/learn/get-started-jetson-nano-devkit
*	[註2-6] 機器人王國Jetson Nano 4GB套件包：https://robotkingdom.com.tw/product/rk-nvidia-jetson-nano-developer-dlikit/
*	[註2-7] Ubuntu系統操作：https://www.ubuntu-tw.org/
*	[註2-8] NVIDIA Jetson 開發者專區：https://developer.nvidia.com/embedded-computing
*	[註2-9] NVIDIA Jetson支援論壇：https://devtalk.nvidia.com/default/board/139/embedded-systems/1
*	[註2-10] puTTY連線程式：https://www.putty.org/
*	[註2-11] MobaXterm連線程式：https://mobaxterm.mobatek.net/
*	[註2-12] Pi Camera 規格：https://www.raspberrypi.org/products/camera-module-v2/
*	[註2-13] Raspberry Pi攝影機測試：https://github.com/JetsonHacksNano/CSI-Camera
*	[註2-14] OpenCV官網：https://opencv.org/
*	[註2-15] OpenCV Wiki: https://zh.wikipedia.org/wiki/OpenCV
*	[註2-16] OpenCV Github: https://github.com/opencv/opencv
*	[註2-17] OpenCV Tutorials: https://docs.opencv.org/master/d9/df8/tutorial_root.html
*	[註2-18] OpenCV中文網站：http://www.opencv.org.cn/
*	[註2-19] HSV色彩空間：https://zh.wikipedia.org/zh-tw/HSL%E5%92%8CHSV%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4
*	[註2-20] 色彩轉換器：https://www.peko-step.com/zhtw/tool/hsvrgb.html 
*	[註2-21] 圖片疊合：https://www.twblogs.net/a/5bb03a202b7177781a0fdf6d
*	[註2-22] cv2.putText語法參數說明：https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html

**第三章：深度學習結合視覺辨識**
*	[註3-1] NVIDIA官網介紹Deploying Deep Learning: https://developer.nvidia.com/embedded/twodaystoademo
*	[註3-2] TenrsorRT: https://developer.nvidia.com/zh-cn/tensorrt
*	[註3-3] jetson-inference github網站：https://github.com/dusty-nv/jetson-inference
*	[註3-4] jetson-inference建置流程：https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md
*	[註3-5] 影像辨識Jetson-inference: Classifying Images with ImageNet: https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md
*	[註3-6] GoogleNet: https://arxiv.org/pdf/1409.4842.pdf
*	[註3-7] 物件偵測Jetson-inference: Locating Objects with DetectNet：https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-console-2.md 
*	[註3-8] MS COCO資料集：https://cocodataset.org/#home
*	[註3-9] 影像語意分割Jetson-inference: Semantic Segmentation with SegNet：https://github.com/dusty-nv/jetson-inference/blob/master/docs/segnet-console-2.md 
*	[註3-10] PASCAL VOC: http://host.robots.ox.ac.uk/pascal/VOC/

**第四章：GPIO硬體控制**
*	[註4-1] NVIDIA Jetson Nano 4GB接頭說明：https://www.jetsonhacks.com/nvidia-jetson-nano-j41-header-pinout/
*	[註4-2] jetson-gpio github: https://github.com/NVIDIA/jetson-gpio
*	[註4-3] BCM與BOARD腳位編號說明：https://iot4beginners.com/difference-between-bcm-and-board-pin-numbering-in-raspberry-pi/
*	[註4-4] 電阻色碼計算器：https://www.digikey.tw/zh/resources/conversion-calculators/conversion-calculator-resistor-color-code-4-band
*	[註4-5] I2C LCD函式庫：https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

**第五章：Jetbot機器人動作控制**
*	[註5-1] Jetbot Wiki: https://github.com/NVIDIA-AI-IOT/jetbot/wiki
*	[註5-2] Jetbot範例：https://github.com/NVIDIA-AI-IOT/jetbot/wiki/examples 
*	[註5-3] basic motion展示影片：https://youtu.be/L9TOpQhupmY 
*	[註5-4] teleoperation展示影片：https://youtu.be/drOwT_HPe_k 
*	[註5-5] collision avoidance展示影片：https://youtu.be/Nho1wcHwQUM
*	[註5-6] Road following展示影片：https://youtu.be/8vN29tz4omg
*	[註5-7] Jetbot功能展示影片：https://youtu.be/UCHx_tT2x98
*	[註5-8] Jetbot原廠硬體清單：https://github.com/NVIDIA-AI-IOT/jetbot/wiki/bill-of-materials
*	[註5-9] RK-Jetbot 硬體清單：[請點我](#jetbot-材料表) 
*	[註5-10] Jetbot映像檔下載點：https://drive.google.com/file/d/1G5nw0o3Q6E08xZM99ZfzQAe7-qAXxzHN/view
*	[註5-11] Jupyter官方教學：https://jupyterlab.readthedocs.io/en/stable/ 
*	[註5-12] basic_motion.ipynb: https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks_CAVEDU/basic_motion/basic_motion.ipynb
*	[註5-13] teleoperation.ipynb: https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks/teleoperation/teleoperation.ipynb
*	[註5-14] HTML5 Gamepad Tester搖桿偵測網站：http://html5gamepad.com

**第六章：JetBot深度視覺機器人**
*	[註6-1] 什麼是深度學習：https://blogs.nvidia.com/blog/2015/02/19/deep-learning-2/ 
*	[註6-2] AI、機器學習與深度學習的差異：https://blogs.nvidia.com/blog/2016/07/29/whats-difference-artificial-intelligence-machine-learning-deep-learning-ai/ 	
*	[註6-3] 深度學習訓練與推論 https://blogs.nvidia.com/blog/2016/08/22/difference-deep-learning-training-inference-ai/
*	[註6-4] 障礙迴避專案資料夾：https://github.com/NVIDIA-AI-IOT/jetbot/tree/master/notebooks/collision_avoidance
*	[註6-5] 障礙迴避執行影片：
*	[註6-6] pytorch：https://pytorch.org/
*	[註6-7] alexnet神經網路：http://www.cs.toronto.edu/~kriz/imagenet_classification_with_deep_convolutional.pdf
*	[註6-8] ImageNet影像資料集：http://www.image-net.org/
*	[註6-9] 道路跟隨專案資料夾：https://github.com/NVIDIA-AI-IOT/jetbot/tree/master/notebooks/road_following
*	[註6-10]道路跟隨影片：https://youtu.be/8vN29tz4omg
*	[註6-11]ResNet-18神經網路：https://pytorch.org/hub/pytorch_vision_resnet/

**第七章：Intel RealSense 深度視覺攝影機**
*	P229 安裝RealSenseviewer套件網址部分有更改(更改教學如下):https://blog.cavedu.com/2021/07/12/realsense/
*	[註7-1] Intel RealSense: https://www.intelrealsense.com/ ; https://www.intel.com.tw/content/www/tw/zh/architecture-and-technology/realsense-overview.html
*	[註7-2] Intel RealSense D435景深攝影機：https://www.intelrealsense.com/depth-camera-d435/
*	[註7-3] JetsonHacksNano: https://github.com/JetsonHacksNano
*	[註7-4] Intel RealSense SDK 安裝須知: https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_jetson.md  (網址已更新)
*	[註7-5] RealSense Viewer: https://www.intelrealsense.com/sdk-2/
*	[註7-6] RealSense code example:  https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python/examples 
*	[註7-7] Pyrealsense2: https://intelrealsense.github.io/librealsense/python_docs/_generated/pyrealsense2.html
*	[註7-8] 顏色格式： http://docs.ros.org/en/kinetic/api/librealsense/html/namespacers.html
*	[註7-9] 假彩色：https://docs.opencv.org/3.4/d3/d50/group__imgproc__colormap.html
*	[註7-10] Haar cascade classifier檔案下載： https://github.com/opencv/opencv/tree/master/data/haarcascades
*	[註7-11] OpenCV Cascade Classifier語法說明：https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

