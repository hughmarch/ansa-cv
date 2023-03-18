### Computer vision for nucleation site analysis

To track the behavior and growth of nucleation sites, we will focus on two important attributes of nucleation sites:
<ul>
<li>Radius - how big the spot is. In developing our diagnostic test, we want to <em>minimize</em> increase the density of discrete nucleation sites per unit of area.</li>
<li>Intensity - how bright the spot is compared to our background. This tells us how strong our signal is compared to the background noise, which is an indicator for how reliably we can detect nucleation sites. Ideally we want to have our radius be as small as possible while our intensity is large enough.</li>
</ul>

At a very high level, the process for extracting information about nucleation site growth takes two steps:
<ol>
<li>Identify nucleation sites in the image</li>
<li>Measure the intensity and radius of each individual site over time</li>
</ol>

To accomplish this, we will use the following image analysis pipeline:
