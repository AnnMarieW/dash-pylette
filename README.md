
# Dash Pylette

### Introduction

Welcome to Dash Pylette - a  Dash app showcasing the power of the [Pylette](https://github.com/qTipTip/Pylette) library. This app serves as a tool to extract
color palettes from images. Whether you're a designer, artist, or developer, Dash Pylette provides an easy
way to generate color schemes for your projects.


### Find more information in the [Pylette GitHub](https://github.com/qTipTip/Pylette) 
__Don't forget to give it a :star:__

### Features

- **User-Friendly Interface**: Easily select an image from the dropdown menu or upload your own to generate a color palette.
- **Dynamic Color Picker**: Explore the extracted colors and choose the perfect frame color for the image.
- **Customization Options**: Configure Pylette to extract colors using different algorithms and sorting methods.
- **Integration with Pylette**: Utilizes the powerful features of the Pylette library for efficient color extraction.
- **Responsive Design**: Designed with the Dash Mantine Components Library.

###  See it live at:  

![dash-pylette](https://github.com/AnnMarieW/dash-pylette/assets/72614349/313443f8-ae43-4371-a4d4-ba9051deb61c)

### Getting Started

To get started with Dash Pylette, simply install the Pylette library:


Then, clone this repository and run the app:

```bash
git clone https://github.com/your-username/DashPylette.git
cd DashPylette
pip install -r requirements.txt
python app.py
```

### Usage

1. **Select Image**: Choose an image from the dropdown menu or upload your own.  

Configure Pylette

2. **Sort Colors By** - will sort the color palette by the frequency or the luminance (perceived brightness).
3. **Color Quantization Mode** - to sepecify the color quantization method - either using K-Means (default) or Median-Cut algorithms.
4. **Palette Color Count** - set the number of colors in the palette
5. **Resize** - resize the image to a more manageable size before beginning color extraction. This significantly speeds up the extraction, but reduces the faithfulness of the color palette.
2. **Generate Palette**: Let Pylette work its magic and extract a color palette from the selected image.

Use the generated Color Palette
5. **Explore**: Explore the extracted colors and pick your favorites using the color picker.
4. **Set Frame Color**: Set the selected color as the frame color for the image to see it in action.
5. **Experiment**: Try out different images, algorithms, and sorting methods to discover unique color combinations.



### License

Dash Pylette is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

#### **Happy Palette Crafting!** 🎨✨