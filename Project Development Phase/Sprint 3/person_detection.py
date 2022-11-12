{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNSMono-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red190\green199\blue208;\red189\green198\blue208;
\red12\green14\blue18;\red109\green109\blue109;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c78933\c82075\c85114;\cssrgb\c78824\c81961\c85098;
\cssrgb\c5098\c6667\c9020;\cssrgb\c50196\c50196\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clmrg \clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 import cv2\cell 
\pard\intbl\itap1\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 import os\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 import numpy as np\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 from .utils import download_file\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 initialize = True\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 net = None\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 dest_dir = os.path.expanduser(\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     '~') + os.path.sep + '.cvlib' + os.path.sep + 'object_detection' + os.path.sep + 'yolo' + os.path.sep + 'yolov3'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 classes = None\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 COLORS = [1, 1, 255], [255, 1, 1]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 def populate_class_labels():\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     class_file_name = 'yolov3_classes.txt'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     class_file_abs_path = dest_dir + os.path.sep + class_file_name\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     url = 'https://raw.githubusercontent.com/IBM-EPBL/IBM-Project-44424-1660724647/main/Project%20Development%20Phase/Sprint%203/yolov3.txt'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     if not os.path.exists(class_file_abs_path):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         download_file(url=url, file_name=class_file_name, dest_dir=dest_dir)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     f = open(class_file_abs_path, 'r')\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     classes = [line.strip() for line in f.readlines()]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     return classes\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 def get_output_layers(net):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3    \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     layer_names = net.getLayerNames()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     return output_layers\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 def draw_bbox(img, bbox, labels, confidence, Drowning, write_conf=False):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     global COLORS\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     global classes\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     if classes is None:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         classes = populate_class_labels()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     for i, label in enumerate(labels):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         # if the person is drowning, the box will be drawn red instead of blue\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         if label == 'person' and Drowning:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             color = COLORS[0]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             label = 'DROWNING'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         else:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             color = COLORS[1]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         if write_conf:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             label += ' ' + str(format(confidence[i] * 100, '.2f')) + '%'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         # you only need to points (the opposite corners) to draw a rectangle. These points\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         # are stored in the variable bbox\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         cv2.rectangle(img, (bbox[i][0], bbox[i][1]), (bbox[i][2], bbox[i][3]), color, 2)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         cv2.putText(img, label, (bbox[i][0], bbox[i][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     return img\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 def detect_common_objects(image, confidence=0.5, nms_thresh=0.3):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     Height, Width = image.shape[:2]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     scale = 0.00392\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     global classes\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     global dest_dir\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     config_file_name = 'yolov3.cfg'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     config_file_abs_path = dest_dir + os.path.sep + config_file_name\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     weights_file_name = 'yolov3.weights'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     weights_file_abs_path = dest_dir + os.path.sep + weights_file_name\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     url = 'https://raw.githubusercontent.com/IBM-EPBL/IBM-Project-44424-1660724647/main/Project%20Development%20Phase/Sprint%203/yolov3.cfg'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     if not os.path.exists(config_file_abs_path):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         download_file(url=url, file_name=config_file_name, dest_dir=dest_dir)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     url = 'https://pjreddie.com/media/files/yolov3.weights'\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     if not os.path.exists(weights_file_abs_path):\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         download_file(url=url, file_name=weights_file_name, dest_dir=dest_dir)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     global initialize\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     global net\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     if initialize:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         classes = populate_class_labels()\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         net = cv2.dnn.readNet(weights_file_abs_path, config_file_abs_path)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         initialize = False\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     net.setInput(blob)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     outs = net.forward(get_output_layers(net))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     class_ids = []\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     confidences = []\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     boxes = []\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     for out in outs:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         for detection in out:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             scores = detection[5:]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             class_id = np.argmax(scores)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             max_conf = scores[class_id]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3             if max_conf > confidence:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 center_x = int(detection[0] * Width)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 center_y = int(detection[1] * Height)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 w = int(detection[2] * Width)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 h = int(detection[3] * Height)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 x = center_x - w / 2\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 y = center_y - h / 2\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 class_ids.append(class_id)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 confidences.append(float(max_conf))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3                 boxes.append([x, y, w, h])\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence, nms_thresh)\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     bbox = []\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     label = []\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     conf = []\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     for i in indices:\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         i = i[0]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         box = boxes[i]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         x = box[0]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         y = box[1]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         w = box[2]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         h = box[3]\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         bbox.append([round(x), round(y), round(x + w), round(y + h)])\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         label.append(str(classes[class_ids[i]]))\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3         conf.append(confidences[i])\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat5 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1883\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth17609\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sl400\qr\partightenfactor0
\cf2 \strokec3 \cell 
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0
\cf2 \strokec3     return bbox, label, conf\cell \lastrow\row
}