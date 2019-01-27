''''
cargoProtecTPro - Delta Hacks 5 2019
***************************************

Created BY: MOhammed Perves, Amanda Masjuwar, Jessica Li, Amanda Guo
'''
from dataset_generator import gen_data
from train_model import train_model
from face_recognition import recognize_faces
from human_detection import detect_humans


def dataset_generator():
    gen_data()
    return


def model_trainer():
    train_model()


def recognizer():
    recognize_faces()


def human_detector():
    detect_humans()


if __name__ == '__main__':
    # dataset_generator()
    # model_trainer()
    #recognizer()
    detect_humans()
