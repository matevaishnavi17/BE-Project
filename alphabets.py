from playsound import playsound
import cv2


def sound(alpha):
    if(alpha=='A'):
        print('APPLE')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\A1.mp4')
        if(cap.isOpened() == False):
         print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50,150), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,0,255), 2, cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\A.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif(alpha=='B'):
        print('BALL')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\B.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\B.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif (alpha=='C'):
        print('CAT')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\C.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\C.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif (alpha=='D'):
        print('DOLPHIN')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\D.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\D.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif (alpha=='E'):
        print('ELEPHANT')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\E.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\E.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif (alpha=='F'):
        print('FISH')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\F.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\F.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif (alpha=='G'):
        print('GOAT')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\G.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\G.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif (alpha=='H'):
        print('HORSE')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\H.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\H.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif (alpha=='I'):
        print('ICECREAM')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\I.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\I.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif (alpha=='J'):
        print('JUG')
        cap = cv2.VideoCapture(r'C:\Users\Dell\RTSLD\audios\J.mp4')
        if (cap.isOpened() == False):
            print("Error opening video  file")

        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.putText(frame, 'Press Q to exit', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
            if ret == True:
                cv2.imshow('Frame', frame)
                playsound(r'C:\Users\Dell\RTSLD\audios\J.mp3')
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

