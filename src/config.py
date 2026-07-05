import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_DIR = os.path.join(BASE_DIR, "data", "Training")
TEST_DIR = os.path.join(BASE_DIR, "data", "Testing")

IMG_SIZE = 64
RANDOM_STATE = 42