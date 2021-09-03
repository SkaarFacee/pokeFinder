# pokeFinder :cyclone:
A CNN made using tensorflow that is cabable of detecting a pokemon on an image. The whole idea was to be able to identify pokemon from the hundreds of games available. The CNN architecture is based of a Mini VGG architecture.
# Dataset :rocket:
The dataset for this project was made by scraping images of all first generation pokemon from a popluar pokemon website and then adding each image to various game/anime backgrounds. Finally a total of 1000+ images was collected for a 150 different pokemon in the first generation. 
&nbsp; &nbsp; &nbsp; &nbsp; The `scraper` used to collect the images of pokemon is divided into 2 parts: 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - `scraper.py` collects the pokemon and it's image url, saving it as a JSON file.
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - `downloader.py` makes use of asynchronous functions to download each pokemon image
 &nbsp; &nbsp; &nbsp; &nbsp; Finally the images (each pokemon and background image) is blended together

 # CNN Architecture :zap:
 The CNN architecture is based of a Mini VGG architecture. It contains  many of the same layers and operations used in state of the art CNNs today, however is a toned down version. For further understanding take a look at this [research paper](https://arxiv.org/pdf/1409.1556v6.pdf) 
Activation Functions used are **ReLU** and **softmax**

# ToDo :scroll: 
- [ ] Add a CLI method to read image and predict the pokemon
- [ ] Add an API version of the same 
- [ ]  Add the next 2 generations of pokemon

