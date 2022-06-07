import cv2
import os

is_using_multi_video = True

video_folder = 'dataset_video/alex'
image_folder = 'dataset_image/alex'

delay_speed = 100

for filename in os.listdir(video_folder):
    f = os.path.join(video_folder, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)

        cap = cv2.VideoCapture(f)
        counter_img = 0

        counter_error = 0

        while True:
            # print(delay_speedb)
            ret_, img = cap.read();

            if not ret_:
                counter_error += 1

                if counter_error >= 20:
                    break
                else:
                    continue
            else:
                counter_error = 0

            cv2.imshow("raw", img)

            res = cv2.waitKey(delay_speed)

            filename_img = os.path.join(image_folder, filename[:-5])

            if res == ord('q'):
                break
            elif res == ord('c'):
                print("capture", filename_img + ".png")

                cv2.imwrite(filename_img + str(counter_img) + ".png", img)
                counter_img += 1
            elif res == ord('f'):
                delay_speed -= 10
                if(delay_speed<=0):
                    delay_speed = 1
                print("SPEED UP", delay_speed)
            elif res == ord('b'):
                delay_speed += 10
                print("SPEED DOWN", delay_speed)
