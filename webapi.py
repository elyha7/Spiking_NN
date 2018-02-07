#import cv2
from flask import Flask, render_template, Response
#from visual_api import mark_on_image,add_info_field,Face_info
import matplotlib.pyplot as plt
import io
from PIL import Image
from math import sin
import numpy as np
import time
TIMER=0
app = Flask(__name__)
def Start_web(): 
    values=[sin(i) for i in np.linspace(0,15,1000)]  
    buf = io.BytesIO()
    for i in range(1000):
        plt.plot(values[0:i*10+10])
        plt.savefig(buf, format='jpg')
        buf.seek(0)
        plt.clf()
        #assert success, 'Encode error'
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf.getvalue() + b'\r\n\r\n')
        time.sleep(0.1)
    buf.close()
    

@app.route('/')
def page():
    return Response(Start_web(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    #sin_values=[sin(i) for i in np.linspace(0,15,1000)]
    app.run(host='0.0.0.0',port =5003,debug=True) 