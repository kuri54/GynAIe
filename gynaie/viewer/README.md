# GynAIe Viewer
The GynAIe Viewer is a tool designed to facilitate the viewing and filtering of image data efficiently. By using this viewer, you can quickly review images stored in specific directories.

## How to Use
1. Launching the Viewer:  
Run `gynaie-viewer` from the command line or terminal to start the viewer.

2. Selecting a Directory:  
Once the viewer is launched, you will be prompted to select the directory containing the images you wish to display.

3. Applying Filters:  
Apply filters to the image list to display only those images that meet certain criteria.

4. Image Enlargement:  
Hovering over an image displays a magnification button. You can also enlarge images of sorting results.

5. Checking Images:  
After viewing images in the viewer, please make sure to check the checkbox. This will help you keep track of which images have been reviewed and prevent forgetting where you left off.

## Important Notes
- **Supported Directories:** Currently, only images stored in the `GynAIe/input` directory can be displayed. Support for other directories is planned for the future, but it is a low priority at this moment.
- **How to Exit:** After viewing the images, please close the browser and either close the terminal window or press `Ctrl + C` to terminate the task.
- **Error Messages:** You may see the `MediaFileHandler: Missing file` error message in the terminal while displaying images. This is a Streamlit-specific message, and we are unable to address it. Please wait for a library update.

