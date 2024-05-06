
# Dash Pylette

### Introduction

Welcome to Dash Pylette - a  Dash app showcasing the power of the [Pylette](https://github.com/qTipTip/Pylette) library. This app serves as a tool to extract
color palettes from images. Whether you're a designer, artist, or developer, Dash Pylette provides an easy
way to generate color schemes for your projects.

###  See it live at https://dashpylette.pythonanywhere.com/

------------------

![dash-pylette](https://github.com/AnnMarieW/dash-pylette/assets/72614349/1ce897c4-caa2-4b24-a0a7-d795faa516d5)


--------------

### Getting Started

1. **Select Image**: Choose an image from the dropdown menu or upload your own.  

Configure Pylette

2. **Sort Colors By** - will sort the color palette by the frequency or the luminance (perceived brightness).
3. **Color Quantization Mode** - to specify the color quantization method - either using K-Means (default) or Median-Cut algorithms.
4. **Palette Color Count** - set the number of colors in the palette
5. **Resize** - resize the image to a more manageable size before beginning color extraction. This significantly speeds up the extraction, but reduces the faithfulness of the color palette.
6. **Generate Palette**: Let Pylette work its magic and extract a color palette from the selected image.

Use the generated Color Palette  

7. **Explore**: Explore the extracted colors and pick your favorites using the color picker.
8. **Set Frame Color**: Set the selected color as the frame color for the image to see it in action.
9. **Experiment**: Try out different images, algorithms, and sorting methods to discover unique color combinations.
10. **Copy the Color Palette**: Use the generated color palette in your onw project!


### To run the app locally

To get started with Dash Pylette, clone this repository and run the app:

```bash
git clone https://github.com/AnnMarieW/dash-pylette.git
cd dash-pylette
python3 -m venv venv && . venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

### Contributing

Contributions to Dash Pylette are welcome! Whether it's fixing bugs, adding features, or improving documentation, 
your contributions help make Dash Pylette even better. Simply fork the repository, make your changes, and submit a pull request.

### Show Your Support!
If you find Dash Pylette helpful or enjoy using the open-source libraries it depends on, please consider showing your support by giving a ⭐️ star to:

- Dash Pylette: Help us grow and improve by giving this repository a star.
- [Pylette](https://github.com/qTipTip/Pylette): Show appreciation for the powerful color extraction capabilities of Pylette.
- [Dash](https://github.com/plotly/dash): Support the development of Dash, the Python framework used to create interactive web applications.
- [Dash Mantine Components](https://github.com/snehilvj/dash-mantine-components): Contribute to the growth of Dash Mantine Components, providing beautiful UI components for Dash apps.
- [DashIconify](https://github.com/snehilvj/dash-iconify): Encourage the development of DashIconify, enabling the use of icons in Dash applications with ease.
Your stars not only boost our morale but also help others discover these valuable tools. Thank you for your support!

### License

Dash Pylette is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

#### **Happy Palette Crafting!** 🎨✨