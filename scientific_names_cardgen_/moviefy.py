import cv2
import os

cards_dir = "cards"
image_files = sorted(
    [f for f in os.listdir(cards_dir) if f.endswith(".png")],
    key=lambda x: int(x.split('_')[1].split('.')[0])
)

first_image_path = os.path.join(cards_dir, image_files[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

output_path = "cards_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_path, fourcc, 1/2, (width, height))

for image_file in image_files:
    image_path = os.path.join(cards_dir, image_file)
    frame = cv2.imread(image_path)
    resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    video.write(resized_frame)

video.release()

print("VIDEO SAVED")
