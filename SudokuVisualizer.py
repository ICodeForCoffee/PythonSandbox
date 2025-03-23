#import webbrowser
#import atlastk
from nicegui import app, ui
from SudokuPuzzle import SudokuPuzzle
import copy

#This might get removed, but for now it's here.
STYLE = """
<style>
table, th, td {
  border: 1px solid black;
}

td {
    height: 20px;
  width 20px;
}
</style>
"""

POSSIBLE_VALUES = """
<table class="possibleValues">
<tr>
    <td data-fakeId="y1">z1</td>
    <td data-fakeId="y2">z2</td>
    <td data-fakeId="y3">z3</td>
</tr>
<tr>
    <td data-fakeId="y4">z4</td>
    <td data-fakeId="y5">z5</td>
    <td data-fakeId="y6">z6</td>
</tr>
<tr>
    <td data-fakeId="y7">z7</td>
    <td data-fakeId="y8">z8</td>
    <td data-fakeId="y9">z9</td>
</tr>
</table>
"""

SUDOKY_CONTAINER = """
<table class="puzzle">
<tr>
    <td data-fakeId="x1">z1</td>
    <td data-fakeId="x2">z2</td>
    <td data-fakeId="x3">z3</td>
</tr>
<tr>
    <td data-fakeId="x4">z4</td>
    <td data-fakeId="x5">z5</td>
    <td data-fakeId="x6">z6</td>
</tr>
<tr>
    <td data-fakeId="x7">z7</td>
    <td data-fakeId="x8">z8</td>
    <td data-fakeId="x9">z9</td>
</tr>
</table>
"""

def render_possible_values(possible_values):
    body_new = copy.deepcopy(POSSIBLE_VALUES)
    
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        cell = "z" + str(x)
        if x in possible_values:
            body_new = body_new.replace(cell, str(x))
        else:
            body_new = body_new.replace(cell, "&nbsp;")
    
    ui.html(body_new)

#this method will have to go at some point if this is to be unit tested.
def main():
    app.native.window_args['resizable'] = False
    app.native.start_args['debug'] = True
    app.native.settings['ALLOW_DOWNLOADS'] = True
    
    ui.html(STYLE)
    ui.label('Hello NiceGUI!')
    
    possible_values = [1, 5]
    
    render_possible_values(possible_values)
    
    ui.button('Solve Puzzle', on_click=lambda: ui.notify('button was pressed'))
    #ui.table()
    
    #ui.run(native=True, window_size=(400, 300), fullscreen=False)
    ui.run()

main()