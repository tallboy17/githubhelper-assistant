---
repo: ageitgey/face_recognition
readme_filename: ageitgey_face_recognition_README.md
stars: 54971
forks: 13620
watchers: 54971
contributors_count: 49
license: MIT
Header 1: Face Recognition
Header 2: Features
---
#### Find faces in pictures  
Find all the faces that appear in a picture:  
![](  
```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
```  
#### Find and manipulate facial features in pictures  
Get the locations and outlines of each person's eyes, nose, mouth and chin.  
![](  
```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
```  
Finding facial features is super useful for lots of important stuff. But you can also use it for really stupid stuff
like applying digital make-up (think 'Meitu'):  
![](  
#### Identify faces in pictures  
Recognize who appears in each photo.  
![](  
```python
import face_recognition
known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
```  
You can even use this library with other Python libraries to do real-time face recognition:  
![](  
See this example for the code.