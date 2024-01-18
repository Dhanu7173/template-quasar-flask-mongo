import re
from bleach import clean
import imghdr
from werkzeug.utils import secure_filename
from os.path import splitext

def regex_validator(value, pattern):
    return re.match(pattern, value)

def length_validator(value, limits:tuple):
    return len(value) < limits[0] or len(value) > limits[1]

def sanitize(data):
    return clean(data)

def validate_image_format(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

def validate_filename(file, allowed_extensions=['.jpg', '.jpeg']):
    filename = secure_filename(file.filename)
    if(filename != '' and splitext(filename)[1] not in allowed_extensions or splitext(filename)[1] != validate_image_format(file.stream)):
        return True
    else:
        return False

