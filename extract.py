import cv2

## your var ##
input_file = './test.mp4'
output_file = './frame_%d.jpg'
num_frames = 50
interval_min = 2
##############

counter = 0
seek_where = 0

# read first frame
vidcap = cv2.VideoCapture(input_file)
success, image = vidcap.read()
fps = vidcap.get(cv2.CAP_PROP_FPS)
print(
    "Frames per second: {0}".format(fps))
# write output and extract more frames
while success:
    cv2.imwrite((output_file) % counter, image)
    success, image = vidcap.read()
    counter += 1
    seek_where += int(fps) * 60 * interval_min
    vidcap.set(1, seek_where)

    # break after reading enough frames
    if(counter >= num_frames):
        break
