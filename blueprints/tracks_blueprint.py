from flask import Blueprint, render_template

from init_db import get_db_connection

tracks_blueprint = Blueprint('tracks', __name__)


@tracks_blueprint.route('/tracks')
def get_count_tracks():
    """Return the number of tracks in the database"""
    con = get_db_connection()
    count = con.execute('SELECT COUNT(*) FROM customers').fetchone()
    return render_template('tracks.html', title='Tracks Count', count=count[0])


@tracks_blueprint.route('/tracks-sec')
def get_all_tracks():
    """Return all tracks in the database"""
    con = get_db_connection()
    tracks = con.execute('SELECT track_name, duration FROM tracks').fetchall()
    tracks = [dict(track_name=row[0], duration=row[1]) for row in tracks]
    return render_template('all-tracks.html', title='Tracks', count=len(tracks), tracks=tracks)
