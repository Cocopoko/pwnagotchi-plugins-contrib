import logging
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.ui.view as view
import pwnagotchi.ui.components as components
import pwnagotchi.plugins as plugins
import pwnagotchi
import subprocess

class OnlineOfflinePlugin(plugins.Plugin):
    __author__ = 'akira'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Plugin that displays wether your gotchi is either online or offline from the internet.'

    __dependencies__ = {
        'pip': ['scapy']
    }
    __defaults__ = {
        'enabled': False,
    }

    def on_loaded(self):
        logging.info("pinging if gotchi is online or nah..............")

    def on_ui_setup(self, ui):
        ui.add_element('is', components.LabeledValue(color=view.BLACK, label='', value='', position=(39, 20),
                                                         label_font=fonts.Bold, text_font=fonts.Bold))

        ui.add_element('is', components.LabeledValue(color=view.BLACK, label='', value='', position=(39, 20),
                                                          label_font=fonts.Bold, text_font=fonts.Bold))

    def on_ui_update(self, ui):
        try:
            output = subprocess.check_output(['ping', '-c', '1', '1.1.1.1'],)
            ui.set('is', 'online')
        except subprocess.CalledProcessError:
            ui.set('is', 'offline')

    def on_ready(self, agent):
        while True:
            try:
                subprocess.check_output(['ping', '-c', '1', '1.1.1.1'],)
                ui.set('is', 'online')
            except subprocess.CalledProcessError:
                ui.set('is', 'offline')
            time.sleep(30) 

# Instantiate the plugin
plugin = OnlineOfflinePlugin()
# Call the on_loaded method to initialize the plugin
plugin.on_loaded()