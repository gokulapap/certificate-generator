from flask import Flask, render_template, send_file, url_for
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

font = ImageFont.truetype("arial.ttf", 50)

W = 1000

app = Flask(__name__)

@app.route("/")
def hello():
	return '''
	<center>
	<u><h1>Certificate Generator</h1></u>
	<br><br>

	<h3>Go to this URL to generate your certificate <br><br> https://certificate-creator.herokuapp.com/certificate/{name}</h3>

	</center>
	'''

@app.route("/certificate/<name>")
def certificate(name):
	img = Image.open('/home/pagania/remove/certi_gen/certificate.jpg')
	draw = ImageDraw.Draw(img)
	w, h = draw.textsize(name)
	draw.text(xy=((W-w)/2 - w/2,360),text='{}'.format(name),fill=(0,0,0),font=font)
	img.save('/home/pagania/remove/certi_gen/static/images/{}.jpg'.format(name))
	f = open("/home/pagania/remove/certi_gen/templates/{}.html".format(name), "w")
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
#	return send_file("/home/pagania/remove/certi_gen/templates/{}.jpg".format(name), as_attachment = True)
	return render_template("{}.html".format(name))

if __name__ == "__main__":
	app.run(port=5000)


