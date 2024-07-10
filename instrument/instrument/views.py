from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Img_predictions
from .models import Instrument
from .serializers import ImgPredictionsSerializer
from ultralytics import YOLO
import cv2
import numpy as np
from numpy import argmax
import tensorflow as tf

class InstrumentList(APIView):
    def get(self, request, *args, **kwargs):
        # Truy vấn tất cả các nhạc cụ từ cơ sở dữ liệu
        instruments = Instrument.objects.all()
        # Chuẩn bị dữ liệu để trả về dưới dạng JSON
        data = []
        for instrument in instruments:
            data.append({
                'name': instrument.name,
                'description': instrument.description,
            })
        # Trả về JSON response
        return Response(data, status=status.HTTP_200_OK)

class ImageDetectAPI(APIView):

    def post(self, request, *args, **kwargs):
        image_input = request.FILES.get('image_input')

        if not image_input:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        img = Img_predictions.objects.create(image=image_input)
        img.save()

        list_img, cl_out = self.detect_img(img.image.path)
        output = [f'predict/image_{i:03d}.jpg' for i in range(list_img)]

        return Response({'output': output, "cl_o": cl_out})

    def detect_img(self, path_img):
        model = YOLO("E:/Báo Cáo Khoa Học/CODE/instrument/model/model_yolo/best.pt")
        img_input = cv2.imread(path_img)
        rs = model.predict(source=img_input)
        rs = rs[0]
        i = 0
        listImg = []
        class_out = []
        for ob in rs.boxes:
            box = ob.xyxy[0].tolist()
            box = [round(x) for x in box]
            x1, y1, x2, y2 = box
            conf = ob.conf[0].item()
            img_cut = img_input[y1:y2, x1:x2]
            listImg.append(img_cut)
            cv2.imwrite(f'instrument/static/predict/image_{i:03d}.jpg', img_cut)
            i += 1

        for t in range(len(listImg)):
            a = cv2.cvtColor(listImg[t], cv2.COLOR_RGB2BGR)
            label = self.predict_lenet(a)
            # print(label)
            print(f"Label for image_{t:03d}: {label}")
            class_out.append(label)

        return i, class_out

    def predict_lenet(self, image):
        categories = ['cong_chieng', 'dan_bau', 'dan_co', 'dan_da', 'dan_day', 'dan_nguyet', 'dan_sen', 'dan_t_rung', 'dan_tinh', 'dan_tranh', 'dan_ty_ba', 'guitar', 'khen', 'trong_quan']
        model_lenet = tf.keras.models.load_model("E:/Báo Cáo Khoa Học/CODE/instrument/model/model_lenet/lenet_model30.h5")
        model_lenet.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])  # Compile the model
        img_input = cv2.resize(image, dsize=(64, 64))
        img_array = np.array(img_input)
        from tensorflow.keras.applications.resnet50 import preprocess_input
        img_batch = np.expand_dims(img_array, axis=0)
        img_preprocessed = preprocess_input(img_batch)
        pred = model_lenet(img_preprocessed)
        res = argmax(pred, axis=1)
        return categories[res[0]]
