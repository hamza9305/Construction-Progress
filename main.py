import cv2
import numpy as np

# input
Video_in = "data\\formwork.mp4"

# output
Video_out = "output/progress.mp4"

# Video Settings
winName = 'output'

cv2.resizeWindow(winName, 500, 500)
cap = cv2.VideoCapture(Video_in)

fps = int(cap.get(cv2.CAP_PROP_FPS))
length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(3))
height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(Video_out, fourcc, fps, (width, height))

n_frame = 0
frames = []

#points for the region of interest
points = np.array([[293,511],[604,573],[663,313],[513,308]])

#limits for yellow pixels inside the region of interest
lb_yellow = [3, 35, 65]
ub_yellow = [35, 255, 255]

#limts for pixels that are not yellow inside the region of interest
lb_not_yelow = [10,45,145]
ub_not_yellow = [33,160,225]

def pixels_count(pixels_array, upper_bound, lower_bound):

    """Function to compare pixels with upper and lower bounds

    Parameters:
        pixels_array (array): Array of pixels inside the region of interest.
        upper_bound (list): A list of pixels values to be checked for upper bound
        lower_bound (list): A list of pixels values to be checked for lower bound
    Returns:
        pixel (int): Total number of pixels that lie within the range

   """
    pixel = 0
    for i in pixels_array:
        value = (i >= lower_bound).all() and (i <= upper_bound).all()
        if value == True:
            pixel += 1
        else:
            pass
    return pixel


while cap.isOpened():
    # get frame from video
    ret, frame = cap.read()
    print('video_progress: ', round(n_frame*100/length_video, 1), '%')

    try:
        #convert each frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #create a mask with the size of an image
        mask = np.zeros(frame.shape[:2], dtype=frame.dtype)

        #draw a polygon around the region of interest
        mask = cv2.fillPoly(mask,[points],(255,255, 255))

        #find pixels that are within the region of interest
        pixel_info = hsv[mask == 255]
        array = np.array(pixel_info)

        #checks for pixels that are roughly yellow
        pixel_yellow = pixels_count(array, ub_yellow, lb_yellow)
        complete = round(pixel_yellow/len(pixel_info) * 100)

        #checks for pixels that are not yellow
        pixel_not_yellow = pixels_count(array, ub_not_yellow,lb_not_yelow)
        incomplete = round(pixel_not_yellow/len(pixel_info) * 100)
        complete_inv = 100 - incomplete

        #compares for percentage of pixels that are not yellow
        if complete_inv >= complete:
            writer = str(incomplete)
        else:
            writer = str(complete)
        writer = writer + '% complete'

        font = cv2.FONT_HERSHEY_SIMPLEX
        if ret:
            cv2.putText(frame, writer, (350, 640), font, 2, (255, 255, 255), 2)
            out.write(frame)
            cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
            cv2.imshow('output', frame)
            if cv2.waitKey(1000) == ord('q'):
                break
        else:
            break
        n_frame += 1
    except:
        print('End of Video')
        exit(0)

cap.release()