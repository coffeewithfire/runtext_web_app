import cv2
import numpy as np

def create_video(message: str) -> None:

    width, height = 100, 100    #window dimensions
    fps = 24    #frames per second
    time = 3    #video duration in sec

    #video parameters
    out = cv2.VideoWriter(f"runtext/utils/video/{message}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    #black background frame
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    #start pos
    x, y = width, height // 2

    #font parameters
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    #for each frame
    for t in range(fps * time):
        #clear frame
        frame.fill(0)

        #set new x coordinates
        x -= len(message) // 2

        #add text to the frame
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        #record frame
        out.write(frame)

    out.release()