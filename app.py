import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, _dash_renderer, html, dcc, callback, Input, Output, State, ctx
from Pylette import extract_colors
import tempfile
import base64

_dash_renderer._set_react_version("18.2.0")

icons = {
    "github": "ion:logo-github",
    "tools": "bi:tools",
    "palette": "bi:palette",
}


select_image = dmc.Select(
    id="select-image",
    label="Select sample image",
    placeholder="Select one",
    data=[
        {"value": "assets/flowers.jpg", "label": "Flowers"},
        {"value": "assets/fall.jpg", "label": "Fall in New England"},
        {"value": "assets/duck.jpg", "label": "Duck"},
        {"value": "assets/space_needle.jpg", "label": "Space Needle"},
        {"value": "assets/mushrooms.jpg", "label": "Mushrooms"},
        {"value": "assets/flowers_arrangement.jpg", "label": "Flower Arrangement"},
    ],
    w="100%",
    mb=10,
    value="assets/flowers.jpg",
)

upload = dcc.Upload(
    dmc.NavLink(label="Drag and Drop or Upload an Image File", className="upload"),
    multiple=False,
    id="upload-image",
)


sort_by_data = [["frequency", "Frequency"], ["luminance", "Luminance"]]
sort_by = dmc.RadioGroup(
    children=dmc.Group([dmc.Radio(l, value=k) for k, l in sort_by_data], my=10),
    id="radio-group-sort-by",
    value="frequency",
    label="Sort colors by",
    size="sm",
    mb=30,
)


mode_data = [["KM", "K-Means"], ["MC", "Median Cut"]]
mode = dmc.RadioGroup(
    children=dmc.Group([dmc.Radio(l, value=k) for k, l in mode_data], my=10),
    id="radio-group-mode",
    value="MC",
    label="Color quantization mode",
    size="sm",
    mb=30,
)


resize = dmc.Checkbox(
    id="checkbox-resize", label="Resize image for faster results", checked=False, mb=30
)


pallette_color_count = dmc.Slider(
    value=6, min=1, step=1, max=12, w="100%", my=20, id="color-count"
)


set_frame_color = dmc.Checkbox(
    id="checkbox-set-background", label="Set image frame color", checked=True, mb=10
)


color_picker = dmc.ColorPicker(
    id="color-picker", swatchesPerRow=6, withPicker=False, mb=10
)


def create_link(icon, href):
    return dmc.Anchor(
        dmc.ActionIcon(
            DashIconify(icon=icon, width=25), variant="transparent", size="lg"
        ),
        href=href,
        target="_blank",
        visibleFrom="xs",
    )


header = dmc.Group(
    [
        dmc.Burger(id="burger-button", opened=False),
        dmc.Text(["Pylette: Extract a color palette from an image"], size="xl"),
        create_link(icons["github"], "https://github.com/qTipTip/Pylette"),
    ],
    justify="flex-start",
)


def make_divider(text, icon):
    return dmc.Divider(
        label=[
            DashIconify(icon=icon, height=23),
            dmc.Text(text, ml=5, size="sm"),
        ],
        labelPosition="left",
        mt=60,
        mb=10,
    )


navbar = html.Div(
    [
        select_image,
        dmc.Text("Or upload a file", size="sm"),
        upload,
        make_divider("Configure Pylette", icons["tools"]),
        sort_by,
        mode,
        resize,
        dmc.Text("Palette color count", size="sm"),
        pallette_color_count,
    ]
)

page_content = dcc.Loading(
    [
        dmc.Center(
            html.Div(
                html.Img(
                    id="image", style={"height": 650, "width": "auto", "padding": 50}
                ),
                id="image-card",
                style={"height": 650},
            )
        ),
        dmc.Group(id="palette", gap=0, justify="center", mt=10),
        html.Center(
            html.Div(
                [
                    color_picker,
                    dmc.Text(id="selected-color", mb=24),
                    dmc.ScrollArea(html.Div(id="copy"), w=650),
                ]
            )
        ),
    ],
    overlay_style={"visibility": "visible", "opacity": 0.5, "backgroundColor": "white"},
    delay_show=500
)


app = Dash()

app_shell = dmc.AppShell(
    [
        dmc.AppShellHeader(header, px=25),
        dmc.AppShellNavbar(navbar, p=24),
        dmc.AppShellMain(page_content),
    ],
    header={"height": 70},
    padding="xl",
    navbar={
        "width": 375,
        "breakpoint": "md",
        "collapsed": {"mobile": True},
    },
    id="app-shell",
)

app.layout = dmc.MantineProvider([app_shell])


def save_base64_image(base64_string):
    """
    Save uploaded image to a temporary file
    :param base64_string: image
    :return: temporary path name
    """
    # Decode the base64 string into bytes
    image_data = base64.b64decode(base64_string.split(",")[1])
    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        # Write the image data to the temporary file
        temp_file.write(image_data)
    return temp_file.name


@callback(
    Output("image", "src"),
    Output("color-picker", "swatches"),
    Output("color-picker", "value"),
    Output("copy", "children"),
    Input("select-image", "value"),
    Input("upload-image", "contents"),
    Input("color-count", "value"),
    Input("radio-group-sort-by", "value"),
    Input("radio-group-mode", "value"),
    Input("checkbox-resize", "checked"),
)
def update_image(image_path, upload, color_count, sort_value, mode_value, resize_value):
    """
    Notes:
        `extract_colors` accepts an image file path only.  If a file is uploaded, it's saved in a temporary file
        the html.Img `src` prop is either the uploaded base64 file, or a path to a file in the assets folder.
    """
    src = image_path

    if ctx.triggered_id == "upload-image":
        temp_file_path = save_base64_image(upload)
        image_path = temp_file_path
        src = upload

    palette = extract_colors(
        image=image_path,
        palette_size=color_count,
        mode=mode_value,
        sort_mode=sort_value,
        resize=resize_value,
    )

    swatches = [f"rgb{color.rgb}" for color in palette]
    dominant_color = swatches[0]

    copy_swatches = dmc.CodeHighlight(
        code=f" color_palette = {swatches}",
        language="python",
        copyLabel="copy color palette",
        p="sm",
        style={"textAlign": "left"}
    )

    return src, swatches, dominant_color, copy_swatches


@callback(
    Output("image-card", "style"),
    Output("selected-color", "children"),
    Input("color-picker", "value"),
)
def update_frame_color(color):
    style = {"backgroundColor": color}
    selected = f"Selected frame color: {color}"
    return style, selected


@callback(
    Output("app-shell", "navbar"),
    Input("burger-button", "opened"),
    State("app-shell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar

if __name__ == "__main__":
    app.run_server(debug=True)
