#### Site identification

We just need one image to identify where sites are, so we will only use the last image for this:

<ol>
<li><strong>Binary threshold - </strong>Set all pixels that are brighter than some threshold value to white, set all other pixels to black.</li>
<li><strong>Connected components - </strong>Groups together pixels that are next to each other of the same color, like getting connected components of a graph. These are our nucleation site candidates.</li>
<li><strong>Selection criteria - </strong>The goal is not to measure every single site in the image, but just a statistically significant sample size, so we will ignore sites that would be hard to measure. Identified regions, for instance, that are not circular (high eccentricity) are likely multiple sites that have merged, so we only choose sites with a lower eccentricity. This doesn't pick up on every site that doesn't merge, but for our purposes this is good enough.</li>
<li><strong>Bounding boxes & padding - </strong>We define the region of interest for every "good" nucleation site to be the smallest bounding box that contains the thresholded region plus an additional constant padding of 3 pixels. Selected regions are drawn as boxes below:</li>
</ol>