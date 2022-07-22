from pyzipcode import ZipCodeDatabase
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
from flask import Flask, jsonify, request, make_response


app = Flask(__name__)


@app.errorhandler(Exception)
def no_zipcode(e):
    return {"Error": "No zip code was given"}


@app.errorhandler(Exception)
def bad_zipcode(e):
    return {"Error": "Bad zip code was given"}


def zip_code_check(zipcode):
    for numbers in zipcode:
        try:
            if 0 <= int(numbers) <= 9:
                return False
        except ValueError:
            return True


@app.route('/ZipToTime', methods=['GET'])
def ZipcodeToTime():
    zipcode = request.args.get('zipcode')
    if not zipcode:
        raise no_zipcode()
    elif len(zipcode) != 5 or zip_code_check(zipcode):
        raise bad_zipcode()

    # convert zipcode to  lat and long
    zcbd = ZipCodeDatabase()
    latitude = zcbd[zipcode].latitude
    longitude = zcbd[zipcode].longitude

    # get timezone for lat and long
    obj = TimezoneFinder()
    timezone = obj.timezone_at(lng=longitude, lat=latitude)

    # get time and date from timezone
    location_time = datetime.now(pytz.timezone(timezone))
    response = make_response(jsonify({'time': str(location_time.strftime("%H:%M"))}))
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    app.run()