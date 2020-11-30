### Problem01

1. ./datasets/ants/swiss-army-ant.jpg를 텐서플로우에서 불러와서 128x128 (rgb)로 resize하여라
2. 1번에서 resize한 이미지를 random_crop 64x64로 resize하여라 
3. 2번에서 resize한 이미지를 resize_with_pad를 통하여 128x128로 만들어라
4. 1, 2, 3번의 이미지를 matplot으로 출력하여라



### Problem 02

1. ./datasets/cifar10-py 밑에 있는 data_batch_{1~5}까지의 파일을 읽어라
2. tf.image의 아래의 함수를 참조 하여 Data Agument를 하여라
   - random_brightness
   - random_contrast
   - random_crop, resize
   - random_flip_left_right
   - random_flip_up_down
3. cifar10을  tfrecord파일로 만들어라
4. 간단한 cnn 모델을 작성하여 학습 하여라