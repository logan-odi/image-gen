from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from io import BytesIO


app = Flask(__name__)
api = Api(app)

@app.route('/linkgen/get_image')
def get_image():
    event_name = request.args.get('name')
    event_time = request.args.get('time')
    event_link = request.args.get('code')
    img = Image.open('image.png')
    d1 = ImageDraw.Draw(img)
    d2 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('font/pnb.otf', 80)
    myFont2 = ImageFont.truetype('font/pnf.otf', 70)
    myFont3 = ImageFont.truetype('font/pnf.otf', 50)
    d1.text((875, 350), event_name, font=myFont, fill =(255, 255, 255))
    d2.text((890, 505), event_time, font=myFont2, fill =(255, 255, 255))
    d2.text((890, 650), "swiftbot.io/join/" + event_link, font=myFont3, fill =(255, 255, 255))
    img.save("swiftbot.io_" + event_name + event_time + ".png")    
    filename = ("swiftbot.io_" + event_name + event_time + ".png")
    return send_file(filename)
    
if __name__ == '__main__':
     app.run(port='4002')
     
