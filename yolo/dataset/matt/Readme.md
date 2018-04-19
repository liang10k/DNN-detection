## C extension 
`pip install -e .`
### if meet the problem blow 
C:\Users\mlapp\Downloads\darkflow-master>python setup.py build_ext --inplace
running build_ext
building 'darkflow.cython_utils.nms' extension
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools

### Double check if you have correctly install Cython
---
## train Tiny YOLO 1 model with pretrain weights and annotations 
`python flow --model cfg/tiny-yolo-voc-fs-1c.cfg --load bin/tiny-yolo-voc.weights --train --annotation annotations --dataset images --gpu 0.7 --epoch 400`

