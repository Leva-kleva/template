#!/bin/bash

# run: ./run.sh dataset_name mode model batch epochs

source ../venv/bin/activate

mode=$2

# config
dataset_name="$1"
root_path="./"
dataset_path="$root_path/dataset"
dataset_yaml="$dataset_path/$dataset_name/description.yaml"

start_model=$3"$(test -z "$3" && echo yolov8n.pt)"
imgsz=640
epochs=$5"$(test -z "$5" && echo 8)"
batch=$4"$(test -z "$4" && echo 16)"

output_name_model=$start_model'_e'$epochs'_b'$batch'_'$dataset_name

output_model="runs/detect/$output_name_model/weights/best.pt"

imgs_path="test_img"
imgs=`ls $imgs_path`


train(){
    echo "+++++++++ TRAINING MODE +++++++++"
    echo "+++ model:   $start_model"
    echo "+++ imgsz:   $imgsz"
    echo "+++ dataset: $dataset_yaml"
    echo "+++ epochs:  $epochs"
    echo "+++ batch:   $batch"
    echo "+++ output:  $output_model"
    echo ""

    echo "+++++ RUN TRAINING +++++"
    yolo task=detect mode=train model=$start_model imgsz=$imgsz data=$dataset_yaml epochs=$epochs batch=$batch name=$output_name_model

#    ln -s $output_model last.best.pt
#ultralytics export model=$path_to_model format=torchscript
    echo "++++++++ DONE +++++++++"
}

predict(){
    echo "+++++++++ PREDICT MODE +++++++++"
    echo "+++ model:     $output_model"
    echo "+++ imgs_path: $imgs_path"
    echo ""

    echo "+++++ RUN PREDICT +++++"

    yolo task=detect mode=predict model=$output_model source=$imgs_path show=False hide_labels=True save=True name=$output_name_model'_predict'

    echo "++++++++ DONE +++++++++"
}

if [ "$mode" == "" ]; then
    train
    predict
elif [ "$mode" == "train" ]; then
    train
elif [ "$mode" == "predict" ]; then
    predict
fi
