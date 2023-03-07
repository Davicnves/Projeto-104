import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "sol",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )
cv2.putText(img,
            "mercurio",
            (110, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "venus",
            (190, 170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "terra",
            (290, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "marte",
            (380, 270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "jupiter",
            (480, 110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "saturno",
            (780, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "urano",
            (970, 140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "netuno",
            (1120, 140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow("resultado",img)

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)