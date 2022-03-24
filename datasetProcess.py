import cv2
import pandas as pd


def main():
    topFilePath = '/home/nab/Desktop/nabang1010/OxfordTownCenterDataset/dataset/TownCentre-groundtruth.top'
    vidPath = '/home/nab/Desktop/nabang1010/OxfordTownCenterDataset/dataset/TownCentreXVID.mp4'
    df =  pd.read_csv(topFilePath)
    print(df.info())
    # frameArr = df.loc[0]['frameNumber']
    
    # bodyLeftArr = df.loc[:][8]
    # bodyTopArr = df.loc[:][9]
    # bodyRightArr = df.loc[:][10]
    # bodyBottomArr = df.loc[:][11]
    # for frameID in frameArr:
    #     print(frameID)
    
    
    # print(frame)
        # print(bodyLeft)
        # print(bodyTop)
        # print(bodyRight)
        # print(bodyBottom)

    frameCount = 0
    cap = cv2.VideoCapture(vidPath)
    if cap.isOpened() == False:
        print('Error loading video')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frameCount += 1
            frameData = df.loc[df['frameNumber'] == frameCount]
            # print(frameData)
            for i in range (frameData.shape[0]):
                bodyLeft = frameData.iloc[[i],[8]]
                bodyTop = frameData.iloc[[i],[9]]
                bodyRight = frameData.iloc[[i],[10]]
                bodyBottom = frameData.iloc[[i],[11]]
                print(type(bodyLeft))
                frame = cv2.rectangle(frame, (int(bodyLeft),int(bodyTop)),(int(bodyRight),int(bodyBottom)), (255, 0, 0), 1)
            cv2.imshow('Video Strean', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()




    print('Main function run')

if __name__ == '__main__':
    main()