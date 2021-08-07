import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

########### INPUT PARAMETERS ###################
## Details
try:
    from dev_settings import *
except:
    pass

########### VCARD ###################
input_data = '''BEGIN:VCARD

VERSION:3.0

N:''' + N + '''

FN:''' + FN + '''

ORG:''' + ORG + '''

EMAIL:''' + EMAIL + ''' 

TEL;TYPE=voice,work,pref:''' + phone + '''

X-SOCIALPROFILE;type=twitter;x-user=''' + twitter + twitter_url + '''

X-SOCIALPROFILE;type=linkedin;x-user=''' + linkedin + linkedin_url + '''

PHOTO;VALUE=URL;TYPE=JPEG:''' + pic + '''

END:VCARD '''

########### QRCODE ###################
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer(), fill='black', back_color='white')
img.save('vr_qrcode001.png')