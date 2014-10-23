gem 'ruby-imgur'
client = Imgur::Client.new
image = client.images.all.first
image.open_in_browser