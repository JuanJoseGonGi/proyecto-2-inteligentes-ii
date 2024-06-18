import os

# Directory containing images
image_dir = "other-models"
image_extensions = [".jpg", ".jpeg", ".png", ".pdf"]  # Add more extensions if needed

# Get list of image files
image_files = [
    f
    for f in os.listdir(image_dir)
    if os.path.splitext(f)[1].lower() in image_extensions
]

# Generate LaTeX code
with open("discussion_images.tex", "w") as f:
    f.flush()
    for batch_index in range(0, len(image_files), 4):
        images = image_files[batch_index : batch_index + 4]

        f.write(r"\begin{figure}[H]" + "\n")
        f.write(r"    \centering" + "\n")
        for image in images:
            f.write(r"    \begin{subfigure}{.47\linewidth}" + "\n")
            f.write(r"        \centering" + "\n")
            f.write(
                r"        \includegraphics[width=\textwidth]{"
                + os.path.join(image_dir, image).replace("\\", "/")
                + "}"
                + "\n"
            )
            f.write(r"    \end{subfigure}" + "\n")
        f.write(r"\end{figure}" + "\n")

print("LaTeX code has been written to discussion_images.tex")
