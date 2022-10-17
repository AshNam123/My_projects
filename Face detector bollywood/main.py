# !pip install mtcnn==0.1.0
# !pip install tensorflow==2.3.1
# !pip install keras==2.4.3
# !pip install keras-vggface==0.6
# !pip install keras_applications==1.0.8

# import os
# import pickle
# actors = os.listdir('data')
# #print(actors)
#
# filenames=[]
# for actor in actors:
#     for file in os.listdir(os.path.join('data',actor)):
#         filenames.append(os.path.join('data',actor,file))
#
# pickle.dump(filenames,open('filenames.pkl','wb'))

from tensorflow.keras.preprocessing import image
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
import numpy as np

import pickle
filenames = pickle.load(open('filenames.pkl','rb'))

model = VGGFace(model='resent50',include_top = False,input_shape=(224,224,3),pooling='avg')
print(model.summary())