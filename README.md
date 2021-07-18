# AI-optical-search-using-VGG16
In this project, I have integrated ML with Django web application. It will take an image as an input and will return detailed information about given image using VGG 16 model and wikipedia API

<!-- wp:paragraph -->
<p>In this project, I have integrated ML with Django web application. It will take an image as an input and will return detailed information about given image using VGG 16 model and wikipedia API</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":152,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://cwadtech.files.wordpress.com/2021/07/untitled-17.png?w=1024" alt="" class="wp-image-152"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Introduction</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Optical Search image is an application&nbsp; that takes an image file as an input and&nbsp; returns results related to the image.&nbsp; In this we used Python language for backend and for designing purpose we used HTML, CSS, JQuery, JavaScripts and Bootstrap.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this VGG16 model is used for detection and classification. VGG16 is a convolution neural Network model for Large-scale Image Recognition. The model achieves 92.7%&nbsp; top-5&nbsp; test accuracy in ImageNet, which is a dataset of over 14 million&nbsp; images belonging to 1000 classes. The CNN Model predict the class label / category of the image.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After prediction it checks for Wikipedia whether there is any Wikipedia related to image or not. When there is Wikipedia related to image it shows the result that available on Wikipedia. When there is no Wikipedia details related to image this respond to user couldn’t find Wikipedia details.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>By using Optical search we can learn more about an image in few second. It helps in reducing the amount of time taken to find similar images and information related image.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Tools &amp; Technologies Used</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Software used : </strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Visual Studio Code</li><li>Jupyter Notebook</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Backend :&nbsp;</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Python</li><li>Django</li><li>Tensorflow</li><li>Keras – Deep Learning</li><li>VGG16 – (DL model)</li><li>Imagenet – Dataset</li><li>No. of classes - 1000</li><li>Wikipedia API (To get detailed information about predicted model)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Frontend :</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>HML</li></ul>
<!-- /wp:list -->

<!-- wp:list -->
<ul><li>CSS</li><li>JS</li><li>JQuery</li><li>Bootstrap</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Database : </strong>SQLite</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Project Lifecycle</h3>
<!-- /wp:heading -->

<!-- wp:image {"id":158,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://cwadtech.files.wordpress.com/2021/07/untitled-18.png?w=652" alt="" class="wp-image-158"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":159,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://cwadtech.files.wordpress.com/2021/07/untitled-19.png?w=660" alt="" class="wp-image-159"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>SNAPSHOTS</h3>
<!-- /wp:heading -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh5.googleusercontent.com/so7k1JBDwX1-yMzQw-XCI4i2fh6KhPq1Y8yhlsH-0eyL9Xt2P9efhnQNoVZSJirmB2UCMT4odURZLnd0Z11jUwdVHgYZsemn5E9kGK54t8805Mbj0mOg2sxo03r1V8mqWo3Wz9k" alt="C:\Users\acer\Downloads\1623214227632.png"/><figcaption><strong>Front End of the project</strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This is the front end of the project. Here user can search an image.</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh6.googleusercontent.com/7S_CbJwmuq7Ey5NYfPhNPFTqTT-RY1EeU3vvCokbyoq05Ah7PWbbeX_bSdclXWSPIYLe3oZHP4hj243z2ff3oAnWzbVapLdIx0Wvv4yEJpOtoMDlfebIS_4ZLlxRhztrZoDAQ9s" alt="C:\Users\acer\Downloads\1623214227627.png"/><figcaption><strong>When user select an Image</strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>This looks like this when user search any image from the files.</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh5.googleusercontent.com/VnSRCnwUENn8pyIPfJbKJToOEzWTLvDIDXIKdtYLzBIdz9SPN4NHtEw83HRIUoXGzPwZGJFshHfKsdFfmPXbKLoYfqIIK8RXYPPPtN0Zzz-OK6Z8_0LBZYmPC5IVIgJRvYpypPg" alt="C:\Users\acer\Downloads\65464564.png"/><figcaption><strong>Image During The Scanning Process</strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>After selecting image firstly it will scan the image then goes to database</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh5.googleusercontent.com/z_E2YYvb9Bq5v7AHjXoNDUm4ceQpRHrnRR_AOAoApsxgwzFYiPEQjVpH8-v-cIfs1zv4oGzXanG9YdXBwEhirTlPYz9LBO5p6NODviCesKScgwhG_iipgGBPLiIs3V79XYbzhf4" alt="C:\Users\acer\Downloads\65456646454564456456.png"/><figcaption><strong>Image After The Scanning</strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>After scanning the search result of image store in database and Wikipedia gives the information about the image i.e the name of the searched object and images related to the particular object.</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh3.googleusercontent.com/5eSuF1QNHoNBdPCTcj0GyPgGqpxQrkZzdCZS54kDow-5CGbCbw-x3OOi3SG9pG02FNmnPojaKelcLUxjxD8YbOw_1PH1oN_qG7HEwZ-kZFHrZ8HKzsYBhWv0L4Bwumixp0Mj9C8" alt="C:\Users\acer\Downloads\WhatsApp Image 2021-06-08 at 7.05.42 PM.jpeg"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The related images of the searched flower.</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh4.googleusercontent.com/Y1ict5xVd5FdXxT50eNDfZq369jvIWM9rmQ0q0Yqn1PfltvmFrbfHQg2Dww0olmTbQKfHSW2YqwLE4pZjk7kSzf-bOOo9MQ2ngEIXezb6T6bNwRMErVBrVt7mNVWAjWJjVcWNVM" alt="C:\Users\acer\Downloads\kjhajhsdhkajsdjkhasjkhd.png"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>All information about the searched image is like as&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh6.googleusercontent.com/mWFnfjBZO_o8xKbv9n5oBLHU-unHIQ31cO8m8YFMyfM29KN3FfcLBKtRRVgjgItCYN6ADwLvEz0JtEpEllccLC91gCKFkD3kkp_8C0eCfWAWqDY72dcZ74G13RCK4PcIQPjFqBc" alt="C:\Users\acer\Downloads\+++++++.png"/><figcaption><strong>Previous Search Results</strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>All the previous search results are store in database which is also shown in this website</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Database Snapshots:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh3.googleusercontent.com/f_y_KwHX2zJ_QujEgXfKAeb20grDa2dz37jyoApS8PKdo44Evg40bpsLPpQd7HlUead1tjp4MelC24esA07iDPGiCoM3k623AmTG0knlKEXxB5rZD3gHEkBcLnLQbQ7WbWLQSmw" alt="C:\Users\acer\Downloads\image12245456 (1).png"/></figure>
<!-- /wp:image -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://lh3.googleusercontent.com/TCoLoYn0XldejETs9891BvrYFDazNTR_IzmWyYDe1J-s4_cfgoTCZorLdsK2othyfbzi3ag-IB0PF3Oy12R5f9N-vTH9vBw7dGHVXBqJHw0USbSiOrIbDsLm7cu_cEXpRD0cf_0" alt="C:\Users\acer\Downloads\image.png"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>DOWNLOAD CODE :</h3>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><li>Download the code from <a href="https://github.com/akd6203/AI-optical-search-using-VGG16">github</a></li><li>Download all above mentioned software dependencies</li><li>Open downloaded folder inside terminal.</li><li>Run following commands:</li></ol>
<!-- /wp:list -->

<!-- wp:code -->
<pre class="wp-block-code"><code>conda create --name envName django
conda activate envName
pip install tensorflow
pip install wikipedia
python manage.py makemigrations
python manage.py migrate
python manage.py runserver</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Note: There is no VGG16 (mymodel.h5) file inside repository. You are expected to download weights by your own.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> <strong>VISIT MY YOUTUBE CHANNEL FOR MORE DETAILS</strong>: <a href="https://youtu.be/D2t-P3zEeSk">https://youtu.be/D2t-P3zEeSk</a> </p>
<!-- /wp:paragraph -->
