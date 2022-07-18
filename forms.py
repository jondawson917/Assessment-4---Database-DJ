"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Name", validators=[InputRequired(message="You must enter a name"), Length(min=1, max=20)])
    description = StringField("Description", validators=[InputRequired(message="You must enter a description"), Length(min=5, max=50, message="Description between 5 and 50 characters")]) 
    


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("title", validators=[InputRequired(message="You must enter a song"),Length(min=1, max=30)])
    artist = StringField("artist", validators=[InputRequired(message="You must enter an artist"), Length(min=1, max=20)])
    # Add the necessary code to use this form
    

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
