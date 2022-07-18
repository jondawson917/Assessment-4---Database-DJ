"""Models for Playlist app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True, unique=True)
    # song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    # songs = db.relationship('Song', backref="playlists")
    # playlistsongs = db.relationship('PlaylistSong', backref='playlists')
    
    def __repr__(self):
        return f"<Playlist Id: {self.id} Name: {self.name} Description: {self.description}"

class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    artist = db.Column(db.Text, nullable=False, unique=True)
    
    
    # playlistsongs = db.relationship('PlaylistSong', backref='songs')

    
    def __repr__(self):
        return f"<Song Id: {self.id} Title: {self.title} Artist: {self.artist}"


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.id'), primary_key=True)

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
