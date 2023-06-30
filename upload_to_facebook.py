import os
import facebook

# I removed access tokens for privacy, replace with your won
access_token = 'YOUR_ACCESS_TOKEN'
# I removed group ID for privacy. Replace with your own. 
# Check this link to find your group ID https://www.sociablekit.com/how-to-find-facebook-group-id/
group_id = 'YOUR_GROUP_ID'

# Initialize the Facebook Graph API
graph = facebook.GraphAPI(access_token)

# Local path to your albums. For me I just used ~
directory_path = '/path/to/albums'

# Get the list of directories in the specified path
directories = [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]

# Iterate over the directories
for directory in directories:
    # Create an album with the directory name
    album_name = directory
    album_response = graph.put_object(group_id, "albums", name=album_name)
    album_id = album_response['id']
    
    # Get the list of images in the directory
    images_path = os.path.join(directory_path, directory)
    images = [name for name in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, name))]

    # Upload each image to the created album
    for image in images:
        image_path = os.path.join(images_path, image)
        with open(image_path, 'rb') as image_file:
            graph.put_photo(image=image_file, album_path=album_id+'/photos')
    # Success prints here!
    print(f"Uploaded images in album: {album_name}")
