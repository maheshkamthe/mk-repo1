#!/bin/bash

echo "**********************************"
echo "usage: ./test.sh filepath/filename"
echo "*******************************8**"

cp ~/flower_training_bkp/out* /tmp
source ~/venv2-python27/bin/activate
cd ~/venv2-python27/tensorflow/
bazel-bin/tensorflow/examples/label_image/label_image --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --output_layer=final_result --image=$1 --input_layer=Mul
