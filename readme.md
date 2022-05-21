# Networking QR Code Generator 
## Motivation
Who wants to touch other people's phone to enter their information while exchanging contact information or business cards? 

This code will create a personal QR Code so you can have it on your phone and anyone you meeet can just scan it and it will automatically import your card into that person's contacts.

## Virtual Environment Requirements
pip install qrcode

pip instal pillow

## Other requirements
Make sure to create a dev_settings.py file with you VCARD information in the following format:

qr_prefix = "xx" #qr png file naming prefix

N = "LastName;FirstName"

FN = "FirstName" 

ORG = "Company Name"

URL = "Website URL"

EMAIL = "email@gmail.com"

phone = "+1 xxx xxx xxxx"

twitter = "twitter_handle"

twitter_url = "twitter_url"

linkedin = "linkedin_handle"

linkedin_url = "linkedin_url"

telegram = "telegram_handle"

telegram_url = "telegram_url

pic = "picture_url"

## Do you want your QR code on your Iphone?
- Save the .png file outputed by this code in your camera roll
- Download *Widgetsmith* app
- Create a widget using the .png file in your camera roll
- Go to Iphone widget panel and insert recently created widget to your Home Page
- Enjoy the amazing networking experience and share your contact card!


Cheers. 