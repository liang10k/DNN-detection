# DNN-detection
---

## prototype model from Tensorflow
models folder can be found :   
https://github.com/tensorflow/models/tree/master/research/object_detection

---
errors during Protobuf Compilation with command : $ protoc is not found 
`protoc object_detection/protos/*.proto --python_out=.`

For Mac OS system : try commands in terminal below :

`brew install automake`

`brew install libtool`

`brew install protobuf`

---
## Run object_detection.jpyn
Must run the object_detection.jpyn file in the models file or be careful of the import path to avoid import problems

---
## import Open Cv package

`pip install opencv-python`
if get error: image no found 

try other version of Open CV to match the operate system
`pip install opencv-python=={}`  {3.1.0.4;3.1.0.5;3.2.0.7;3.2.0.8;3.3.0.9;3.3.0.10;3.3.1.11;3.4.0.12}

---
there are still have problem in picture reshow 
---
