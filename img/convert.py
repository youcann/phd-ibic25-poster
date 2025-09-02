from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load grayscale image with PIL
gray_img = Image.open('basler2.png').convert('L')  # Ensure grayscale

# Convert to NumPy array and normalize to [0, 1]
gray_np = np.array(gray_img) / 255

# Apply Viridis colormap
viridis = cm.get_cmap('viridis')
viridis_img = viridis(gray_np)  # Returns RGBA float array in [0, 1]

# Convert to 8-bit RGB image (drop alpha channel)
viridis_rgb = (viridis_img[:, :, :3] * 255).astype(np.uint8)

# Convert to PIL Image
viridis_pil = Image.fromarray(viridis_rgb)

# Save to file
viridis_pil.save('basler2v.png')
