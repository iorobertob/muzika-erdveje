# -*- coding: utf-8 -*-
from    __future__      import unicode_literals
from    flask           import Flask, render_template, json, request, redirect, session, abort, jsonify
from    io_lib          import io_debug
import  os
import  re
import  uuid
import  argparse
import  flask
import  logging

# Private key is not shared
compendium_credentials = "keykeykeykey"
private_key = "keykeykeykey"

# server
artists_table    = "git/static/texts/artists_table.csv"
timetable_table  = "git/static/texts/timetable.csv"
images_path      = "git/static/javy/"
# local
# artists_table   = "static/texts/artists_table.csv"
# timetable_table = "static/texts/timetable.csv"
# images_path     = "static/javy/"

# This is necessary for the connection to mysql to support special characters
import sys
from re import search

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/Uploads'
# app.secret_key = compendium_credentials.app_secret_key
app.secret_key = private_key
app.debug = True

# ################################################# MAIN  ###########################
@app.route('/')
@app.route('/home')
def main():

    try:
        return render_template('index.html')

    except Exception as e:
        return str(e) 

    
# ################################################# MAIN  ###########################


# Start:
# This part is completly ignored by google cloud.
# Just use it for local development.
# Google clound only needs the methods and line 20 to run.
if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()

    args_parser.add_argument(   "-d",
                                "--debug",
                                help="print debug statements",
                                action="store_true",
                                default = False)

    args = args_parser.parse_args()

    IO_DEBUG = args.debug

    io_print = io_debug.io_debug(IO_DEBUG, None).io_print

    app.run(host='0.0.0.0',port=5665)
