import click
import matplotlib.pyplot as plt
from skimage import io, filters, color
from skimage.measure import label, regionprops


def convert_to_gray(image):
    # if there is a fourth channel (alpha channel), ignore it
    rgb_image = image[:, :, :3]
    return color.rgb2gray(rgb_image)


def locate_positions(image):
    gray_image = convert_to_gray(image)

    # apply a gaussian filter to reduce noise
    image_smooth = filters.gaussian(gray_image, sigma=0.5)

    # threshold the image to create a binary image (bright objects will be white, background black)
    thresh = filters.threshold_otsu(image_smooth)
    binary_image = image_smooth > thresh

    # label connected regions in the binary image
    labeled_image = label(binary_image)

    # get properties of labeled regions
    regions = regionprops(labeled_image)

    # extract positions (centroids)
    positions = [region.centroid for region in regions]

    return positions


def plot_positions(image, positions, file_name):
    # plot the original image
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap="gray")

    # overlay positions with crosses
    for y, x in positions:
        plt.plot(y, x, "rx", markersize=5, markeredgewidth=0.1)

    plt.savefig(file_name, dpi=300)


@click.command()
@click.option(
    "--image-file", type=click.Path(exists=True), help="Path to the input image"
)
@click.option("--output-file", type=click.Path(), help="Path to the output file")
@click.option("--generate-plot", is_flag=True, default=False)
def main(image_file, output_file, generate_plot):
    image = io.imread(image_file)

    star_positions = locate_positions(image)

    if generate_plot:
        plot_positions(image, star_positions, f"detected-{image_file}")

    with open(output_file, "w") as f:
        f.write(f"number of stars detected: {len(star_positions)}\n")


if __name__ == "__main__":
    main()
