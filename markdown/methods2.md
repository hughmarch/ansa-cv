#### Preprocessing

The first step for identifying and measuring nucleation sites is to first preprocess our raw image data to reduce noise and normalize our image. Images at every time frame are preprocessed.

<ol>
<li><strong>Center crop - </strong>The circular boundary in the raw image data is the boundary of the RPA solution. Due to evaporation (notice how the boundary changes over time), uneven lighting, autofluoresence, etc., it proved difficult to try to segment the image into background and solution. We don't care too much about finding every single nucleation site, all we need is a statistically significant sample size, so a simple center crop is good enough.</li>
<li><strong>Moving average - </strong>This is our first denoising step. We take the average image every 10 frames, so we go from 900 images to 90 images, each of these images being the average of 10 original images. This helps us get rid of noise from our camera sensor, since we are artificially increasing the exposure by a factor of 10.</li>
<li><strong>Background subtraction - </strong>We take the average of the first 24 of 90 images (first 4 minutes of experiment where nothing is happening) to get a good idea of what the background signal is. We then subtract this background from every frame, so all that's left is the signal produced by nucleation sites.</li>
<li><strong>Box blur - </strong>To get rid of any high frequency noise left in the image, we apply a simple box blur filter.</li>
</ol>