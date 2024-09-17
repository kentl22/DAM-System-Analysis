from shiny import App, Inputs, Outputs, Session
from shiny import render, reactive, req, ui


# Create a custom header with logo and title
header = ui.div(
    ui.img(src="path_to_your_logo.png", height="30px", style="margin-right: 10px; vertical-align: middle;"),
    ui.h2("DAM System Analyzer", style="display: inline-block; vertical-align: middle; margin: 0;"),
    style="display: flex; align-items: center; padding: 10px;"
)

# Page title and tabs
app_ui = ui.page_fluid(
    header,  # Add the custom header here
    ui.navset_tab(
        ui.nav_panel("Data Cleaned", ""),
        ui.nav_panel("Experiment Analysis", ""),
        ui.nav_panel("Raster Plots", ""),
        ui.nav_menu(
            "Period Analysis",
            ui.nav_panel("Lomb-Scargle", ""),
            ui.nav_panel("Cosinor", ""),
            ui.nav_panel("Chi-Squared", ""),
            ui.nav_panel("Fourier Transform", ""),
            "----",
            "Description:",
            ui.nav_control(
                ui.a("Shiny", href="https://shiny.posit.co", target="_blank")
            ),
        ),
        id="selected_navset_tab",
    ),
    ui.h5("Selected:"),
    ui.output_code("selected"),
)

def server(input, output, session):
    @render.code
    def selected():
        return input.selected_navset_tab()

app = App(app_ui, server)