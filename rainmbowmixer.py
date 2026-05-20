import flet as ft

def main(page: ft.Page):

    def changeColor(e):
        redValue = int(redSlider.value)
        greenValue = int(greenSlider.value)
        blueValue = int(blueSlider.value)

        page.bgcolor = f"#{redValue:02x}{greenValue:02x}{blueValue:02x}"
        colorText.value = f"RGB: ({redValue}, {greenValue}, {blueValue})"
        page.update()

    redSlider = ft.Slider(
        label="Red",
        value=0,
        min=0,
        max=255,
        divisions=255,
        on_change=changeColor
    )

    greenSlider = ft.Slider(
        label="Green",
        value=0,
        min=0,
        max=255,
        divisions=255,
        on_change=changeColor
    )

    blueSlider = ft.Slider(
        label="Blue",
        value=0,
        min=0,
        max=255,
        divisions=255,
        on_change=changeColor
    )

    colorText = ft.Text(value="RGB: (0,0,0)")

    page.add(colorText, redSlider, greenSlider, blueSlider)

ft.run(main)