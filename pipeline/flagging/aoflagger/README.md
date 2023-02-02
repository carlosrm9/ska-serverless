## Installation instructions

First, set up a virtual enviroment with

```
python3 -m venv <nameofvenv>
```

Then activate it and update pip, setuptools and wheel with

```
source <nameofvenv>/bin/activate
pip install -U pip wheel setuptools
```

Finally, install the stimela package:

```
pip install stimela
```

To install Aoflagger, run in the virtual enviroment the following 

```
stimela pull --cab-base cab/autoflagger
```
## Usage
To check the different possible parameters of Aoflagger, run

```
stimela cabs -i autoflagger
```

To run Aoflagger, you will need to specify its parameters in parameters.txt. After that, run

```
stimela run aoflager.py
```
