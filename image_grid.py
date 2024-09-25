from PIL import Image, ImageDraw

def overlay_grid(image_path, grid_size, output_path):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Get image dimensions
    width, height = image.size
    
    # Draw vertical lines
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill="red", width=1)
    
    # Draw horizontal lines
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill="red", width=1)
    
    # Save the modified image
    image.save(output_path)
    print(f"Grid overlay saved as {output_path}")

# Example usage
image_path = input("Enter the path of the image: ")
grid_size = int(input("Enter the grid size (in pixels): "))
output_path = "output_image.png"  # You can change the output filename

overlay_grid(image_path, grid_size, output_path)