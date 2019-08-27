from imagescrapper import download_images
from train_model import train_model
# download_images("cats", "Animals")


train_model("model_definition.yaml", ".","csvfile.csv", "TestExp", "log.txt")