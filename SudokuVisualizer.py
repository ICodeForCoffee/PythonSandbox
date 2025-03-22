#import webbrowser
#import atlastk
from nicegui import app, ui

BODY = """
<table>
<tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
</tr>
</table>
"""

def main():
    print("Display a grid")
    
    app.native.window_args['resizable'] = False
    app.native.start_args['debug'] = True
    app.native.settings['ALLOW_DOWNLOADS'] = True
    
    ui.label('Hello NiceGUI!')
    ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))
    ui.html(BODY)
    
    #ui.run(native=True, window_size=(400, 300), fullscreen=False)
    ui.run()




main()