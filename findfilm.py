# imported the requests library
import requests
image_url = "https://www.python.org/Lutsifer.mp4"

# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("Lutsifer.mp4",'mp4 ') as f:

	# Saving received content as a png file in
	# binary format

	# write the contents of the response (r.content)
	# to a new file in binary mode.
	f.write(r.content)
