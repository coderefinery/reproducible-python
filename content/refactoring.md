(refactoring)=

# Code quality and good practices

In this episode we will explore code quality and good practices in Python using
a hands-on approach. We will together build up a small project and improve it
step by step.

We will start from a relatively simple image processing script which can read a
telescope image of stars and our goal is to **count the number of stars** in
the image. Later we will want to be able to process many such images.

The (fictional) telescope images look like the one below here ([in this
repository](https://github.com/workshop-material/random-star-images) we can find more):
:::{figure} img/stars.png
:alt: Generated image representing a telescope image of stars
:width: 60%

Generated image representing a telescope image of stars.
:::

:::{solution} Starting point (spoiler alert)

We can imagine that we pieced together the following code
based on some examples we found online:
```python
import matplotlib.pyplot as plt
from skimage import io, filters, color
from skimage.measure import label, regionprops


image = io.imread("stars.png")
sigma = 0.5

# if there is a fourth channel (alpha channel), ignore it
rgb_image = image[:, :, :3]
gray_image = color.rgb2gray(rgb_image)

# apply a gaussian filter to reduce noise
image_smooth = filters.gaussian(gray_image, sigma)

# threshold the image to create a binary image (bright stars will be white, background black)
thresh = filters.threshold_otsu(image_smooth)
binary_image = image_smooth > thresh

# label connected regions (stars) in the binary image
labeled_image = label(binary_image)

# get properties of labeled regions
regions = regionprops(labeled_image)

# extract star positions (centroids)
star_positions = [region.centroid for region in regions]

# plot the original image
plt.figure(figsize=(8, 8))
plt.imshow(image, cmap="gray")

# overlay star positions with crosses
for star in star_positions:
    plt.plot(star[1], star[0], "rx", markersize=5, markeredgewidth=0.1)

plt.savefig("detected-stars.png", dpi=300)

print(f"number of stars detected: {len(star_positions)}")
```
:::


Part 1:
- 15 min: Discuss how we would solve the problem, run example code, and make it work
  as part of a Jupyter notebook.
- 15 min: Refactor the positioning code into a function and a module
- 15 min: Now we wish to process many images - discuss how we would approach this
- 15 min: Introduce CLI and discuss the benefits

Part 2:
- 30 min: From a script to a workflow (using Snakemake)
- 15 min: Discuss concepts
  - Pure functions
  - Design patterns: functional design vs. object-oriented design
  - How to design your code before writing it: document-driven development

Bonus:
- Move it under Git
- Document dependencies
- Show nbdime, black, vulture, ruff
