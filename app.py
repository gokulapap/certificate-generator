from flask import Flask, render_template, send_file, url_for
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

font = ImageFont.truetype("arial.ttf", 50)

app = Flask(__name__)

@app.route("/")
def hello():
	return '''
	<center>
	<u><h1>Certificate Generator</h1></u>
	<br><br>

	<h3>Add this to the URL to generate your certificate <br><br> /certificate/{name}</h3>

	</center>
	'''

# add your app url in the above content 

@app.route("/certificate/<name>")
def certificate(name):
	img = Image.open('/app/certificate.jpg')
	W = img.size[0]
	draw = ImageDraw.Draw(img)
	w, h = draw.textsize(name)
	draw.text(xy=((W-w)/2 + w/2 + 10, 410),text='{}'.format(name), fill=(0,0,0), font=font, anchor="ms")
	# must add the absolute path of the folders
	img.save('/app/static/images/{}.jpg'.format(name))
	f = open("/app/templates/{}.html".format(name), "w")
	f.write('''
	<html>
	<head>
	</head>
	<body>
	<br><br><br>
	<center>
	<img style="max-width: 99%; max-height: 99%;" src="/static/images/{}.jpg">
	</center>
	</body>
	</html>
	'''.format(name))
	f.close()
	return render_template("{}.html".format(name))

if __name__ == "__main__":
	app.run(port=5000)


