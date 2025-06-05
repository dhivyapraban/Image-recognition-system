# Image-recognition-system
This project encloses with the image recognising system by uploading a image in website , the system shows the identified objects  image within the website .

 • This runs on a yolov8n model so you need to download the file from the ultralytics github repository and put the file in the same folder where static , main.py files are present.

• Make sure that you give the path in the main.py file.

• Used Packages are 

    Packages                         Preinstalled?	                    Pip install command

    fastapi	                            ❌ No	                       pip install fastapi
    uvicorn (needed to run FastAPI)	    ❌ No	                       pip install "uvicorn[standard]"
    ultralytics	                        ❌ No	                       pip install ultralytics
    cv2 (OpenCV)	                      ❌ No	                       pip install opencv-python
    shutil	                            ✅ Yes (Standard library)	            —
    os	                                ✅ Yes (Standard library)	            —

• Though we need a backend to run, since we host in website so we use terminal, 
   open terminal(Microsoft powershell) and run the command uvicorn main:app --reload

• After succesfull run ,use the local url that have given.
