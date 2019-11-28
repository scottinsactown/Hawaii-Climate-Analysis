import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start_end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """  Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
         Return the JSON representation of the dictionary. Instructions don't say but assuming for a year from the          last data point"""
    
    # Query past year precipitation
    start_date = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date,Measurement.prcp)\
    .filter(Measurement.date > start_date).order_by(Measurement.date).all()
                                                                      
    session.close()

    # Create a dictionary from the row data
    all_precip = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        all_precip.append(precip_dict)

    return jsonify(all_precip)    

@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset"""
    # Query all passengers
    results = session.query(Station.name).all()
    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def temps():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Query for the dates and temperature observations from a year from the last data point.
       Return a JSON list of Temperature Observations (tobs) for the previous year."""

    # Query past year precipitation
    start_date = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date,Measurement.tobs)\
    .filter(Measurement.date > start_date).order_by(Measurement.date).all()
                                                                      
    session.close()

    # Create a dictionary from the row data
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["prcp"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)    
    
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a            given start or start-end range.
       When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to          the start date."""
#     start_date = dt.datetime(2017, 8, 23)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    return jsonify(results)
    
@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a            given start or start-end range.
       When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the            start and end date inclusive."""
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    return jsonify(results)
    
if __name__ == '__main__':
    app.run(debug=True)
