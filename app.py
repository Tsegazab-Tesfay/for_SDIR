from flask import Flask, render_template, requestimport jsonifyimport requestsimport pickleimport numpy as npimport sklearnfrom sklearn.preprocessing import StandardScalerapp = Flask(__name__)model = pickle.load(open("Model.pkl", "rb"))@app.route("/",methods=["GET"])def Home():    return render_template("SDIR.html")standard_to = StandardScaler()@app.route("/predict", methods=["POST"])def predict():        if request.method == "POST":        MMSI = int(request.form["MMSI"])        LAT = float(request.form["LAT"])        LON = float(request.form["LON"])        SOG = int(request.form["SOG"])        COG = int(request.form["COG"])        VESSELTYPE = request.form["VESSELTYPE"]                LENGTH = request.form["LENGTH"]        WIDTH = request.form["WIDTH"]        CARGO = request.form["CARGO"]                prediction = model.predict([[MMSI, LAT, LON, SOG,COG, VESSELTYPE, LENGTH, WIDTH, CARGO]])        return render_template("SDIR.html", prediction_text="Predicted HEADING IS: {}".format(prediction))    else:        return render_template("SDIR.html")if __name__=="__main__":    app.run(debug=True)