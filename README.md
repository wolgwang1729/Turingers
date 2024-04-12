# Turingers

## This project aims at providing early diagnosis for various crop diseases, through a Flask-based web app, using Tensorflow Convolution Neural Network, and a responsive interface created in HTML5, CSS3, JavaScript.

This dataset contains the combination of :

1.) Dataset for Crop Pest and Disease Detection (https://data.mendeley.com/datasets/bwh3zbpkpv) (400,400,3)

2.) Kaggle paddy contest (https://www.kaggle.com/c/paddy-disease-classification/) (480,640,3)

It in total has 32 categories with disease of Cashew, Cassava, Maize, Tomato, Rice with each split into training and test(90%/10%)

## Kaggle link: https://www.kaggle.com/code/wolgwang/turingers/

The model has been set for training, and will take some time to train. What we intend to implement is, taking the affected plant image from user through an HTMl form, which is fed as input to the pre-trained model in Flask app, and the output of model (i.e the prediction of disease) is used to to redirect to a special page made for that disease, providing the recommended remedies, and pesticides to save the crop.
