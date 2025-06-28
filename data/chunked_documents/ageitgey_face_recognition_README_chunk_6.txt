---
repo: ageitgey/face_recognition
readme_filename: ageitgey_face_recognition_README.md
stars: 54971
forks: 13620
watchers: 54971
contributors_count: 49
license: MIT
Header 1: Face Recognition
Header 2: Usage
Header 3: Command-Line Interface
---
When you install `face_recognition`, you get two simple command-line
programs:  
* `face_recognition` - Recognize faces in a photograph or folder full for
photographs.
* `face_detection` - Find faces in a photograph or folder full for photographs.  
#### `face_recognition` command line tool  
The `face_recognition` command lets you recognize faces in a photograph or
folder full  for photographs.  
First, you need to provide a folder with one picture of each person you
already know. There should be one image file for each person with the
files named according to who is in the picture:  
!known  
Next, you need a second folder with the files you want to identify:  
!unknown  
Then in you simply run the command `face_recognition`, passing in
the folder of known people and the folder (or single image) with unknown
people and it tells you who is in each image:  
```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```  
There's one line in the output for each face. The data is comma-separated
with the filename and the name of the person found.  
An `unknown_person` is a face in the image that didn't match anyone in
your folder of known people.  
#### `face_detection` command line tool  
The `face_detection` command lets you find the location (pixel coordinatates)
of any faces in an image.  
Just run the command `face_detection`, passing in a folder of images
to check (or a single image):  
```bash
$ face_detection  ./folder_with_pictures/

examples/image1.jpg,65,215,169,112
examples/image2.jpg,62,394,211,244
examples/image2.jpg,95,941,244,792
```  
It prints one line for each face that was detected. The coordinates
reported are the top, right, bottom and left coordinates of the face (in pixels).  
##### Adjusting Tolerance / Sensitivity  
If you are getting multiple matches for the same person, it might be that
the people in your photos look very similar and a lower tolerance value
is needed to make face comparisons more strict.  
You can do that with the `--tolerance` parameter. The default tolerance
value is 0.6 and lower numbers make face comparisons more strict:  
```bash
$ face_recognition --tolerance 0.54 ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```  
If you want to see the face distance calculated for each match in order
to adjust the tolerance setting, you can use `--show-distance true`:  
```bash
$ face_recognition --show-distance true ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama,0.378542298956785
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person,None
```  
##### More Examples  
If you simply want to know the names of the people in each photograph but don't
care about file names, you could do this:  
```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/ | cut -d ',' -f2

Barack Obama
unknown_person
```  
##### Speeding up Face Recognition  
Face recognition can be done in parallel if you have a computer with
multiple CPU cores. For example, if your system has 4 CPU cores, you can
process about 4 times as many images in the same amount of time by using
all your CPU cores in parallel.  
If you are using Python 3.4 or newer, pass in a `--cpus ` parameter:  
```bash
$ face_recognition --cpus 4 ./pictures_of_people_i_know/ ./unknown_pictures/
```  
You can also pass in `--cpus -1` to use all CPU cores in your system.  
#### Python Module  
You can import the `face_recognition` module and then easily manipulate
faces with just a couple of lines of code. It's super easy!  
API Docs:   
##### Automatically find all the faces in an image  
```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image)

# face_locations is now an array listing the co-ordinates of each face!
```  
See this example
to try it out.  
You can also opt-in to a somewhat more accurate deep-learning-based face detection model.  
Note: GPU acceleration (via NVidia's CUDA library) is required for good
performance with this model. You'll also want to enable CUDA support
when compliling `dlib`.  
```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image, model="cnn")

# face_locations is now an array listing the co-ordinates of each face!
```  
See this example
to try it out.  
If you have a lot of images and a GPU, you can also
find faces in batches.  
##### Automatically locate the facial features of a person in an image  
```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

# face_landmarks_list is now an array with the locations of each facial feature in each face.
# face_landmarks_list[0]['left_eye'] would be the location and outline of the first person's left eye.
```  
See this example
to try it out.  
##### Recognize faces in images and identify who they are  
```python
import face_recognition

picture_of_me = face_recognition.load_image_file("me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
print("It's a picture of me!")
else:
print("It's not a picture of me!")
```  
See this example
to try it out.