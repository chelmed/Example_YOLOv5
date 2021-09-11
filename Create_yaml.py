# Create .yaml file 
import yaml
data_yaml = dict(
    train = '/content/drive/MyDrive/NFL_Helmet_Assignment_Yolo_v5/images/train',
    val = '/content/drive/MyDrive/NFL_Helmet_Assignment_Yolo_v5/images/valid',
    nc = 5,
    names = list(extra_df.label.unique())
)

with open('/content/drive/MyDrive/NFL_Helmet_Assignment_Yolo_v5/yolov5/data/data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)
    
%cat /content/drive/MyDrive/NFL_Helmet_Assignment_Yolo_v5/yolov5/data/data.yaml





