# Get meta information of images

### Tech Stack:
+ Python

### Libraries used:
+ requests
###  Pre-requirements:
+ Run `pip install -r requirements.txt`

### To execute the project:
+ Run `get_meta_from_pic.py`

### Note:
+ Make sure the picture contains location information, otherwise the location cannot be obtained
+ you need fill in your email address to use the function in gps_utils.py:
```python
geolocator = Nominatim(user_agent = "your email")
```
