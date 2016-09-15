# Simpsonator
Telegram bot to auto-make-send The Simpsons related memes.

## Installation

```
git clone https://github.com/nanocatdemen/simpsonator.git
```
```
$ sudo apt-get install python3-dev
$ sudo apt-get install python-pip
$ pip install virtualenv
```
```
$ virtualenv -p [python 3 interpreter] venv  
$ . venv/bin/activate
```
```
$ (venv) pip install -r requirements.txt
```

### OpenCV

Follow this guide: http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/

Note that on Step 3, you should use "git checkout 3.1.0" instead of 3.0.0 in both cases. Also note that when running "cmake" (last part of Step 3) you should change "OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules" for "OPENCV_EXTRA_MODULES_PATH=\<PATH WHERE YOU CLONED THE opencv_contrib\>/opencv_contrib/modules", although if you followed every step until here that folder should in fact be "~".

Lastly, on Step 4 you have to create the SymLink inside the virtualenv you are using for the project. This will work even if you choose to skip Step 2 and not use the virtualenv wrapper.
