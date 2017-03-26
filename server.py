from flask import Flask, Response, render_template, request, redirect, url_for
from sqldb import db 
import simplejson as json



app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
  hotel = 'living' 
  return render_template('home.html', hotel=hotel)

@app.route('/hotel_view',methods=['POST','GET'])
def view_hotel_vr():
  hotel_name  = (request.args.get(('hotel_name')))
  print hotel_name
  data_dict = {'Hotel Seccy': 'western', 'Leonardo Da Vinci Rome Airport': 'zodiacHotel', 'Hotel Tiber': 'hotel2', 'Golden Tulip Rome Airport  Isola Sacra': 'hotel3', 'Hilton Airport Rome': 'living'}
  print data_dict[hotel_name]
  return render_template('index.html', hotel_name=data_dict[hotel_name])


@app.route('/hotel',methods=['POST','GET'])
def get_hotel():
  check_in  = (request.args.get(('check_in')))
  check_out  = (request.args.get(('check_out')))
  airport_code  = (request.args.get(('airport_code')))
  return render_template('hotels.html', check_in=check_in, check_out=check_out, airport_code=airport_code )

# @app.route('/hotel_name',methods=['POST','GET'])
# def get_hotel_name():
#   if request.method == 'POST':   
#   #   data = json.loads(request.form['hotelName'])
#   #   data_dict = {'Hotel Seccy': 'western', 'Leonardo Da Vinci Rome Airport': 'zodiacHotel'}
#   #   print data_dict[data]
#     print "dsfds" 
#     return redirect(url_for('.view_hotel_vr', hotel='dummy')) #data_dict[data])

@app.route('/test',methods=['POST','GET'])
def test():
  data = json.loads(request.form['json_data'])
  print data['270']
  db_instance = db()
  db.create(db_instance)
  db.insert(db_instance, data['hotel'], data['0'], data['90'], data['180'], data['270']) 
  db.close(db_instance)
  print 'db insert'
  return "done!"

@app.route('/analysis',methods=['POST','GET'])
def analysis():
  db_instance = db()
  result = db.select(db_instance)
  db.close(db_instance)
  data_dict = {'Hotel Seccy': 'western', 'Leonardo Da Vinci Rome Airport': 'zodiacHotel', 'Hotel Tiber': 'hotel2', 'Golden Tulip Rome Airport  Isola Sacra': 'hotel3', 'Hilton Airport Rome': 'living'}

  return render_template('analyse.html', result=result, data_dict=data_dict)

if __name__ == '__main__':
    app.run(debug=True,port=5000)