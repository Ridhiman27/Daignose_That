### Daignose_That
Disease prediction systems allow medical practitioners to intervene early and prevent chronic  illness by identifying people who are at risk. Our web app aims to predict whether the user has a certain disease or not. The prediction  has been done on the basis of general questions asked in the form of multiple-choice  questions.  Alzheimer and Tuberculosis models are also based on the X-ray and scan images provided by  the users. 
### Scope
The user can choose among 6 diseases and on choosing a certain disease general information 
about that disease and informative facts are provided to the user. 
The 6 diseases which we have included in our website are:
1. Lung Cancer 
2. Heart diseases
3. Diabetes 
4. Urinary Inflammation 
5. Alzheimer’s 
6. Tuberculosis (TB)

### Architecture Design
• Initially on the introduction page the user has to give a short questionnaire where some basic 
questions age and gender are asked and it’s users option to give the details.
• The user can select any of the disease for which either the user will have to upload his/her xray scan or will have to give a questionnaire. There will be total 6 diseases out of which 
Alzheimer, tuberculosis will take image as input from the user and diabetes, lung cancer, heart 
disease, urinary disease will be a questionnaire for the user. 
• And after the prediction is made a recommendation will be made and solution and remedies 
will be displayed for the user.
![image](https://user-images.githubusercontent.com/93005927/226123830-a8dcc6fb-4e84-4992-8ac5-036be44d27ff.png)

### Hardware and software requirements
Procurement of hardware for using the system is OUT OF SCOPE of this project and only software has been used and implemented.

### Working flow of the website
• The user interacts with our landing page containing an optional questionnaire. If the user skips this questionnaire they are asked to choose 1 of 6 diseases for which they want to get tested.
![image](https://user-images.githubusercontent.com/93005927/226124337-6fd41b34-881f-457d-b13f-c3ff31078253.png)

• After filling the basic details user is redirected to choose one of the 6 diseases and get 
himself/herself tested.
• Here the user can choose one of the diseases to get tested.

![image](https://user-images.githubusercontent.com/93005927/226124482-1bda5acc-f9e3-4bd6-bd2c-968555173207.png)

• After the user chooses which diseases they want to get tested for, they need to answer certain 
medical questions or upload relevant medical imaging information. 
For example, the webpage of Alzheimer disease is shown below

![image](https://user-images.githubusercontent.com/93005927/226128051-f9e77ed6-a881-4303-a6ab-d00827a27b30.png)

### Output Predictions
![image](https://user-images.githubusercontent.com/93005927/226128212-cc8c904e-fa9e-4c89-9dbb-6bb5d7ae96b4.png)

### Model Building  
The model was built using the following steps:
We used transfer learning using inception v3 for image classification. When we have a 
relatively small dataset, a super-effective technique is to use Transfer Learning where we use 
a pre-trained model. This model has been trained on an extremely large dataset, and we would 
be able to transfer weights which were learned through hundreds of hours of training on 
multiple high-powered GPUs. Many such models are open-sourced such as VGG-19 and 
Inception-v3. They were trained on millions of images with extremely high computing power 
which can be very expensive to achieve from scratch.
The next step was to add new trainable layers that will turn old features into predictions on 
the new dataset. This is important because the pre-trained model is loaded without the final 
output layer.
The pre-trained model’s final output will most likely be different from the output that we want 
for your model.
Therefore, we added some new dense layers as you please, but most importantly, a final dense 
layer with units corresponding to the number of outputs expected by your model.
To train the convolution neural network, we used keras library from tensorflow. For 
compiling it, we used binary crossentropy as the loss parameter.
Then for fitting the model, we initialised 10 epochs

### Future scope:
• A feature can be added that will help you find the nearest doctor by taking the user’s area 
Pincode.
• To make chatbots for interaction with user such that when user comes on our website he can 
navigate and get his answers quickly.

### Acknowledegments:
We would like to thank Dr Uday Joshi and our HOD, Dr. Deepak Sharma, of our college, for 
their cooperation in completing our project on the topic Diagnose That.
We would like to take this opportunity to express our gratitude to all of of our group members 
• Ridhiman Dhariwal
• Shruti Tyagi
• Pyanshi Jain
• Varshaah Karkala



