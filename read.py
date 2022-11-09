import cv2 as cv

# Reading Image
img = cv.imread('photos/cat_large2.jpg')
cv.imshow('Cat', img) #menampilkan gambar sebagai jendela baru
cv.waitKey(0)


# Reading Video
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()