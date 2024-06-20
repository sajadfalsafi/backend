import joblib
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CancerDataSerializer
from sklearn.preprocessing import LabelEncoder
import os

class CancerDataView(APIView):
    def post(self, request):
        serializer = CancerDataSerializer(data=request.data)
        if serializer.is_valid():
            # Convert the validated data to a DataFrame
            input_data = pd.DataFrame([serializer.validated_data])

            # One-hot encode the GENDER field to match training data
            input_data = pd.get_dummies(input_data, columns=['GENDER'])

            # Ensure the one-hot encoding columns match those used in training
            for column in ['GENDER_F', 'GENDER_M']:
                if column not in input_data.columns:
                    input_data[column] = 0

            # Load the model
            current_directory = os.getcwd()
            model_path = os.path.join(current_directory, 'apps', 'cancer', 'ml_model.pkl')
            model = joblib.load(model_path)
            # model = joblib.load('apps/cancer/ml_model.pkl')

            # Ensure input data columns match model's feature names
            missing_cols = set(model.feature_names_in_) - set(input_data.columns)
            for col in missing_cols:
                input_data[col] = 0
            input_data = input_data[model.feature_names_in_]

            # Make prediction
            prediction = model.predict(input_data)

            # Convert numerical prediction back to original labels
            label_encoder = LabelEncoder()
            label_encoder.fit(['NO', 'YES'])  # Assuming these were the original labels
            predicted_labels = label_encoder.inverse_transform(prediction)
            
            return Response({'prediction': predicted_labels[0]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
